from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys

class bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base_url = 'https://open.spotify.com/'
        self.bot = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.play()


    def play(self):
        self.bot.get(self.base_url)
        time.sleep(3)
        self.bot.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[5]/button[2]').click()
        time.sleep(3)
        self.bot.find_element_by_xpath('//*[@id="login-username"]').send_keys(self.username)
        self.bot.find_element_by_xpath('//*[@id="login-password"]').send_keys(self.password)
        self.bot.find_element_by_xpath('//*[@id="login-password"]').send_keys(Keys.RETURN)
        time.sleep(3)
        self.bot.find_element_by_xpath('//*[@id="main"]/div/div[2]/nav/div[1]/ul/li[2]/a').click()
        time.sleep(3)
        self.bot.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input').click()
        self.bot.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input').send_keys('OK computer')
        self.bot.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input').send_keys(Keys.RETURN)
        time.sleep(3)
        self.bot.find_element_by_class_name('_3802c04052af0bb5d03956299250789e-scss').click()
        #self.bot.find_element_by_class_name('link-subtle _47872eede19af06725157ba21fea3516-scss d1c9699572913ee01b0280946ab1f470-scss').click()              #Bouton rechercher
        #time.sleep(7)

if __name__ == "__main__":
    BOT = bot("mdnmincraft@gmail.com","Binimo11")