# VirtualLab - Electrical Circuit Reasoning API

Đây là một API phân tích cấu trúc mạch điện, đánh giá và giải thích chuyên sâu về bản chất hiện tượng vật lý phổ thông.

---

## 🚀 Cài đặt và chạy dự án

### 👉 Tuỳ chọn 1: **Chạy bằng Docker (khuyến nghị)**

#### 1. Clone repository

```bash
git clone https://github.com/nguyenddat/VirtualLab.git
cd VirtualLab
```

#### 2. Tạo file `.env`

Tạo file `.env` tại thư mục gốc với nội dung sau:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> Bạn cần có một API key hợp lệ từ [OpenAI](https://platform.openai.com/account/api-keys).

#### 3. Chạy Docker Compose

```bash
docker compose up --build -d
```

#### 4. Truy cập ứng dụng

Mở trình duyệt và truy cập: [http://localhost:8000](http://localhost:8000)

---

### 👉 Tuỳ chọn 2: **Chạy thủ công với môi trường Python**

#### 1. Clone repository

```bash
git clone https://github.com/nguyenddat/VirtualLab.git
cd VirtualLab
```

#### 2. Tạo file `.env`

Tạo file `.env` tại thư mục gốc với nội dung:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### 3. Cài đặt môi trường (Python 3.12.6)

**Với virtualenv:**
```bash
python -m venv venv
source venv/bin/activate  # hoặc venv\Scripts\activate trên Windows
pip install -r requirements.txt
```

**Hoặc với conda:**
```bash
conda create -n env python=3.12.6
conda activate env
pip install -r requirements.txt
```

#### 4. Chạy server

```bash
uvicorn app.main:app --reload
```

Server sẽ chạy tại `http://127.0.0.1:8000`

---

## ⚡️ Các thiết bị vật lý hỗ trợ

Hệ thống hiện tại hỗ trợ các loại thiết bị sau trong mô hình mạch điện:

- **battery**: Pin, nguồn điện một chiều  
- **bulb**: Bóng đèn điện  
- **voltmeter**: Vôn kế đo hiệu điện thế  
- **ammeter**: Ampe kế đo dòng điện  
- **capacitor**: Tụ điện  
- **wire**: Dây nối

Mỗi thiết bị có các thuộc tính riêng, ví dụ:

- **battery**: `voltage`, `left_socket`, `right_socket`
- **bulb**: `on`, `min_voltage`, `max_voltage`, `left_socket_connected`, `right_socket_connected`
- **voltmeter**: `current`, `left_socket_connected`, `right_socket_connected`
- **ammeter**: `current`, `left_socket_connected`, `right_socket_connected`
- **capacitor**: `charged`, `capacitance`, `left_socket_connected`, `right_socket_connected`
- **wire**: `from`, `to`

Bạn có thể xem chi tiết trong các file:

- `app/models/basic_physics/battery.py`
- `app/models/basic_physics/bulb.py`
- `app/models/basic_physics/voltmeter.py`
- `app/models/basic_physics/ammeter.py`
- `app/models/basic_physics/capacitor.py`
- `app/models/basic_physics/wire.py`

---