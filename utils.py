import pygame
from colorama import Fore, init
from datetime import datetime
import math
import pygame
import webbrowser


def printMessage(retailer, product_name, status, stock_checking, url):
    if status == "found" and stock_checking:
        print(
            f"{Fore.LIGHTWHITE_EX}[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] {Fore.RED}[OUT OF STOCK] {Fore.LIGHTWHITE_EX}--> {Fore.LIGHTYELLOW_EX}[{retailer}] {Fore.LIGHTBLUE_EX}{product_name}")
    elif status == "found" and not stock_checking:
        print(
            f"{Fore.LIGHTWHITE_EX}[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] {Fore.GREEN}[IN STOCK] {Fore.LIGHTWHITE_EX}--> {Fore.LIGHTYELLOW_EX}[{retailer}] {Fore.LIGHTBLUE_EX}{product_name}")
        playInStockSound()
        webbrowser.open(url)
    elif status == "notfound" and stock_checking:
        print(
            f"{Fore.LIGHTWHITE_EX}[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] {Fore.GREEN}[IN STOCK] {Fore.LIGHTWHITE_EX}--> {Fore.LIGHTYELLOW_EX}[{retailer}] {Fore.LIGHTBLUE_EX}{product_name}")
        playInStockSound()
        webbrowser.open(url)
    else:
        print(
            f"{Fore.LIGHTWHITE_EX}[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] {Fore.RED}[OUT OF STOCK] {Fore.LIGHTWHITE_EX}--> {Fore.LIGHTYELLOW_EX}[{retailer}] {Fore.LIGHTBLUE_EX}{product_name}")


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
