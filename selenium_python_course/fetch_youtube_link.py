import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    all_links = []
    driver.get("https://www.youtube.com/@LearnEnglishWithTVSeries/videos")
    for i in range(50):
        all_object = driver.find_elements(By.XPATH, "//a[@id='video-title-link']")
        for obj in all_object:
            link = obj.get_attribute('href')
            if link not in all_links:
                all_links.append(link)
            else:
                continue
        driver.execute_script("window.scrollBy(0,10000)")
        time.sleep(1)
    print(all_links)
    print(len(all_links))

