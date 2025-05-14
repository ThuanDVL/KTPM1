import time
import csv
import requests
from bs4 import BeautifulSoup
import json
import os


class DataCollector:
    def __init__(self, url, css_selector_name, css_selector_price, product_container_selector='.product-info'):
        self.url = url
        self.css_selector_name = css_selector_name
        self.css_selector_price = css_selector_price
        self.product_container_selector = product_container_selector

    def collect_data(self):
        print("Đang khởi tạo...")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0'
        }
        
        try:
            print(f"Đang truy cập trang web: {self.url}")
            response = requests.get(self.url, headers=headers, timeout=30)
            response.raise_for_status()
            
            print("Đang phân tích dữ liệu...")
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # In ra HTML để debug
            print("HTML của trang web:")
            print(soup.prettify()[:1000])  # In 1000 ký tự đầu tiên
            
            # Tìm tất cả sản phẩm
            items = soup.select(self.product_container_selector)
            print(f"Tìm thấy {len(items)} sản phẩm")
            
            if not items:
                # Thử các selector khác
                alternative_selectors = [
                    '.product__item',
                    '.item',
                    '.product',
                    '.product-item',
                    '.product__list .item',
                    '.product__list .product__item'
                ]
                
                for selector in alternative_selectors:
                    items = soup.select(selector)
                    if items:
                        print(f"Tìm thấy {len(items)} sản phẩm với selector: {selector}")
                        break
            
            data = []
            seen_products = set()
            
            for index, item in enumerate(items, 1):
                try:
                    # Lấy tên sản phẩm
                    name_element = item.select_one(self.css_selector_name)
                    if not name_element:
                        print(f"Bỏ qua sản phẩm {index}: Không tìm thấy tên")
                        continue
                    name = name_element.text.strip()
                    
                    # Lấy giá
                    price_element = item.select_one(self.css_selector_price)
                    if not price_element:
                        print(f"Bỏ qua sản phẩm {index}: Không tìm thấy giá")
                        continue
                    price = price_element.text.strip()
                    
                    # Kiểm tra sản phẩm trùng lặp
                    product_key = f"{name}|{price}"
                    if product_key in seen_products:
                        print(f"Bỏ qua sản phẩm {index}: Sản phẩm trùng lặp")
                        continue
                    
                    seen_products.add(product_key)
                    data.append((name, price))
                    print(f"Sản phẩm {index}: {name} - {price}")
                except Exception as e:
                    print(f"Lỗi khi thu thập dữ liệu sản phẩm {index}: {str(e)}")
                    continue

            print(f"Đã thu thập thành công {len(data)} sản phẩm (đã loại bỏ sản phẩm trùng lặp và không hợp lệ)")
            return data
            
        except Exception as e:
            print(f"Lỗi trong quá trình thu thập dữ liệu: {str(e)}")
            return []

    def save_to_csv(self, data, filename):
        try:
            # Lấy đường dẫn đầy đủ của file
            full_path = os.path.abspath(filename)
            
            with open(filename, mode='w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Tên sản phẩm", "Giá"])
                writer.writerows(data)
            print(f"Đã lưu dữ liệu thành công vào file: {full_path}")
        except Exception as e:
            print(f"Lỗi khi lưu file CSV: {str(e)}")


def get_website_config(website_name):
    """
    Cấu hình cho các trang web khác nhau
    """
    configs = {
        'cellphones': {
            'url': 'https://cellphones.com.vn/laptop.html',
            'name_selector': '.product__name',
            'price_selector': '.product__price--show',
            'container_selector': '.product__item'
        },
        'fpt': {
            'url': 'https://fptshop.com.vn/laptop',
            'name_selector': '.product__name',
            'price_selector': '.product__price--show',
            'container_selector': '.product__item'
        },
        'fat4g': {
            'url': 'https://fat4g.com.vn/laptop',
            'name_selector': '.product-name',
            'price_selector': '.product-price',
            'container_selector': '.product-item'
        },
        'myuda': {
            'url': 'https://myuda.com.vn/laptop',
            'name_selector': '.product-name',
            'price_selector': '.product-price',
            'container_selector': '.product-item'
        },
        'thegioididong': {
            'url': 'https://www.thegioididong.com/laptop',
            'name_selector': 'h3',
            'price_selector': '.price',
            'container_selector': '.item'
        },
        'hoanghamobile': {
            'url': 'https://hoanghamobile.com/laptop',
            'name_selector': '.product-name',
            'price_selector': '.product-price',
            'container_selector': '.product-item'
        },
        'phongvu': {
            'url': 'https://phongvu.vn/laptop',
            'name_selector': '.product-name',
            'price_selector': '.product-price',
            'container_selector': '.product-item'
        },
        'nguyenkim': {
            'url': 'https://www.nguyenkim.com/laptop/',
            'name_selector': '.product-name',
            'price_selector': '.product-price',
            'container_selector': '.product-item'
        },
        'mediamart': {
            'url': 'https://mediamart.vn/laptop/',
            'name_selector': '.product-name',
            'price_selector': '.product-price',
            'container_selector': '.product-item'
        },
        'dienmayxanh': {
            'url': 'https://www.dienmayxanh.com/laptop',
            'name_selector': '.product-name',
            'price_selector': '.product-price',
            'container_selector': '.product-item'
        }
    }
    return configs.get(website_name)


if __name__ == "__main__":
    print("=== Bắt đầu thu thập dữ liệu sản phẩm ===")
    
    # Danh sách các website có thể crawl
    available_websites = [
        'thegioididong',
        'cellphones',
        'fpt',
        'fat4g',
        'myuda',
        'hoanghamobile',
        'phongvu',
        'nguyenkim',
        'mediamart',
        'dienmayxanh'
    ]
    
    print("\nCác website có thể crawl:")
    for i, website in enumerate(available_websites, 1):
        print(f"{i}. {website}")
    
    # Chọn website muốn crawl
    website_name = input("\nNhập tên website muốn crawl (hoặc nhập 'all' để crawl tất cả): ").lower()
    
    if website_name == 'all':
        for website in available_websites:
            print(f"\n=== Đang crawl dữ liệu từ {website} ===")
            config = get_website_config(website)
            if config:
                collector = DataCollector(
                    url=config['url'],
                    css_selector_name=config['name_selector'],
                    css_selector_price=config['price_selector'],
                    product_container_selector=config['container_selector']
                )
                data = collector.collect_data()
                if data:
                    filename = f"{website}_data.csv"
                    collector.save_to_csv(data, filename)
                time.sleep(5)  # Delay 5 giây giữa các request
    else:
        # Lấy cấu hình cho website
        config = get_website_config(website_name)
        if not config:
            print(f"Không tìm thấy cấu hình cho website: {website_name}")
            exit()
        
        # Khởi tạo collector với cấu hình của website
        collector = DataCollector(
            url=config['url'],
            css_selector_name=config['name_selector'],
            css_selector_price=config['price_selector'],
            product_container_selector=config['container_selector']
        )

        # Thu thập và lưu dữ liệu
        data = collector.collect_data()
        if data:
            filename = f"{website_name}_data.csv"
            collector.save_to_csv(data, filename)
        else:
            print("Không thu thập được dữ liệu nào. Vui lòng kiểm tra lại cấu trúc trang web hoặc CSS selectors.")
    
    print("\n=== Hoàn thành ===")

