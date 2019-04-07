import os
import traceback
import sys
import logging
import shutil
from miner.config import tools_path
import re
import requests
import time

from bs4 import BeautifulSoup
from selenium import webdriver


logger = logging.getLogger(__name__)

chromedriver_path = os.path.join(tools_path, "chromedriver.exe")

class Crawler:

    def __init__(self, driver_type='chrome'):
        self.driver_type = driver_type
        if driver_type == 'firefox':
            from selenium.webdriver.firefox.options import Options
            options = Options()
            options.set_headless(headless=True)
            self.driver = webdriver.Firefox(firefox_options=options)
        elif driver_type == 'chrome':
            from selenium.webdriver.chrome.options import Options
            options = Options()  
            options.headless = True
            self.driver = webdriver.Chrome(chromedriver_path, chrome_options = options)

    def _scroll_to_oblivion(self):
        pause = 3
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        i = 0
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(pause)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height or i == 100:
                return i
            last_height = new_height
            i += 1
            

    def get_links(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a', href=re.compile(r'.*/@.*/.*'))
        href_list = set()
        for link in links:
            href = link['href']
            if href.startswith('/'):
                href = "https://medium.com" + href
            href_list.add(href)
        return href_list

    def parse(self, url):
        self.driver.get(url)
        scroll_count = self._scroll_to_oblivion()
        title = self.driver.title
        html = self.driver.page_source
        links = self.get_links(html)
        return {"url": url, "html": html, "links":links, "scroll_count": scroll_count}