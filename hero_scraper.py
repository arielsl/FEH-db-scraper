# This file will read and scrape all the individual heroes sent by the main fie
import hero
from bs4 import BeautifulSoup
import requests
import pandas as pandas

def scrape(url, img_url):
    return