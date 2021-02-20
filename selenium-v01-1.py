from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

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
        try:
            element = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[5]/button[2]'))
            )
            element.click()

            element = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="login-username"]'))
            )
            element.send_keys(self.username)

            element = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="login-password"]'))
            )
            element.send_keys(self.password)

            element = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="login-password"]'))
            )
            element.send_keys(Keys.RETURN)

            element = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/nav/div[1]/ul/li[2]/a'))
            )
            element.click()

            element = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input'))
            )
            element.click()

            element = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input'))
            )
            element.send_keys('Fanatic Squirrel') 

            element = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input'))
            )
            element.send_keys(Keys.RETURN)

            element = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, '_3802c04052af0bb5d03956299250789e-scss'))
            )
            element.click()  
        except:
            self.bot.quit()
        #self.bot.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[5]/button[2]').click()                                                         #Bouton Login
        #time.sleep(3)
        #self.bot.find_element_by_xpath('//*[@id="login-username"]').send_keys(self.username)
        #self.bot.find_element_by_xpath('//*[@id="login-password"]').send_keys(self.password)                                                                        #Rentrer les infos du compte
        #self.bot.find_element_by_xpath('//*[@id="login-password"]').send_keys(Keys.RETURN)
        #time.sleep(3)
        #self.bot.find_element_by_xpath('//*[@id="main"]/div/div[2]/nav/div[1]/ul/li[2]/a').click()                                                                  #Bouton rechercher
        #time.sleep(3)
        #self.bot.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input').click()
        #self.bot.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input').send_keys('Fanatic Squirrel')                               #Recherche auteur/album
        #self.bot.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input').send_keys(Keys.RETURN)
        #time.sleep(3)
        #self.bot.find_element_by_class_name('_3802c04052af0bb5d03956299250789e-scss').click()                                                                       #Selectionne normalement le premier album



if __name__ == "__main__":
    BOT = bot("mdnmincraft@gmail.com","Binimo11")
