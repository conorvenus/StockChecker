import random
import time
from parsers import getStores, useRequest, useSelenium
from utils import printTimeElapsed, playInStockSound, printCheckingRetailer
from threading import Thread


def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    return [mins, sec]


def check(country=None):
    while True:
        threads = []
        for store in getStores(country):
            if store["method"] == "request":
                threads.append(
                    (store, Thread(target=lambda: useRequest(store))))
            elif store["method"] == "selenium":
                threads.append(
                    (store, Thread(target=lambda: useSelenium(store))))
        for (store, thread) in threads:
            thread.start()
            time.sleep(0.2)
            printCheckingRetailer(store["name"])
        print()
        start_time = time.time()
        for (store, thread) in threads:
            thread.join()
        end_time = time.time()
        printTimeElapsed(time_convert(end_time - start_time))
