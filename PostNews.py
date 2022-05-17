###########################################################
### Teste do Bot, esse não é o arquivo para executar-lo ###
### Esse arquivo foi um teste do bot                    ###
###########################################################
import telebot
import time 

CHAVE_API = "5297947770:AAGeMzt6z8KcN2lJGPupQj98hYtroW_POCc"

bot = telebot.TeleBot(CHAVE_API)

from datetime import datetime, timedelta

today = datetime.now()   
f_data = today.strftime("%H:%M")


#### Data de hoje para ser usado na URL da página
mes_ext = {1: 'janeiro', 2 : 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}
date_today = today.strftime("%d/%m/%Y")
dia, mes, ano = date_today.split("/")
date = '%s de %s de %s' % (dia, mes_ext[int(mes)], ano)


### Comando de teste de funcionamento
@bot.message_handler(commands=["start"])
def teste(message):
        bot.send_message(-1001491434503, "Olá, me encontro funcionando corretamente!")

def verificar(message):
    if "21:36" == "21:36":
       return True
    else:
       return False


import requests
from bs4 import BeautifulSoup

url = 'https://pt.wikinews.org/wiki/Utilizador:Juan90264/Telebot' #+ date.replace(" ", "_")

headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.79"}
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
placas = soup.find_all('div', class_='mw-parser-output')

#### Localizador de páginas na categoria
ultima_pagina = soup.find('div', class_='mw-parser-output')
paginas = ultima_pagina.find('span', class_='Pages-in-category').get_text()
#pag = paginas[62:]
#pag = pag[:-8]


#### Mensagens com as notícias para compartilhar
if int(paginas) >= 1:
    placa = placas[0]
    marca = placa.find_all('a')[0]
    marca_1 = marca.get('href')
    messagem = "https://pt.wikinews.org" + marca_1.replace(" ", "_")

if int(paginas) >= 2:
    placa2 = placas[0]
    marca2 = placa.find_all('a')[1]
    marca_2 = marca2.get('href')
    messagem2 = "https://pt.wikinews.org" + marca_2.replace(" ", "_")

if int(paginas) >= 3:
    placa3 = placas[0]
    marca3 = placa.find_all('a')[2]
    marca_3 = marca3.get('href')
    messagem3 = "https://pt.wikinews.org" + marca_3.replace(" ", "_")

if int(paginas) >= 4:
    placa4 = placas[0]
    marca4 = placa.find_all('a')[3]
    marca_4 = marca4.get('href')
    messagem4 = "https://pt.wikinews.org" + marca_4.replace(" ", "_")

if int(paginas) >= 5:
    placa5 = placas[0]
    marca5 = placa.find_all('a')[4]
    marca_5 = marca5.get('href')
    messagem5 = "https://pt.wikinews.org" + marca_5.replace(" ", "_")

if int(paginas) >= 6:
    placa6 = placas[0]
    marca6 = placa.find_all('a')[5]
    marca_6 = marca6.get('href')
    messagem6 = "https://pt.wikinews.org" + marca_6.replace(" ", "_")

if int(paginas) >= 7:
    placa7 = placas[0]
    marca7 = placa.find_all('a')[6]
    marca_7 = marca7.get('href')
    messagem7 = "https://pt.wikinews.org" + marca_7.replace(" ", "_")

if int(paginas) >= 8:
    placa8 = placas[0]
    marca8 = placa.find_all('a')[7]
    marca_8 = marca8.get('href')
    messagem8 = "https://pt.wikinews.org" + marca_8.replace(" ", "_")

if int(paginas) >= 9:
    placa9 = placas[0]
    marca9 = placa.find_all('a')[8]
    marca_9 = marca9.get('href')
    messagem9 = "https://pt.wikinews.org" + marca_9.replace(" ", "_")

if int(paginas) >= 10:
    placa10 = placas[0]
    marca10 = placa.find_all('a')[9]
    marca_10 = marca10.get('href')
    messagem10 = "https://pt.wikinews.org" + marca_10.replace(" ", "_")

if int(paginas) >= 11:
    placa11 = placas[0]
    marca11 = placa.find_all('a')[10]
    marca_11 = marca11.get('href')
    messagem11 = "https://pt.wikinews.org" + marca_11.replace(" ", "_")

if int(paginas) >= 12:
    placa12 = placas[0]
    marca12 = placa.find_all('a')[11]
    marca_12 = marca12.get('href')
    messagem12 = "https://pt.wikinews.org" + marca_12.replace(" ", "_")

if int(paginas) >= 13:
    placa13 = placas[0]
    marca13 = placa.find_all('a')[12]
    marca_13 = marca13.get('href')
    messagem13 = "https://pt.wikinews.org" + marca_13.replace(" ", "_")

