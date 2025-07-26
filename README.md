# VirtualLab - Electrical Circuit Reasoning API

Đây là một API phân tích cấu trúc mạch điện, đánh giá và giải thích chuyên sâu về bản chất hiện tượng vật lý phổ thông.

---

## 🚀 Cài đặt và chạy dự án

### 1. Clone repository

```bash
git clone https://github.com/nguyenddat/VirtualLab.git
cd VirtualLab
```

### 2. Tạo file `.env`

Tạo file `.env` tại thư mục gốc và thêm dòng sau:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> Bạn cần có một API key hợp lệ từ [OpenAI](https://platform.openai.com/account/api-keys).

### 3. Cài đặt môi trường (Python >= 3.8)

Khuyên dùng virtualenv:

```bash
python -m venv venv
source venv/bin/activate  # hoặc venv\Scripts\activate trên Windows
pip install -r requirements.txt
```

### 4. Chạy server

```bash
uvicorn app.main:app --reload
```

Server sẽ chạy tại `http://127.0.0.1:8000`

---

## 🔌 Gọi API phân tích mạch điện

### Endpoint:

```
POST /api/physics/explain
```

### Headers:

```json
Content-Type: application/json
```

### Request body ví dụ:

```json
{
  "graph": { "devices": [...], "connections": [...] },
  "question": "Phân tích chi tiết lý do tại sao tất cả các bóng đèn đều không sáng, ampe kế không đo được dòng, vôn kế không có số chỉ và tụ điện không tích điện."
}
```

> Phần `graph` là mô hình mạch điện, gồm các thiết bị và dây nối như pin, bóng đèn, tụ điện, ampe kế, vôn kế...

### Response mẫu:

```json
{
  "response": "Tất cả các bóng đèn không sáng vì mạch bị hở tại ..."
}
```

---

## 🧪 Dữ liệu test mẫu

```json
{
  "graph": {
    "devices": [
      {"name": "battery1", "type": "battery", "position": {"x": 0, "y": 0}, "properties": {"voltage": 12.0, "left_socket": "positive", "right_socket": "negative"}},
      {"name": "bulb1", "type": "bulb", "position": {"x": 1, "y": 0}, "properties": {"on": false, "min_voltage": 2.0, "max_voltage": 12.0, "left_socket_connected": true, "right_socket_connected": true}},
      {"name": "bulb2", "type": "bulb", "position": {"x": 2, "y": 0}, "properties": {"on": false, "min_voltage": 2.0, "max_voltage": 12.0, "left_socket_connected": true, "right_socket_connected": true}},
      {"name": "bulb3", "type": "bulb", "position": {"x": 1, "y": 1}, "properties": {"on": false, "min_voltage": 2.0, "max_voltage": 12.0, "left_socket_connected": true, "right_socket_connected": true}},
      {"name": "ammeter1", "type": "ammeter", "position": {"x": 2, "y": 1}, "properties": {"current": 0.0, "left_socket_connected": true, "right_socket_connected": true}},
      {"name": "voltmeter1", "type": "voltmeter", "position": {"x": 3, "y": 0}, "properties": {"current": 0.0, "left_socket_connected": true, "right_socket_connected": true}},
      {"name": "capacitor1", "type": "capacitor", "position": {"x": 3, "y": 1}, "properties": {"charged": false, "capacitance": 0.002, "left_socket_connected": true, "right_socket_connected": true}}
    ],
    "connections": [
      {"name": "wire1", "type": "wire", "properties": {"from": "battery1.right_socket", "to": "bulb1.left_socket"}},
      {"name": "wire2", "type": "wire", "properties": {"from": "bulb1.right_socket", "to": "bulb2.left_socket"}},
      {"name": "wire3", "type": "wire", "properties": {"from": "bulb2.right_socket", "to": "ammeter1.left_socket"}},
      {"name": "wire4", "type": "wire", "properties": {"from": "ammeter1.right_socket", "to": "capacitor1.left_socket"}},
      {"name": "wire5", "type": "wire", "properties": {"from": "capacitor1.right_socket", "to": "battery1.left_socket"}},
      {"name": "wire6", "type": "wire", "properties": {"from": "battery1.right_socket", "to": "bulb3.left_socket"}},
      {"name": "wire7", "type": "wire", "properties": {"from": "bulb3.right_socket", "to": "voltmeter1.left_socket"}},
      {"name": "wire8", "type": "wire", "properties": {"from": "voltmeter1.right_socket", "to": "battery1.left_socket"}}
    ]
  },
  "question": "Phân tích chi tiết lý do tại sao tất cả các bóng đèn đều không sáng, ampe kế không đo được dòng, vôn kế không có số chỉ và tụ điện không tích điện."
}
```

---