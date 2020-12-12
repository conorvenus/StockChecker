import pygame
from colorama import Fore, init
from datetime import datetime
import math
import pygame
import webbrowser


productsInStock = []


def printMessage(retailer, product_name, status, stock_checking, url):
    global productsInStock
    if status == "found" and stock_checking:
        print(
            f"{Fore.LIGHTWHITE_EX}[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] {Fore.RED}[OUT OF STOCK] {Fore.LIGHTWHITE_EX}--> {Fore.LIGHTYELLOW_EX}[{retailer}] {Fore.LIGHTBLUE_EX}{product_name}")
        if (retailer, product_name) in productsInStock:
            productsInStock.remove((retailer, product_name))
    elif status == "found" and not stock_checking:
        print(
            f"{Fore.LIGHTWHITE_EX}[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] {Fore.GREEN}[IN STOCK] {Fore.LIGHTWHITE_EX}--> {Fore.LIGHTYELLOW_EX}[{retailer}] {Fore.LIGHTBLUE_EX}{product_name}")
        playInStockSound()
        if (retailer, product_name) not in productsInStock:
            webbrowser.open(url)
            productsInStock.append((retailer, product_name))
    elif status == "notfound" and stock_checking:
        print(
            f"{Fore.LIGHTWHITE_EX}[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] {Fore.GREEN}[IN STOCK] {Fore.LIGHTWHITE_EX}--> {Fore.LIGHTYELLOW_EX}[{retailer}] {Fore.LIGHTBLUE_EX}{product_name}")
        playInStockSound()
        if (retailer, product_name) not in productsInStock:
            webbrowser.open(url)
            productsInStock.append((retailer, product_name))
    else:
        print(
            f"{Fore.LIGHTWHITE_EX}[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] {Fore.RED}[OUT OF STOCK] {Fore.LIGHTWHITE_EX}--> {Fore.LIGHTYELLOW_EX}[{retailer}] {Fore.LIGHTBLUE_EX}{product_name}")
        if (retailer, product_name) in productsInStock:
            productsInStock.remove((retailer, product_name))


def printCheckingRetailer(retailer):
    retailer = "STARTED CHECKING: " + retailer.upper()
    print(f"{Fore.CYAN}{retailer}")


def printStatusCodeError(statusCode):
    print(
        f"{Fore.LIGHTWHITE_EX}[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] {Fore.RED}[⚠️  STATUS CODE {statusCode}]")


def printTimeElapsed(timeArray, totalSites):
    titleName = "FULL STOCK CHECK COMPLETED"
    print(f"\n{Fore.WHITE}{'-'*len(titleName)}")
    print(
        f"{Fore.CYAN}{titleName} {Fore.GREEN}[{totalSites} PRODUCTS CHECKED]")
    print(f"{Fore.WHITE}{'-'*len(titleName)}\n")
    print(
        f"{Fore.LIGHTWHITE_EX}[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] {Fore.GREEN}[⏱️  Time Elapsed for Full Stock Check: {math.trunc(timeArray[0])} Minutes {math.trunc(timeArray[1])} Seconds]\n")


def playInStockSound():
    pygame.init()
    pygame.mixer.Sound('success.mp3').play()
