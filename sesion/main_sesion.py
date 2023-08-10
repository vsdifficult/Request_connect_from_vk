
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 

from threading import Thread

from bs4 import BeautifulSoup
import requests, pyuseragents

def response(vk_com, login, password): 
    
    user_agent  = pyuseragents.random()
    
    
    headers = { 
               'User-Agent': user_agent, 
               'Content-Type': 'application/json'}
    print(f'Headers: \n{headers}') 
    
    params = {
         'login': login, 
         'password': password
    }
    
    print(f'Params:  \n{params}')
    
    __response__ = requests.get(vk_com, headers=headers, params=params) 
    
    pars_ogbj = BeautifulSoup(__response__.text, 'html.parser') 
    
    
    try: 
        with open('vk_res.html', 'w', encoding='utf-8') as file: 
            file.write(str(pars_ogbj))
            
    except ConnectionError as e: 
        return e
    
def sel(vk, login, password): 
    
    
    path_from_driver = 'C:\Users\user\Desktop\WORK 2023 IT\Parso-ingenier\VK_api_parsing\geckodriver.exe'
    driver = webdriver.Firefox(path_from_driver)
    driver.get(vk) 
    
    
    try:
        logining = driver.find_element('login') 
        logining.send_keys(login) 
        
        login_ = driver.find_element('pass') 
        login_.send_keys(password) 
        login_.send_keys(Keys.ENTER)
        
        
    except ConnectionError and TimeoutError as e:
        return e
    
    
    pass

requests_connect_t = Thread(target=response, name="Loging Requests", args=('https://vk.com', 'number', 'pass',)).start() 
selenium_connetc_t = Thread(target=sel, name='Loging Selenium', args=('https://vk.com', 'number', 'pass',)).start() 
print(f'Thread 1: {requests_connect_t}') 
print(f'Thread 2: {selenium_connetc_t}')
