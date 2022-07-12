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

#### Processa a curiosidade atual do Sabia que? na Página Principal
import urllib.request, json, requests
import re
import emoji

url_dados = "https://pt.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&titles=Usuário(a)%3ASabiaQueBot%2Flog&rvprop=timestamp%7Ccontent%7Cids&rvslots=main&rvlimit=1"
f = open('/FotosDoDia/' + date + 'SabiaQue.json','wb')
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
os.remove('/FotosDoDia/' + dataOntem + 'SabiaQue.json')
print("Arquivos de ontem apagados com sucesso")

with open('/FotosDoDia/' + date + 'SabiaQue.json', "r", encoding='utf-8') as archive:
    dados = json.load(archive)

dadosJSON = dados["query"]["pages"]["6731563"]["revisions"]
dados2 = dados["query"]["pages"]["6731563"]["revisions"][0]["slots"]["main"]["*"]

#### Prepara a mensagem contendo a curiosidade
curiosidade = dados2[19:].replace("?", emoji.emojize(':red_question_mark:'))
curiosidadeCheckUp = dados2[19:].replace('\n', '')
mensagemCuriosidade = "<b>Você sabia que... </b>" + curiosidade

#### Checa se a curiosidade atual já foi postado
ArquivoCheckUpSabiaQue = open('/FotosDoDia/ArquivoCheckUpSabiaQue.json','r')
dadosArquive = json.load(ArquivoCheckUpSabiaQue)
Arquivo = dadosArquive["curiosidadeSabiaQue"]
##print(Arquivo)
if Arquivo == curiosidadeCheckUp:
    # Não fará nada, e alguns segundos ignorará
    print("A atual curiosidade do Wikipédia:Sabia que? já foi postado")
else:
    #### Se ainda não foi postado, postará e deixando registrado num arquivo
    ArquivoCheckUpSabiaQue = open('/FotosDoDia/ArquivoCheckUpSabiaQue.json','w+')
    TextoCheckUpSabiaQue = '{"curiosidadeSabiaQue":"' + curiosidadeCheckUp + '"}'
    TextoCheckUpSabiaQue = TextoCheckUpSabiaQue.strip()
    ArquivoCheckUpSabiaQue.write(TextoCheckUpSabiaQue)
    ArquivoCheckUpSabiaQue.close()
    bot.send_message(-1001569914422, mensagemCuriosidade, parse_mode="HTML")
    ######print("Enviado mensagens compartilhando as notícias do Wikinotícias")
    print("Curiosidade atual do Wikipédia:Sabia que? enviado com sucesso")
    ##print(mensagemCuriosidade)
