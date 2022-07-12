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

#### Processa o artigo em destaque atual na Página Principal
import urllib.request, json, requests
import re

url_dados = "https://pt.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&titles=Usuário(a)%3AAlbeROBOT%2FEAD&rvprop=timestamp%7Ccontent%7Cids&rvslots=main&rvlimit=1"
f = open('/FotosDoDia/' + date + 'ArtigoEAD.json','wb')
response = requests.get(url_dados)
f.write(response.content)
f.close()
print("Json baixado com sucesso")

#### Apaga o arquivo antigo
dateOntem = today - timedelta(1)
dataOntemStr = dateOntem.strftime("%d/%m/%Y")
dia2, mes2, ano2 = dataOntemStr.split("/")
dataOntem = '%s de %s de %s' % (int(dia2), mes_ext[int(mes2)], ano2)

import os
os.remove('/FotosDoDia/' + dataOntem + 'ArtigoEAD.json')
print("Arquivos de ontem apagados com sucesso")

with open('/FotosDoDia/' + date + 'ArtigoEAD.json', "r", encoding='utf-8') as archive:
    dados = json.load(archive)

dadosJSON = dados["query"]["pages"]["6375156"]["revisions"][0]
dados2 = dados["query"]["pages"]["6375156"]["revisions"][0]["slots"]["main"]["*"]

#### Prepara a mensagem contendo o artigo em destaque
import emoji
urlArtigoEAD = "https://pt.wikipedia.org/wiki/" + dados2.replace(" ", "_")
artigoEAD = '<a href="' + urlArtigoEAD + '"><b>' + dados2 + "</b></a>"
mensagemEAD = emoji.emojize(':star:') + " " + artigoEAD + " é um artigo de destaque na Wikipédia! Isso significa que foi identificado como um dos melhores artigos produzidos pela comunidade da Wikipédia. O que achou? Ainda tem como melhorar?"
artigoEAD2 = re.sub('<[^>]+?>', '', artigoEAD).strip()

#### Checa se o artigo em destaque atual já foi postado
ArquivoCheckUpEAD = open('/FotosDoDia/ArquivoCheckUpEAD.json','r')
dadosArquive = json.load(ArquivoCheckUpEAD)
Arquivo = dadosArquive["artigoEAD"]
##print(Arquivo)
if Arquivo == artigoEAD2:
    # Não fará nada, e alguns segundos ignorará
    print("O atual artigo em destaque já foi postado")
else:
    #### Se ainda não foi postado, postará e deixando registrado num arquivo
    ArquivoCheckUpEAD = open('/FotosDoDia/ArquivoCheckUpEAD.json','w+')
    TextoCheckUpEAD = '{"artigoEAD":"' + artigoEAD2 + '"}'
    ArquivoCheckUpEAD.write(TextoCheckUpEAD)
    ArquivoCheckUpEAD.close()
    print("Arquivo de CheckUp de atualizações foi atualizado com sucesso")
    bot.send_message(-1001569914422, mensagemEAD, parse_mode="HTML")
    ######print("Enviado mensagens compartilhando as notícias do Wikinotícias")
    print("Artigo em destaque: " + artigoEAD2 + ", enviado com sucesso")
    time.sleep(5)
