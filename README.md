# 📦 Logistics Cost Analyzer (LCA)

> **Tool Python tự động so sánh giá cước vận chuyển (Freight Comparison).**

![Status](https://img.shields.io/badge/Status-Active-success) ![Python](https://img.shields.io/badge/Python-3.10-blue)

## 📸 Demo Kết Quả
Đây là báo cáo so sánh giá cước tự động được xuất ra từ Tool:

<img src="https://images.unsplash.com/photo-1542744094-24638eff58b5?q=80&w=1000&auto=format&fit=crop" width="100%" style="border-radius: 10px">

## 🚩 Vấn đề
Mỗi Forwarder gửi báo giá một kiểu (Excel, PDF). Việc nhập tay vào file so sánh tốn **45 phút/lô hàng** và dễ sai sót.

## 💡 Giải pháp
Tool này sẽ:
1.  Đọc file báo giá thô.
2.  Tự động quy đổi tỷ giá (USD -> VND).
3.  Tính tổng chi phí: `Cước biển + Local Charge + Trucking`.
4.  **Tô màu xanh** cho bên nào có giá rẻ nhất.

## 📂 Cách chạy (How to run)
```bash
python src/main.py
