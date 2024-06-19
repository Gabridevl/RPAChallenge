from RPA.Browser.Selenium import Selenium
from RPA.Excel.Files import Files
from RPA.HTTP import HTTP
from datetime import datetime, timedelta
import re
import os

# Instanciar as bibliotecas
browser = Selenium()
excel = Files()
http = HTTP()

def open_website(url):
    browser.open_available_browser(url)

def search_news(phrase, category):
    browser.input_text("input[name='q']", phrase)
    browser.press_keys("input[name='q']", "\ue007")  # Press Enter
    if category:
        browser.click_link(category)

def scrape_news(months):
    news_data = []
    articles = browser.find_elements("//article")
    for article in articles:
        title = article.find_element_by_tag_name("h1").text
        date_str = article.find_element_by_tag_name("time").get_attribute("datetime")
        date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
        if date < datetime.now() - timedelta(days=30*months):
            continue
        description = article.find_element_by_tag_name("p").text
        image_url = article.find_element_by_tag_name("img").get_attribute("src")
        money_in_text = bool(re.search(r"\$\d+|\d+ dollars|\d+ USD", title + description))
        news_data.append((title, date_str, description, image_url, title.count(phrase) + description.count(phrase), money_in_text))
        save_image(image_url, title)
    return news_data

def save_image(url, title):
    filename = f"output/{title[:50]}.jpg"
    http.download(url, filename)
    return filename

def save_to_excel(data):
    excel.create_workbook("output/news.xlsx")
    excel.append_worksheet("Sheet", data)
    excel.save_workbook()

def main(search_phrase, news_category, months):
    open_website("https://www.aljazeera.com/")
    search_news(search_phrase, news_category)
    news_data = scrape_news(months)
    save_to_excel(news_data)
    browser.close_all_browsers()

if __name__ == "__main__":
    main("example phrase", "example category", 2)
