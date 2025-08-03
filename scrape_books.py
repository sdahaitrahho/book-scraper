import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import os
import time

class BookScraper:
    def __init__(self):
        self.base_url = "http://books.toscrape.com/catalogue/page-{}.html"
        self.book_data = []
        self.output_dir = './book-scraper/data'
        self.rating_map = {
            'One': 1,
            'Two': 2,
            'Three': 3,
            'Four': 4,
            'Five': 5
        }

    def get_books_from_page(self, page_number):
        url = self.base_url.format(page_number)
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise HTTPError for bad status
        except requests.RequestException as e:
            print(f"[!] Error fetching page {page_number}: {e}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.select('article.product_pod')

        for book in books:
            title = book.h3.a['title']
            price = book.select_one('.price_color').text
            availability = book.select_one('.availability').text.strip()
            rating_word = book.p['class'][1]
            rating = self.rating_map.get(rating_word, 0)

            self.book_data.append({
                'title': title,
                'price': price,
                'availability': availability,
                'rating': rating
            })

    def scrape_all_pages(self, total_pages=50):
        print("🔍 Starting scraping...")
        for page in range(1, total_pages + 1):
            print(f"📄 Scraping page {page}")
            self.get_books_from_page(page)
            time.sleep(1)  # Be polite and avoid hammering the server
        print("✅ Scraping complete!")

    def save_data(self):
        os.makedirs(self.output_dir, exist_ok=True)
        df = pd.DataFrame(self.book_data)

        # Save to CSV
        csv_path = os.path.join(self.output_dir, 'books.csv')
        df.to_csv(csv_path, index=False, encoding='utf-8')
        print(f"💾 CSV saved to {csv_path}")

        # Save to JSON
        json_path = os.path.join(self.output_dir, 'books.json')
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(self.book_data, f, indent=4)
        print(f"💾 JSON saved to {json_path}")

    def run(self):
        self.scrape_all_pages()
        self.save_data()

# ✅ Run the scraper
if __name__ == "__main__":
    scraper = BookScraper()
    scraper.run()
