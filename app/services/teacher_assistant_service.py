import os
import json
from typing import Dict, Optional, Any
from dotenv import load_dotenv
from openai import OpenAI
from openai import APIConnectionError, RateLimitError, BadRequestError

load_dotenv()


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    v = os.getenv(name, default)
    if v is not None and isinstance(v, str):
        v = v.strip()
    return v


class TeacherAssistantService:
    def __init__(self):
        self.openai_api_key = _env("OPENAI_API_KEY")
        if not self.openai_api_key:
            raise RuntimeError(
                "OPENAI_API_KEY chưa được thiết lập. Thêm vào .env hoặc export biến môi trường."
            )

        # Cho phép chọn model qua ENV, mặc định gpt-4o-mini
        self.model = _env("OPENAI_MODEL", "gpt-4o-mini")
        self.temperature = float(_env("OPENAI_TEMPERATURE", "0.3"))

        # Dùng đúng API key của bạn
        self.client = OpenAI(api_key=self.openai_api_key)

        # Log nhẹ để chắc chắn bản này đã được load
        print(f"[TeacherAssistantService] START model={self.model} temp={self.temperature}")

    # --- helpers -------------------------------------------------------------

    def _json_completion(self, system_prompt: str, user_prompt: str, max_tokens: int) -> Dict[str, Any]:
        """Gọi model và ÉP trả JSON hợp lệ (không trả mock)."""
        resp = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            response_format={"type": "json_object"},
            temperature=self.temperature,
            max_tokens=max_tokens,
        )
        content = resp.choices[0].message.content
        # print("LLM RAW ->", content)  # bật khi cần debug
        return json.loads(content)

    @staticmethod
    def _sanitize_list(x: Any) -> list:
        """Đảm bảo trả về list các string sạch sẽ, bỏ rỗng/placeholder."""
        if not isinstance(x, list):
            return []
        cleaned = []
        for it in x:
            if isinstance(it, str):
                s = it.strip().rstrip(". ").replace("...", "").strip()
                if s and "example.com" not in s:
                    cleaned.append(s)
        return cleaned

    # --- public APIs ---------------------------------------------------------

    def generate_teaching_response(
        self,
        query: str,
        subject: str,
        grade: str,
        context: Optional[str] = None,
        topic: Optional[str] = None,
    ) -> Dict:
        """
        Tạo phản hồi trợ giảng cho giáo viên
        """
        try:
            system_prompt = (
                "Bạn là trợ lý AI cho giáo viên. "
                "Luôn trả lời bằng tiếng Việt, chính xác, thực tế, có thể triển khai ngay tại lớp. "
                "Không dùng placeholder, không dùng dấu ba chấm, không bịa URL. "
                "Nếu không có nguồn tham khảo tin cậy thì để mảng resources rỗng."
            )

            user_prompt = f"""
Bạn đang hỗ trợ môn {subject} lớp {grade}.
Chủ đề: {topic or "Không có"}
Câu hỏi của giáo viên: {query}
Bối cảnh thêm: {context or "Không có"}

Chỉ trả về **JSON** với các trường sau (đúng kiểu):
- answer: string (tối thiểu 3 câu, có ví dụ minh họa ngắn)
- teaching_tips: string[] (>=3 mục, hành động cụ thể, có thể áp dụng ngay)
- common_mistakes: string[] (>=3 mục, nêu rõ nhầm lẫn và cách khắc phục)
- assessment_questions: string[] (>=3 câu, đa dạng mức độ)
- resources: string[] (0..5 đường link thật, KHÔNG dùng example.com; nếu không chắc chắn, để mảng rỗng)

YÊU CẦU:
- Tuyệt đối không dùng dấu "..." hay cụm kiểu "v.v.", "etc".
- Không chèn Markdown code block, không tiêu đề thừa.
- Nội dung ngắn gọn nhưng đầy đủ, dùng ngôn từ sư phạm.
"""

            data = self._json_completion(system_prompt, user_prompt, max_tokens=1000)

            # Hậu xử lý nhẹ để tránh rác/placeholder
            result = {
                "answer": str(data.get("answer", "")).strip().replace("...", "").strip(),
                "teaching_tips": self._sanitize_list(data.get("teaching_tips")),
                "common_mistakes": self._sanitize_list(data.get("common_mistakes")),
                "assessment_questions": self._sanitize_list(data.get("assessment_questions")),
                "resources": self._sanitize_list(data.get("resources")),
            }
            return result

        except (APIConnectionError, RateLimitError, BadRequestError) as e:
            return {
                "answer": f"Lỗi khi gọi mô hình: {e.__class__.__name__}",
                "teaching_tips": [],
                "common_mistakes": [],
                "assessment_questions": [],
                "resources": []
            }
        except Exception as e:
            return {
                "answer": f"Có lỗi xảy ra: {str(e)}",
                "teaching_tips": [],
                "common_mistakes": [],
                "assessment_questions": [],
                "resources": []
            }

    def generate_lesson_plan(
        self,
        subject: str,
        grade: str,
        topic: str,
        duration: int = 45
    ) -> Dict:
        """Tạo kế hoạch bài giảng."""
        try:
            system_prompt = (
                "Bạn là chuyên gia thiết kế bài giảng. "
                "Trả lời bằng JSON, súc tích, có thể dạy ngay."
            )
            user_prompt = f"""
Tạo kế hoạch bài giảng cho môn {subject} lớp {grade}, chủ đề: {topic}
Thời lượng: {duration} phút

Chỉ trả về JSON:
- topic: string
- duration: number
- objectives: string[] (3-5 mục, theo SMART)
- activities: {{time: string, activity: string, description: string}}[] (4-6 hoạt động)
- materials: string[] (tối đa 8 mục)
- assessment: string[] (2-4 mục, tiêu chí đánh giá rõ)
"""
            data = self._json_completion(system_prompt, user_prompt, max_tokens=900)

            return {
                "topic": str(data.get("topic", topic)).strip(),
                "duration": int(data.get("duration", duration) or duration),
                "objectives": self._sanitize_list(data.get("objectives")),
                "activities": data.get("activities", []),
                "materials": self._sanitize_list(data.get("materials")),
                "assessment": self._sanitize_list(data.get("assessment")),
            }

        except Exception as e:
            return {
                "topic": topic,
                "duration": duration,
                "objectives": [],
                "activities": [],
                "materials": [],
                "assessment": [],
                "error": f"Có lỗi xảy ra: {str(e)}"
            }

    def generate_assessment(
        self,
        subject: str,
        grade: str,
        topic: str,
        difficulty: str = "medium"
    ) -> Dict:
        """Tạo đề kiểm tra."""
        try:
            system_prompt = (
                "Bạn là chuyên gia ra đề kiểm tra THPT. "
                "Mỗi câu hỏi phải rõ ràng, có đáp án và giải thích ngắn."
            )
            user_prompt = f"""
Tạo bài kiểm tra cho môn {subject} lớp {grade}, chủ đề: {topic}
Độ khó: {difficulty}

Chỉ trả về JSON:
- topic: string
- difficulty: string
- questions: {{
    type: "multiple_choice" | "short_answer",
    question: string,
    options?: string[],          # bắt buộc nếu multiple_choice
    correct_answer: string,
    explanation: string
  }}[] (6-10 câu)
- time_limit: number (phút)
- total_points: number
"""
            data = self._json_completion(system_prompt, user_prompt, max_tokens=1000)

            # sanitize sơ bộ
            questions = data.get("questions", [])
            if isinstance(questions, list):
                for q in questions:
                    if isinstance(q, dict):
                        # bỏ dấu "..." trong câu hỏi/giải thích
                        for k in ["question", "explanation", "correct_answer"]:
                            if k in q and isinstance(q[k], str):
                                q[k] = q[k].replace("...", "").strip()

            return {
                "topic": str(data.get("topic", topic)).strip(),
                "difficulty": str(data.get("difficulty", difficulty)).strip(),
                "questions": questions,
                "time_limit": int(data.get("time_limit", 45) or 45),
                "total_points": int(data.get("total_points", 10) or 10),
            }

        except Exception as e:
            return {
                "topic": topic,
                "difficulty": difficulty,
                "questions": [],
                "time_limit": 45,
                "total_points": 10,
                "error": f"Có lỗi xảy ra: {str(e)}"
            }


# Global instance
teacher_assistant_service = TeacherAssistantService()
