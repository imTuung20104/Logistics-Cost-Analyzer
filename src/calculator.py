import pandas as pd

def calculate_final_price(row):
    """
    Hàm tính toán giá cước cuối cùng (Total Cost)
    Quy đổi tất cả về VND dựa trên tỷ giá hiện tại.
    """
    # Giả định tỷ giá (trong thực tế sẽ lấy từ API hoặc file config)
    usd_rate = 25350 
    
    # Logic: Nếu báo giá là USD thì nhân tỷ giá, nếu VND thì giữ nguyên
    if row['Currency'] == 'USD':
        ocean_freight = row['Ocean_Freight'] * usd_rate
    else:
        ocean_freight = row['Ocean_Freight']

    # Tổng = Cước biển + Các loại phí local
    total = ocean_freight + row['THC_Fee'] + row['CIC_Fee'] + row['Handling_Fee']
    
    return total
