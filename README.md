# 📦 Logistics Cost Analyzer (LCA)

> **Tool Python tự động so sánh giá cước vận chuyển (Freight Comparison Automation).**

![Status](https://img.shields.io/badge/Status-Active-success) ![Python](https://img.shields.io/badge/Python-3.10-blue) ![Excel](https://img.shields.io/badge/Excel-Integration-217346)

## 📸 Demo Kết Quả (Dashboard)
Dưới đây là giao diện phân tích chi phí sau khi Tool chạy xong:

<img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" width="100%" style="border-radius: 10px">

## 🚩 Vấn đề thực tế
Là nhân viên Purchasing, mỗi khi nhập hàng tôi nhận được rất nhiều file báo giá từ các Forwarder (DHL, Kuehne+Nagel...).
* **Khó khăn:** Mỗi bên một form Excel khác nhau.
* **Tốn thời gian:** Mất **45 phút** để nhập tay vào file so sánh.
* **Dễ sai sót:** Tính nhầm tỷ giá hoặc sót phí Local Charge.

## 💡 Giải pháp của tôi
Tôi viết một Script Python để:
1.  **Đọc tự động** các file báo giá đầu vào.
2.  **Quy đổi tỷ giá** USD/VND tự động.
3.  **So sánh & Tô màu** phương án rẻ nhất (Best Option).

## 📂 Cách sử dụng
```bash
# 1. Bỏ file báo giá vào thư mục input
# 2. Chạy lệnh:
python src/main.py
