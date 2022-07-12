import telebot
import time 

CHAVE_API = "TOKEN"

bot = telebot.TeleBot(CHAVE_API)

from datetime import datetime, timedelta, timezone
diferenca = timedelta(hours=0)
fuso_horario = timezone(diferenca)
today = datetime.now().astimezone(fuso_horario) # Define o fuso horário para UTC+0
f_data = today.strftime("%H:%M")
#print(f_data)

#### Data de hoje para ser usado na URL da página
mes_ext = {1: 'janeiro', 2 : 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}
date_today = today.strftime("%d/%m/%Y")
dia, mes, ano = date_today.split("/")
date = '%s de %s de %s' % (int(dia), mes_ext[int(mes)], ano)

#### Mensagem de aviso desse novo semibot ao canal da Wikipédia em Português
##bot.send_message(-1001569914422, "Olá, eu sou um novo semibot, criado pelo @Juan90264 para postar os conteúdos desse canal de um jeito rápido e fácil. Agora diariamente esse canal retornará a ter postagens referentes a Wikipédia Lusófona.")
##print("Enviado uma mensagem")

import requests
from bs4 import BeautifulSoup

url = 'https://pt.wikipedia.org/wiki/Wikipédia:Imagem_em_destaque/' + date.replace(" ", "_") #.replace("9", "8")

headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.79"}
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
placas = soup.find_all('div', class_='mw-parser-output')
print(url)
# Legenda que descreve a imagem
placa = placas[0]
marca = placa.find('p')
marca_1 = marca.get_text().strip()
messagem = marca_1

#print(messagem);

# Busca do nome do arquivo da imagem
placaDado = placas[0]
marcaDado = placaDado.find('a')
marcaDado1 = marcaDado.get('href')
messagem2 = marcaDado1
nomeArquivo = marcaDado1[6:]

#### Extrai o arquivo da imagem
foto = "https://pt.wikipedia.org/wiki/Especial:Redirecionar/file/" + nomeArquivo + "?width=1920"

f = open('C:/Users/User/Documents/FotosDoDia/' + date + '.png','wb')
response = requests.get(foto)
f.write(response.content)
f.close()
print("Foto baixada com sucesso")

#### Extrair dados sobre a foto (CÓDIGO DE TENTATIVA PARA BUSCAR METADADOS DA IMAGEM)
#url2 = 'https://pt.wikipedia.org/wiki/Wikipédia:Imagem_em_destaque/' + date.replace(" ", "_") + "#/media/" + nomeArquivo

#site = requests.get(url2, headers=headers)
#soup = BeautifulSoup(site.content, 'html.parser')
#placas = soup.find('div', class_='mw-mmv-wrapper')

#placaFoto = placas[0]
#marcaFoto = placaFoto.find_all('a')[0]
#marcaFoto1 = marcaFoto.get_text()
#messagem3 = marcaFoto1

#print(placas)

#### Busca metadados da imagem
import urllib.request, json, requests
import re

url_dados = "https://pt.wikipedia.org/w/api.php?action=query&format=json&prop=imageinfo&iiprop=extmetadata&titles=" + nomeArquivo
f = open('/FotosDoDia/' + date + '.json','wb')
response = requests.get(url_dados)
f.write(response.content)
f.close()
print("Json baixado com sucesso")

with open('/FotosDoDia/' + date + '.json', "r", encoding='utf-8') as archive:
    dados = json.load(archive)

dadosJSON = str(dados["query"]["pages"]["-1"]["imageinfo"])
dados2 = dados["query"]["pages"]["-1"]["imageinfo"][0]['extmetadata']

##### Localizar o autor da foto
author = dados2["Artist"]["value"]
author = re.sub('<[^>]+?>', '', author).strip() #Remover um elemento HTML, caso seja necessário

#####Localizar Licença da foto
if 'CC BY-SA 3.0' in dadosJSON:
    LicenseFoto = "CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/deed.pt)"
elif 'CC BY-SA 4.0' in dadosJSON:
    LicenseFoto = "CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/deed.pt)"
elif 'Public domain' in dadosJSON:
    LicenseFoto = "Domínio Público"
elif 'CC BY 4.0' in dadosJSON:
    LicenseFoto = "CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/deed.pt)"
elif 'CC BY 3.0' in dadosJSON:
    LicenseFoto = "CC BY 3.0 (https://creativecommons.org/licenses/by/3.0/deed.pt)"
elif 'FAL' in dadosJSON: #Free Art License
    LicenseFoto = "Free Art License (http://artlibre.org/lal/pt)"
else:
    LicenseFoto = dados2["LicenseShortName"]["value"] + " (" + dados2["LicenseUrl"]["value"] + ")"
#print(LicenseFoto)

##### Localizar e formatar a data original da foto
dateFoto = dados2["DateTimeOriginal"]["value"]
dateFoto = re.sub('<.+?>[^>]+?<*?>', '', dateFoto)
#dateFoto = dateFoto[10:]
diaFoto = dateFoto[8:]
mesFoto = dateFoto[5:-3]
anoFoto = dateFoto[0:-6]

if not diaFoto and not mesFoto:
    anoFoto = dateFoto[:]
    mesNomes = {1: 'janeiro', 2 : 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}
    dateFormatado = '%s' % (anoFoto)
else:
    if not diaFoto:
        mesFoto = dateFoto[5:] #2022-05
        anoFoto = dateFoto[0:-3]
        mesNomes = {1: 'janeiro', 2 : 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}
        dateFormatado = '%s de %s' % (mesNomes[int(mesFoto)], anoFoto)
    else:
        if not mesFoto:
            anoFoto = dateFoto[:]
            mesNomes = {1: 'janeiro', 2 : 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}
            dateFormatado = '%s' % (anoFoto)
        else:
            if len(dateFoto) > 10: #Checa a quantidade de caracteres para caso tenha hora na data
                diaFoto = dateFoto[8:-9]
                mesFoto = dateFoto[5:-13] #2022-09-20 21:39:30
                anoFoto = dateFoto[0:-15]
                mesNomes = {1: 'janeiro', 2 : 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}
                dateFormatado = '%s de %s de %s' % (int(dia), mesNomes[int(mesFoto)], anoFoto)
            else:
                mesNomes = {1: 'janeiro', 2 : 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}
                dateFormatado = '%s de %s de %s' % (int(dia), mesNomes[int(mesFoto)], anoFoto)

#print(author, dateFormatado)

#### Parâmetros da legenda da foto
autor = author
dataFoto = dateFormatado
#LicenseFoto = ""
#print(dataFoto)

#### Apaga o arquivo antigo
dateOntem = today - timedelta(1)
dataOntemStr = dateOntem.strftime("%d/%m/%Y")
dia2, mes2, ano2 = dataOntemStr.split("/")
dataOntem = '%s de %s de %s' % (int(dia2), mes_ext[int(mes2)], ano2)

import os
os.remove('/FotosDoDia/' + dataOntem + '.png')
os.remove('/FotosDoDia/' + dataOntem + '.json')
print("Arquivos de ontem apagados com sucesso")

#print(dataOntem)

LegendaFoto = "<b>Imagem do dia em " + date + ": </b>" + messagem + "\nSaiba mais: " + url + "\nAutor: " + autor + "\nData: " + dataFoto + "\nLicença: " + LicenseFoto

photo = open('/FotosDoDia/' + date + '.png', 'rb')
bot.send_photo(-1001569914422, photo, LegendaFoto, parse_mode="HTML")
print("Foto do dia " + date + " enviada com sucesso!")
time.sleep(15)
exit()

bot.polling()
