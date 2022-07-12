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

#### Processa o evento atual proposto na Página Principal
import urllib.request, json, requests
import re
import emoji

url_dados = "https://pt.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&titles=Usuário(a)%3AEventosAtuaisBot%2Flog&rvprop=timestamp%7Ccontent%7Cids&rvslots=main&rvlimit=1"
f = open('/FotosDoDia/' + date + 'EventosAtuais.json','wb')
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
os.remove('/FotosDoDia/' + dataOntem + 'EventosAtuais.json')
print("Arquivos de ontem apagados com sucesso")

with open('/FotosDoDia/' + date + 'EventosAtuais.json', "r", encoding='utf-8') as archive:
    dados = json.load(archive)

dadosJSON = dados["query"]["pages"]["6740244"]["revisions"]
dados2 = dados["query"]["pages"]["6740244"]["revisions"][0]["slots"]["main"]["*"]

#### Prepara a mensagem contendo o evento atual na Página Principal
EventoAtual = dados2
EventoAtualTitle = re.findall("\'\'\'\[\[([^\]\|\#]*)|\[\[([^\|]*)\|\'\'\'", EventoAtual)
EventoAtualTitle = EventoAtualTitle[0][0]
##print(EventoAtualTitle)
EventoAtual = dados2#.replace("[[", "").replace("'''", "*").replace("]]", "")
EventoAtual = re.sub("\'|\[\[[^\|\]]*\||\]|\[\[", '', EventoAtual).strip()
##curiosidadeCheckUp = dados2[19:].replace('\n', '')
EventoAtualURL = "https://pt.wikipedia.org/wiki/" + EventoAtualTitle.replace(" ", "_")
mensagemEventoAtual = '<b>' + EventoAtualTitle + ': </b>' + EventoAtual + ' Esse é um evento recente ou em curso que está sendo acompanhado por nossas voluntárias e voluntários. <a href="' + EventoAtualURL + '">Veja mais detalhes no link.</a>'
##print(mensagemEventoAtual)

#### Checa se o evento atual já foi postado
ArquivoCheckUpEventoAtual = open('/FotosDoDia/ArquivoCheckUpEventoAtual.json','r')
dadosArquive = json.load(ArquivoCheckUpEventoAtual)
Arquivo = dadosArquive["EventoAtual"]
##print(Arquivo)
if Arquivo == EventoAtual:
    # Não fará nada, e alguns segundos ignorará
    print("O evento atual na Página Principal já foi postado")
else:
    #### Se ainda não foi postado, postará e deixando registrado num arquivo
    ArquivoCheckUpEventoAtual = open('/FotosDoDia/ArquivoCheckUpEventoAtual.json','w+')
    TextoCheckUpEventoAtual = '{"EventoAtual":"' + EventoAtual + '"}'
    TextoCheckUpEventoAtual = TextoCheckUpEventoAtual.strip()
    ArquivoCheckUpEventoAtual.write(TextoCheckUpEventoAtual)
    ArquivoCheckUpEventoAtual.close()
    bot.send_message(-1001569914422, mensagemEventoAtual, parse_mode="HTML")
    ######print("Enviado mensagens compartilhando as notícias do Wikinotícias")
    print("Evento atual relacionado no artigo: " + EventoAtualTitle + ", enviado com sucesso")
    ##print(mensagemCuriosidade)