if int(paginas) >= 14:
    placa14 = placas[0]
    marca14 = placa.find_all('a')[13]
    marca_14 = marca14.get('href')
    messagem14 = "https://pt.wikinews.org" + marca_14.replace(" ", "_")

if int(paginas) >= 15:
    placa15 = placas[0]
    marca15 = placa.find_all('a')[14]
    marca_15 = marca15.get('href')
    messagem15 = "https://pt.wikinews.org" + marca_15.replace(" ", "_")

if int(paginas) >= 16:
    placa16 = placas[0]
    marca16 = placa.find_all('a')[15]
    marca_16 = marca16.get('href')
    messagem16 = "https://pt.wikinews.org" + marca_16.replace(" ", "_")

if int(paginas) >= 17:
    placa17 = placas[0]
    marca17 = placa.find_all('a')[16]
    marca_17 = marca17.get('href')
    messagem17 = "https://pt.wikinews.org" + marca_17.replace(" ", "_")

if int(paginas) >= 18:
    placa18 = placas[0]
    marca18 = placa.find_all('a')[17]
    marca_18 = marca18.get('href')
    messagem18 = "https://pt.wikinews.org" + marca_18.replace(" ", "_")

if int(paginas) >= 19:
    placa19 = placas[0]
    marca19 = placa.find_all('a')[18]
    marca_19 = marca19.get('href')
    messagem19 = "https://pt.wikinews.org" + marca_19.replace(" ", "_")

if int(paginas) >= 20:
    placa20 = placas[0]
    marca20 = placa.find_all('a')[19]
    marca_20 = marca20.get('href')
    messagem20 = "https://pt.wikinews.org" + marca_20.replace(" ", "_")

import emoji
MensagemConfira = emoji.emojize(':backhand_index_pointing_up:') + emoji.emojize(':backhand_index_pointing_up:') + "*Confira as notícias do dia " + date + " no Wikinotícias*" + emoji.emojize(':backhand_index_pointing_up:') + emoji.emojize(':backhand_index_pointing_up:')


@bot.message_handler(func=verificar)
def responder(message):
    #bot.reply_to(-720890200, "Oi, funcionando! https://pt.wikinews.org/?curid=78380")
    if 'messagem' in globals():
        bot.send_message(-1001491434503, messagem)
        time.sleep(2)
        
    if 'messagem2' in globals():
        bot.send_message(-1001491434503, messagem2)
        time.sleep(2)
            
    if 'messagem3' in globals():
        bot.send_message(-1001491434503, messagem3)
        time.sleep(2)
            
    if 'messagem4' in globals():
        bot.send_message(-1001491434503, messagem4)
        time.sleep(2)
                
    if 'messagem5' in globals():
        bot.send_message(-1001491434503, messagem5)
        time.sleep(2)
            
    if 'messagem6' in globals():
        bot.send_message(-1001491434503, messagem6)
        time.sleep(2)
        
    if 'messagem7' in globals():
        bot.send_message(-1001491434503, messagem7)
        time.sleep(2)
            
    if 'messagem8' in globals():
        bot.send_message(-1001491434503, messagem8)
        time.sleep(2)
            
    if 'messagem9' in globals():
        bot.send_message(-1001491434503, messagem9)
        time.sleep(2)
        
    if 'messagem10' in globals():
        bot.send_message(-1001491434503, messagem10)
        time.sleep(2)
            
    if 'messagem11' in globals():
        bot.send_message(-1001491434503, messagem11)
        time.sleep(2)
            
    if 'messagem12' in globals():
        bot.send_message(-1001491434503, messagem12)
        time.sleep(2)
            
    if 'messagem13' in globals():
        bot.send_message(-1001491434503, messagem13)
        time.sleep(2)
        
    if 'messagem14' in globals():
        bot.send_message(-1001491434503, messagem14)
        time.sleep(2)
            
    if 'messagem15' in globals():
        bot.send_message(-1001491434503, messagem15)
        time.sleep(2)
            
    if 'messagem16' in globals():
        bot.send_message(-1001491434503, messagem16)
        time.sleep(2)
            
    if 'messagem17' in globals():
        bot.send_message(-1001491434503, messagem17) 
        time.sleep(2)
        
    if 'messagem18' in globals():
        bot.send_message(-1001491434503, messagem18)
        time.sleep(2)
        
    if 'messagem19' in globals():
        bot.send_message(-1001491434503, messagem19)
        time.sleep(2)
            
    if 'messagem20' in globals():
        bot.send_message(-1001491434503, messagem20)
        time.sleep(2)
        
    bot.send_message(-1001491434503, MensagemConfira, parse_mode= "Markdown")
    time.sleep(5)
                                   #"Oi, estou funcionando! Em breve compartilharei notícias")

bot.polling()
