from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from emailer import send_emails
import os

options = Options()


location = "C:\\Users\\Harold Obasi\\Documents\\Development\\chromedriver.exe"

options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

service_obj = Service(location)
# driver = webdriver.Chrome(service=service_obj)


sender = "haroldobasi2k16@gmail.com"
recievers = ["haroldobasibackup@gmail.com"]

inec_news = "https://inecnews.com/"

# driver = webdriver.Chrome(location)

driver.get(inec_news)
driver.implicitly_wait(20)

news_titles = driver.find_elements(By.CSS_SELECTOR, ".two-third .post-title")
news_dates = driver.find_elements(By.CSS_SELECTOR,".two-third .post-head .updated")

news = {}

for i in range(len(news_dates)):
  news[i] = {
    "title": news_titles[i].get_attribute("textContent"),
    "date": news_dates[i].get_attribute("textContent")
  }

print(news)

driver.quit()#Content > div > div.sections_group > div > div:nth-child(3) > div > div.wrap.mcb-wrap.two-third.valign-top.clearfix > div > div > div > div > div.posts_group.lm_wrapper.col-2.photo > div.post-item.isotope-item.clearfix.author-rotimi.post-5033.post.type-post.status-publish.format-standard.has-post-thumbnail.hentry.category-uncategorized > div.post-desc-wrapper > div > 