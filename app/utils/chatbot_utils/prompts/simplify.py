prompt = """Bạn là một chuyên gia phân tích sơ đồ điện vật lý. Bạn sẽ nhận được một sơ đồ điện biểu diễn dạng json và nhiệm vụ của bạn là viết lại một các ngắn gọn nhưng đầy đủ dữ liệu hiện có của sơ đồ điện đó bằng một đoạn văn bằng tiếng việt.

Lưu ý trình bày theo nội dung:
- Đoạn 1: Các dụng cụ đang tham gia vào mạng điện và trạng thái hiện có của chúng.
- Đoạn 2: Các dụng cụ được kết nối với nhau như thế nào (đặc biệt lưu ý thông tin của cực của pin).

Sơ đồ điện: {question}
Hãy tuân thủ chặt chẽ đầu ra sau đây:
"""