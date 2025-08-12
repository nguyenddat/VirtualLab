# Education AI Services API

## Tổng quan

API này cung cấp 3 dịch vụ AI chính cho giáo dục:

1. **AI Gia sư (RAG)** - Trả lời câu hỏi dựa trên sách giáo khoa với citation chính xác
2. **AI Hỗ trợ Giáo viên** - Hỗ trợ giáo viên trong việc giảng dạy và tạo bài giảng
3. **AI Tạo sinh Dụng cụ** - Tạo hình ảnh dụng cụ giáo dục từ mô tả văn bản

## API Endpoints

### 1. AI Gia sư (RAG)

#### POST `/api/education/tutor/query`
Trả lời câu hỏi của học sinh với citation từ sách giáo khoa

**Request:**
```json
{
  "subject": "physics",
  "grade": "10", 
  "topic": "Động lực học",
  "question": "Tại sao xe đạp không đổ khi chạy?"
}
```

**Response:**
```json
{
  "answer": "Dựa trên sách giáo khoa Vật lý 10...",
  "citations": [
    {
      "page": 45,
      "content": "Nội dung từ sách giáo khoa...",
      "chapter": "Chương 2: Cơ học",
      "section": "2.3 Động lực học"
    }
  ],
  "related_topics": ["Động năng", "Thế năng", "Cơ năng"],
  "confidence_score": 0.85
}
```

#### GET `/api/education/tutor/subjects`
Lấy danh sách các môn học có sẵn

### 2. AI Hỗ trợ Giáo viên

#### POST `/api/education/teacher/assist`
Hỗ trợ giáo viên trả lời câu hỏi và đưa ra gợi ý giảng dạy

**Request:**
```json
{
  "subject": "physics",
  "grade": "10",
  "topic": "Điện học",
  "question": "Làm thế nào để giảng dạy hiệu quả về mạch điện?",
  "context": "Lớp có 30 học sinh, 45 phút"
}
```

**Response:**
```json
{
  "answer": "Để giảng dạy hiệu quả về mạch điện...",
  "teaching_tips": [
    "Bắt đầu với ví dụ thực tế",
    "Sử dụng sơ đồ tư duy"
  ],
  "common_mistakes": [
    "Học sinh thường nhầm lẫn giữa..."
  ],
  "assessment_questions": [
    "Câu hỏi 1: Giải thích tại sao..."
  ],
  "resources": [
    "Video giảng dạy: https://example.com/video1"
  ]
}
```

#### POST `/api/education/teacher/lesson-plan`
Tạo kế hoạch bài giảng

#### POST `/api/education/teacher/assessment`
Tạo bài kiểm tra/đánh giá

### 3. AI Tạo sinh Dụng cụ

#### POST `/api/education/tools/generate`
Tạo hình ảnh dụng cụ giáo dục từ mô tả

**Request:**
```json
{
  "description": "Máy đo điện áp 0-12V với màn hình LCD, dùng cho thí nghiệm mạch điện",
  "subject": "physics",
  "grade": "10",
  "style": "realistic",
  "size": "medium"
}
```

**Response:**
```json
{
  "image_url": "https://example.com/generated_tool.jpg",
  "image_base64": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==",
  "description": "Dụng cụ Máy đo điện áp... cho môn physics lớp 10",
  "usage_instructions": [
    "1. Đọc kỹ hướng dẫn sử dụng...",
    "2. Đảm bảo môi trường thí nghiệm an toàn..."
  ],
  "safety_notes": "Cần có sự giám sát của giáo viên...",
  "related_experiments": [
    "Thí nghiệm 1: Khảo sát tính chất...",
    "Thí nghiệm 2: Đo lường các thông số..."
  ]
}
```

#### GET `/api/education/tools/categories`
Lấy danh sách các loại dụng cụ theo môn học

#### POST `/api/education/tools/validate`
Kiểm tra tính hợp lệ của mô tả dụng cụ

#### GET `/api/education/tools/templates`
Lấy các template mô tả dụng cụ theo môn học

## Cách sử dụng

### 1. Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### 2. Thiết lập environment variables
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Chạy server
```bash
uvicorn app.main:app --reload
```

### 4. Truy cập API documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Cấu trúc dự án

```
app/
├── api/
│   ├── education/
│   │   ├── tutor.py              # AI Gia sư (RAG)
│   │   ├── teacher_assistant.py  # AI Hỗ trợ Giáo viên
│   │   └── tool_generator.py     # AI Tạo sinh Dụng cụ
│   └── physics/                  # API Vật lý hiện tại
├── services/
│   ├── rag_service.py            # RAG service
│   ├── teacher_assistant_service.py  # Teacher assistant service
│   └── image_generator_service.py    # Image generation service
└── main.py                       # FastAPI app
```

## Tính năng chính

### AI Gia sư (RAG)
- ✅ Trả lời câu hỏi dựa trên sách giáo khoa
- ✅ Citation chính xác với trang số và nội dung
- ✅ Hỗ trợ nhiều môn học và lớp học
- ✅ Độ tin cậy cao với confidence score

### AI Hỗ trợ Giáo viên
- ✅ Trả lời câu hỏi giảng dạy
- ✅ Đưa ra gợi ý giảng dạy thực tế
- ✅ Chỉ ra lỗi phổ biến của học sinh
- ✅ Tạo kế hoạch bài giảng
- ✅ Tạo bài kiểm tra/đánh giá

### AI Tạo sinh Dụng cụ
- ✅ Tạo hình ảnh dụng cụ từ mô tả văn bản
- ✅ Kiểm tra tính an toàn và giá trị giáo dục
- ✅ Tạo hướng dẫn sử dụng
- ✅ Hỗ trợ nhiều phong cách (realistic, cartoon, technical)

## Roadmap

- [ ] Tích hợp với cơ sở dữ liệu sách giáo khoa thực tế
- [ ] Thêm tính năng chat real-time
- [ ] Tích hợp với hệ thống LMS
- [ ] Thêm tính năng đánh giá và feedback
- [ ] Tối ưu hóa performance cho RAG
- [ ] Thêm tính năng đa ngôn ngữ 