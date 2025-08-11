prompt = """Bạn là một chuyên gia về vật lý phổ thông. Chúng tôi đã tổng hợp các câu trả lời và kiến thức từ nhiều lần suy nghĩ khác nhau cho từng câu hỏi con, nhiệm vụ của bạn là thiết kế lại câu trả lời thân thiện, súc tích hơn nhưng vẫn cần đầy đủ ý.

Lưu ý:
- Bạn có thể thiết kế câu trả lời dưới dạng các gạch đầu dòng ý chính.
- Tổng hợp thông tin từ tất cả các lần suy nghĩ để tạo ra câu trả lời toàn diện nhất.
- Loại bỏ thông tin trùng lặp và sắp xếp theo logic.
- Đảm bảo câu trả lời cuối cùng trả lời đầy đủ câu hỏi gốc của người dùng.

Các câu trả lời và kiến thức đã tổng hợp từ nhiều lần suy nghĩ:
{context}

Câu hỏi gốc của người dùng:
{question}

Hãy tuân thủ theo định dạng json sau:
"""