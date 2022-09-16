from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time
#pip install -r requirement.txt command to install the necessary, package


S = Service("D:\software\chromedriver.exe")
driver = webdriver.Chrome(service=S)


def scroll_to_end(len_to_scroll: int = 4000, Sleep_between_scroll=5):
    prev_h = 0
    while True:
        driver.execute_script(f"window.scrollTo({prev_h},{prev_h + 1500})")
        time.sleep(Sleep_between_scroll)
        prev_h += 1500
        if prev_h >= (len_to_scroll):
            break


def scrape(no_of_video: int, len_to_scroll = 5000):
    driver.get("https://www.youtube.com/user/krishnaik06")
    driver.implicitly_wait(5)
    driver.execute_script("window.scrollTo(0,900);")
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR,'#tabsContent .ytd-c4-tabbed-header-renderer:nth-child(4) .tp-yt-paper-tab').click()
    driver.implicitly_wait(5)

    scroll_to_end()

    title_box = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

    new_list_title = []
    for i in title_box:
        k = i.get_attribute('title')
        new_list_title.append(k)
        if len(new_list_title) >= no_of_video:
            break



    view_box = driver.find_elements(By.XPATH, '//*[@id="metadata-line"]/span[1]')
    new_list_views = []
    for k in view_box:
        v = k.text
        new_list_views.append(v)
        if len(new_list_views) >= no_of_video:
            break


    time_box = driver.find_elements(By.XPATH, '//*[@id="metadata-line"]/span[2]')
    new_list_upload = []
    for l in time_box:
        upl = l.text
        new_list_upload.append(upl)
        if len(new_list_upload) >= no_of_video:
            break

    url_box = driver.find_elements(By.CSS_SELECTOR, '#video-title')
    new_list_url = []
    for j in url_box:
        u = j.get_attribute('href')
        new_list_url.append(u)
        if len(new_list_url) >= no_of_video:
            break


    my_data_youtube = pd.DataFrame(
        {'title': new_list_title, "url": new_list_url, "views": new_list_views, "upload": new_list_upload})
    return my_data_youtube
    driver.close()
  

k = scrape(50)
print(k)
