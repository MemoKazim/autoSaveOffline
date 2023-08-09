from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
# import io
import os
import pyautogui as pg

#DEBUGGING
driver = webdriver.Firefox()
# END OF DEBUGGING

rigth_folder = 0
with open('names.txt', 'r') as names:
    NAMES=names.readlines()
with open('urls.txt', 'r') as urls:
    URLS=urls.readlines()
for i in range(len(URLS)):
    driver.get(URLS[i][0:-1])
    sleep(1)
    pg.hotkey('ctrl', 's')
    sleep(1.5)
    if rigth_folder == 0:
        sleep(1)
        pg.write('data')
        pg.press('enter')
        rigth_folder=1
    pg.write(f"{NAMES[i][0:-1]}.html")
    sleep(0.5)
    pg.press('enter')
    while not os.path.exists(f'C:/Users/Memo/Downloads/data/{NAMES[i][0:-1]}.html'):
        sleep(1)
    sleep(2)
    print(f"{i}){URLS[i][0:-1]} - {NAMES[i][0:-1]}")

input("> CODE EXECUTED SUCCESSFULLY...\nPLEASE CHECK DOWNLOADS FOLDER AND RETRY FAILED ONES...")