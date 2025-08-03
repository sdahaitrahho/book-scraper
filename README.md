# 📚 Book Scraper

A Python web scraper that extracts book data from [Books to Scrape](http://books.toscrape.com), a sandbox website designed for practicing web scraping.

---

## 🚀 Features

- Scrapes **50 pages** of books
- Extracts:
  - ✅ Title
  - ✅ Price
  - ✅ Availability
  - ✅ Rating (converted to number: 1 to 5)
- Saves data in **CSV** and **JSON** formats
- Organized in a **class-based structure**
- Includes **error handling** for bad network responses
- Adds a **1-second delay** between page requests (respectful scraping)

---

## 🧰 Technologies Used

- Python 3.x
- `requests`
- `beautifulsoup4`
- `pandas`

---

## 📁 Project Structure

```

book-scraper/
├── book\_scraper.py           # Main script (class-based)
├── requirements.txt          # Project dependencies
├── README.md                 # You're reading it!
└── data/                     # Output files (auto-created)
├── books.csv             # Scraped book data (CSV format)
└── books.json            # Scraped book data (JSON format)

````

---

## 🧪 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/book-scraper.git
cd book-scraper
````

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate           # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the scraper

```bash
python book_scraper.py
```

Output files will be saved in the `data/` directory.

---

## 📷 Sample Output

### `books.json`

```json
[
  {
    "title": "A Light in the Attic",
    "price": "£51.77",
    "availability": "In stock",
    "rating": 3
  },
  {
    "title": "Tipping the Velvet",
    "price": "£53.74",
    "availability": "In stock",
    "rating": 1
  }
]
```

---

## 📌 Notes

* The scraper targets only the **main listing pages** (not individual book details).
* You can extend it to scrape descriptions, categories, or UPC by following individual book links.
* Ethical scraping practices are followed (delay, public test site).

---

## 🛡️ License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute it.

---

## 🙋‍♂️ About Me

👨‍🏫 **PR in Computer Science**
💻 Learning Web Scraping & Freelance Skills
🌍 Based in Morocco | 🧠 Passionate about real-world data projects
📫 *Available for freelance scraping work — contact via GitHub!*

```
