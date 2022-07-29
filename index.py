from selenium import webdriver
from emailer import send_emails
import os

location = "C:\\Users\\Harold Obasi\\Documents\\Development\\chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

sender = "haroldobasi2k16@gmail.com"
recievers = ["haroldobasibackup@gmail.com"]

inec_news = "https://inecnews.com/"

# driver = webdriver.Chrome(location)

driver.get(inec_news)

news_dates = driver.find_elements_by_css_selector(".two-third .post-head .updated")
news_titles = driver.find_elements_by_css_selector(".two-third .post-title")

news = {}

for i in range(len(news_dates)):
  news[i] = {
    "title": news_titles[i].text,
    "date": news_dates[i].text
  }

send_emails("haroldobasi2k19@gmail.com", {"subject": "Testing Final", "body": "Placeholder"}, news)
print("news: ", news)
driver.quit()