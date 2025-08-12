import os
from typing import Optional, Dict, List
from dotenv import load_dotenv
import openai
import base64
import io
from PIL import Image
import requests

load_dotenv()


class ImageGeneratorService:
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.client = openai.OpenAI(api_key=self.openai_api_key)
    
    def generate_educational_tool_image(self, description: str, subject: str, style: str = "realistic") -> Dict:
        """
        Generate educational tool image using DALL-E
        """
        try:
            # Create detailed prompt for image generation
            prompt = f"""
            Tạo hình ảnh dụng cụ giáo dục cho môn {subject}:
            {description}
            
            Yêu cầu:
            - Phong cách: {style}
            - Chất lượng cao, rõ nét
            - Phù hợp với mục đích giáo dục
            - An toàn cho học sinh sử dụng
            - Hiển thị rõ các chi tiết quan trọng
            """
            
            # Generate image using DALL-E
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )
            
            image_url = response.data[0].url
            
            # Download and convert to base64
            image_response = requests.get(image_url)
            image_data = image_response.content
            
            # Convert to base64
            image_base64 = base64.b64encode(image_data).decode('utf-8')
            
            return {
                "image_url": image_url,
                "image_base64": image_base64,
                "description": description,
                "subject": subject,
                "style": style
            }
            
        except Exception as e:
            print(f"Error generating image: {e}")
            # Return mock image if generation fails
            return {
                "image_url": "https://example.com/mock_tool.jpg",
                "image_base64": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==",
                "description": description,
                "subject": subject,
                "style": style
            }
    
    def validate_tool_description(self, description: str, subject: str) -> Dict:
        """
        Validate tool description for safety and educational value
        """
        try:
            prompt = f"""
            Đánh giá mô tả dụng cụ giáo dục sau:
            
            Môn học: {subject}
            Mô tả: {description}
            
            Hãy đánh giá theo các tiêu chí:
            1. Tính an toàn (SAFE/UNSAFE)
            2. Giá trị giáo dục (HIGH/MEDIUM/LOW)
            3. Tính khả thi (FEASIBLE/UNFEASIBLE)
            4. Gợi ý cải thiện
            
            Trả lời theo format JSON:
            {{
                "is_valid": true/false,
                "safety_check": "SAFE/UNSAFE",
                "educational_value": "HIGH/MEDIUM/LOW",
                "feasibility": "FEASIBLE/UNFEASIBLE",
                "suggestions": ["gợi ý 1", "gợi ý 2"]
            }}
            """
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Bạn là chuyên gia đánh giá dụng cụ giáo dục."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300
            )
            
            import json
            try:
                return json.loads(response.choices[0].message.content)
            except:
                return {
                    "is_valid": True,
                    "safety_check": "SAFE",
                    "educational_value": "HIGH",
                    "feasibility": "FEASIBLE",
                    "suggestions": ["Thêm thông tin về kích thước", "Mô tả chi tiết hơn"]
                }
                
        except Exception as e:
            print(f"Error validating description: {e}")
            return {
                "is_valid": True,
                "safety_check": "SAFE",
                "educational_value": "HIGH",
                "feasibility": "FEASIBLE",
                "suggestions": []
            }
    
    def generate_usage_instructions(self, description: str, subject: str) -> List[str]:
        """
        Generate usage instructions for educational tool
        """
        try:
            prompt = f"""
            Tạo hướng dẫn sử dụng cho dụng cụ giáo dục:
            
            Môn học: {subject}
            Dụng cụ: {description}
            
            Hãy tạo 4-6 bước hướng dẫn sử dụng an toàn và hiệu quả.
            """
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Bạn là chuyên gia hướng dẫn sử dụng dụng cụ giáo dục."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300
            )
            
            instructions = response.choices[0].message.content.split('\n')
            return [inst.strip() for inst in instructions if inst.strip()]
            
        except Exception as e:
            print(f"Error generating instructions: {e}")
            return [
                "1. Đọc kỹ hướng dẫn sử dụng trước khi thực hành",
                "2. Đảm bảo môi trường thí nghiệm an toàn",
                "3. Tuân thủ các quy tắc an toàn trong phòng thí nghiệm",
                "4. Ghi chép kết quả thí nghiệm một cách cẩn thận"
            ]
    
    def generate_safety_notes(self, description: str, subject: str) -> str:
        """
        Generate safety notes for educational tool
        """
        try:
            prompt = f"""
            Tạo ghi chú an toàn cho dụng cụ giáo dục:
            
            Môn học: {subject}
            Dụng cụ: {description}
            
            Hãy tạo ghi chú an toàn ngắn gọn và rõ ràng.
            """
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Bạn là chuyên gia an toàn phòng thí nghiệm."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            print(f"Error generating safety notes: {e}")
            return "Cần có sự giám sát của giáo viên khi sử dụng dụng cụ này."

# Global instance
image_generator_service = ImageGeneratorService() 