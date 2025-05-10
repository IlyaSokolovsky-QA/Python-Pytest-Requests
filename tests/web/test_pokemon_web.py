import pytest
import requests

from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://pokemonbattle-stage.ru/'

def test_browser():
    """
    TRP-1. Open browser
    """

    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized") # Open Browser in maximized  mode
    chrome_options.add_argument("--disable-infobars") # disabling infobars
    chrome_options.add_argument("--disable-extensions") # disabling extensions
    chrome_options.add_argument("--disable-gpu") # applicable to windows os only
    chrome_options.add_argument("--disable-dev-shm-usage") # overcome limited resourse proble
    #chrome_options.add_argument("--headless")

    Service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)