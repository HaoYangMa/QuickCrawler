#Cloud Music Comment Spider 网易云音乐用户评论爬虫
# coding=utf-8
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import math


driver=webdriver.Chrome()
driver.set_page_load_timeout(10)
driver.get("http://music.163.com/#/song?id=409060868")  #url入口，由子函数对接过来
driver.switch_to.frame("contentFrame")
time.sleep(0.7) #设置延时0.7s，等待页面加载
soup = BeautifulSoup(driver.page_source, 'lxml')
contents = soup.find('span', class_= 'j-flag') #获取评论的总数
t= math.ceil(int(contents.get_text())/20) #获取评论的总数，除以每页20条评论，向上取整得到页数



while True:
    print(t)
    time.sleep(0.7)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    contents = soup.find_all('div', class_='cnt f-brk')
    for content in contents:
        print(content.get_text())
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#    time.sleep(0.5)
    t = t-1
    if t == 0:
        break
    driver.find_element_by_link_text('下一页').click()