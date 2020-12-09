import json
from bs4 import BeautifulSoup
import requests
from utils import printMessage, printStatusCodeError, playInStockSound
import lxml
import cchardet
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import random


def getStores(country):
    with open("stores.json") as stores:
        if country != None:
            return [store for store in json.loads(stores.read()) if store["country"] == country]
        return json.loads(stores.read())


def generateBrowserWebdriver():
    options = Options()
    options.add_argument('--log-level=3')
    options.add_argument('headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    dc = DesiredCapabilities.CHROME
    dc['loggingPrefs'] = {'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}
    return webdriver.Chrome(chrome_options=options, desired_capabilities=dc)


def useRequest(store):
    gpuRequest = requests.get(store["url"])
    if gpuRequest.status_code == 200:
        parser = BeautifulSoup(gpuRequest.content, "lxml")
        webscraping = store["webscraping"]
        for product in parser.find_all(webscraping["product"]["type"], {webscraping["product"]["data_type"]: webscraping["product"][webscraping["product"]["data_type"]]}):
            productTitle = product.find(webscraping["title"]["type"], {
                                        webscraping["title"]["data_type"]: webscraping["title"][webscraping["title"]["data_type"]]}).get_text().strip()
            productUrl = product.find(webscraping["url"]["type"], {
                webscraping["url"]["data_type"]: webscraping["url"][webscraping["url"]["data_type"]]})["href"]
            if webscraping["url"]["append_base_url"]:
                productUrl = "https://" + \
                    store["url"].split("/")[2] + productUrl
            if store["card_name"] in productTitle.lower():
                productRequest = requests.get(productUrl)
                time.sleep(random.randint(0, 2))
                productParser = BeautifulSoup(productRequest.content, "lxml")
                if productParser.find(webscraping["stock_identifier"]["type"], {webscraping["stock_identifier"]["data_type"]: webscraping["stock_identifier"][webscraping["stock_identifier"]["data_type"]]}):
                    printMessage(store["name"].upper(), productTitle, "found",
                                 webscraping["stock_identifier"]["outofstock"], productUrl)
                else:
                    printMessage(store["name"].upper(), productTitle, "notfound",
                                 webscraping["stock_identifier"]["outofstock"], productUrl)
    else:
        printStatusCodeError(gpuRequest.status_code)


def useSelenium(store):
    chrome = generateBrowserWebdriver()
    statusCodeError = True
    try:
        chrome.get(store["url"])
        gpuRequestContent = chrome.execute_script(
            "return document.body.innerHTML;")
        statusCodeError = False
        parser = BeautifulSoup(gpuRequestContent, "lxml")
        webscraping = store["webscraping"]
        for product in parser.find_all(webscraping["product"]["type"], {webscraping["product"]["data_type"]: webscraping["product"][webscraping["product"]["data_type"]]}):
            productTitle = product.find(webscraping["title"]["type"], {
                                        webscraping["title"]["data_type"]: webscraping["title"][webscraping["title"]["data_type"]]}).get_text().strip()
            productUrl = product.find(webscraping["url"]["type"], {
                webscraping["url"]["data_type"]: webscraping["url"][webscraping["url"]["data_type"]]})["href"]
            if webscraping["url"]["append_base_url"]:
                productUrl = "https://" + \
                    store["url"].split("/")[2] + productUrl
            if store["card_name"] in productTitle.lower():
                productRequest = requests.get(productUrl)
                time.sleep(random.randint(0, 2))
                productParser = BeautifulSoup(productRequest.content, "lxml")
                if productParser.find(webscraping["stock_identifier"]["type"], {webscraping["stock_identifier"]["data_type"]: webscraping["stock_identifier"][webscraping["stock_identifier"]["data_type"]]}):
                    printMessage(store["name"].upper(), productTitle, "found",
                                 webscraping["stock_identifier"]["outofstock"], productUrl)
                else:
                    printMessage(store["name"].upper(), productTitle, "notfound",
                                 webscraping["stock_identifier"]["outofstock"], productUrl)
    except:
        if statusCodeError:
            printStatusCodeError("UNKNOWN")
