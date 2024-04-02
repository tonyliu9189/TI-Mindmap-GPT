import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

#@st.cache_resource
def get_driver():
    #options.binary_location = '/usr/bin/chromium'  # change in production!!!
    return webdriver.Chrome(
        service=Service(
            ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
        ),
        options=options,
    )

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--headless")

driver = get_driver()


def take_screenshot(url):  
    if url:    
        driver.get(url)    
        screenshot_path = "screenshot.png" # define your path where screenshot will be saved    
        driver.save_screenshot(screenshot_path)    
        st.image(screenshot_path)  # Display the screenshot in the Streamlit app  