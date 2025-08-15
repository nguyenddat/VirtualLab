INSERT INTO experiment (
    name, 
    description, 
    status, 
    public_status, 
    chapter_id, 
    created_by
) VALUES
(
  'Thí nghiệm kiểm chứng cường độ dòng điện',
  'Mục đích: Kiểm chứng tác dụng mạnh hay yếu của dòng điện bằng cách quan sát sự thay đổi cường độ dòng điện và độ sáng của bóng đèn khi thay đổi điện trở. Dụng cụ: pin, dây nối, khóa K, biến trở, ampe kế, bóng đèn sợi đốt.',
  'blank',
  'public',
  4,
  3
),
(
  'Thí nghiệm đo suất điện động và điện trở trong của nguồn điện',
  'Mục đích: Đo suất điện động và điện trở trong của pin mới và pin đã qua sử dụng. Cơ sở lý thuyết: Quan hệ giữa I và U tuân theo công thức U = E - I(R0 + r), vẽ đồ thị U - I để xác định E và r.',
  'blank',
  'public',
  4,
  3
);