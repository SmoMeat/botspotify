from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import json

class bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base_url = 'https://open.spotify.com/'
        self.bot = webdriver.Chrome()
        self.connect()

    def connect(self):
        self.bot.get(self.base_url)
        time.sleep(3)
        try:
            element = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[5]/button[2]'))
            )
            element.click() #Click on login button

            element = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="login-username"]'))
            )
            element.send_keys(self.username) #Enter Username

            element = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="login-password"]'))
            )
            element.send_keys(self.password) #Enter Password

            element = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="login-password"]'))
            )
            element.send_keys(Keys.RETURN)

            element = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/nav/div[1]/ul/li[2]/a'))
            )
            element.click()

        except Exception as problem:
            print (problem)
            self.bot.quit()
    
    def play_artist(self, artist_name):
        try:

            element = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input'))
            )
            element.click() #Clique le bouton de recherche

            element = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input'))
            )
            element.send_keys(artist_name) #Cherche pour l'artiste

            element = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input'))
            )
            element.send_keys(Keys.RETURN)

            element = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, '_3802c04052af0bb5d03956299250789e-scss'))
            )
            element.click() #Clique sur le premier resultat d'artiste

            element = WebDriverWait(self.bot ,10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/main/div[2]/div[2]/div/div/div[2]/section/div/div[2]/div[2]/div/button[1]'))
            )
            element.click()

        except Exception as problem:
            print (problem)
            self.bot.quit()

    def play_song(self, song_name):
        element = WebDriverWait(self.bot, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input'))
        )
        element.click() #Clique sur le bouton de recherche

        element = WebDriverWait(self.bot, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input'))
        )
        element.send_keys(song_name) #Cherche pour la musique

        element = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input'))
            )
        element.send_keys(Keys.RETURN)

        element = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="searchPage"]/div/div/section[1]/div[2]/div/div/div/div[4]'))
            )
        element.click() #Start la musique resultante

class BotMaster:
    def __init__ (self):
        self.bots_list = []
        self.bots_auth = {}
        self.summon_bots()
        self.play_specific_song('lets get it on')
        #self.play_specific_artist ('Fanatic Squirrel', 1)

    def summon_bots(self):
        with open('spot-accounts.json') as bots_auth_json:
            self.bots_auth = json.load(bots_auth_json)
            for auth in self.bots_auth.items():
                self.bots_list.append(bot(auth[0], auth[1]))

    def play_specific_song (self, song_name, bot_target = None):
        if type(bot_target) is int:
            self.bots_list[bot_target].play_song(song_name)

        elif type(bot_target) is list: #can specify a list of targetable bots
            for i in bot_target:
                self.bots_list[i].play_song(song_name)

        elif bot_target is None: #if no bot is targeted, do on all bots
            count = 0
            while count < len(self.bots_list):
                self.bots_list[count].play_song(song_name)
                count += 1
    
    def play_specific_artist (self, artist_name, bot_target = None):
        if type(bot_target) is int:
            self.bots_list[bot_target].play_artist(artist_name)

        elif type(bot_target) is list: #can specify a list of targetable bots
            for i in bot_target:
                self.bots_list[i].play_artist(artist_name)

        elif bot_target is None: #if no bot is targeted, do on all bots
            count = 0
            while count < len(self.bots_list):
                self.bots_list[count].play_artist(artist_name)
                count += 1



if __name__ == "__main__":
    BotMaster = BotMaster()
