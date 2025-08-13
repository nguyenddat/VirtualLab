FROM python:3.12.6

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Cập nhật và cài đặt các gói hệ thống cần thiết cho OCR và PDF xử lý
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-vie \
    poppler-utils \
    libpoppler-cpp-dev \
    netcat-openbsd \
    swig \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Tạo thư mục làm việc
RUN mkdir /app
WORKDIR /app

# Copy toàn bộ source code vào container
COPY . /app/

# Cài đặt thư viện Python
RUN pip install --no-cache-dir \
    pytesseract \
    pdf2image \
    tqdm \
    -r requirements.txt

# Mở cổng cho app (Render sẽ thay bằng $PORT)
EXPOSE 8000

# Sử dụng biến môi trường PORT từ Render, mặc định 8000 nếu chạy local
# CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}`"]
