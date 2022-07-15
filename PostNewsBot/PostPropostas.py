import telebot
import time 

CHAVE_API = "TOKEN"

bot = telebot.TeleBot(CHAVE_API)

import urllib.request, json, requests

from datetime import datetime, timedelta

today = datetime.now()   
f_data = today.strftime("%H:%M")

dir(json)

#### Data de hoje para ser usado na URL da página
mes_ext = {1: 'janeiro', 2 : 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}
date_today = today.strftime("%d/%m/%Y")
dia, mes, ano = date_today.split("/")
date = '%s de %s de %s' % (dia, mes_ext[int(mes)], ano)

url_dados_proposta = "https://pt.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&titles=Wikipédia%3AEsplanada%2Fpropostas&rvprop=ids%7Ctimestamp%7Cuser%7Ccomment%7Ccontent%7Ccontentmodel&rvslots=main&rvlimit=8&rvexcludeuser=User%3AAleth%20Bot"
url_dados_geral = "https://pt.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&titles=Wikipédia%3AEsplanada%2Fgeral&rvprop=ids%7Ctimestamp%7Cuser%7Ccomment%7Ccontent%7Ccontentmodel&rvslots=main&rvlimit=8&rvexcludeuser=User%3AAleth%20Bot"
f = open('/FotosDoDia/PostPropostas.json','wb')
response = requests.get(url_dados_proposta)
f.write(response.content)
f.close()
print("Json baixado com sucesso")

with open('/FotosDoDia/PostPropostas.json', "r", encoding='utf-8') as archive:
    dados = json.load(archive)

## url_dados_geral
f = open('/FotosDoDia/PostPropostas-geral.json','wb')
response = requests.get(url_dados_geral)
f.write(response.content)
f.close()
print("Json baixado com sucesso")

with open('/FotosDoDia/PostPropostas-geral.json', "r", encoding='utf-8') as archive:
    dados2 = json.load(archive)


# para cada item do arquivo json
#for i in dados:

    # imprimindo nome e idade formatados
## Esplanada/Propostas 
dadosProposta = dados["query"]["pages"]["61666"]["revisions"][0]["comment"] ## Altere [0] para qualquer número para trocar de comentário
dadosProposta1 = dados["query"]["pages"]["61666"]["revisions"][1]["comment"] ## Altere [0] para qualquer número para trocar de comentário
dadosProposta2 = dados["query"]["pages"]["61666"]["revisions"][2]["comment"] ## Altere [0] para qualquer número para trocar de comentário
dadosProposta3 = dados["query"]["pages"]["61666"]["revisions"][3]["comment"] ## Altere [0] para qualquer número para trocar de comentário
dadosProposta4 = dados["query"]["pages"]["61666"]["revisions"][4]["comment"] ## Altere [0] para qualquer número para trocar de comentário
dadosProposta5 = dados["query"]["pages"]["61666"]["revisions"][5]["comment"] ## Altere [0] para qualquer número para trocar de comentário
dadosProposta6 = dados["query"]["pages"]["61666"]["revisions"][6]["comment"] ## Altere [0] para qualquer número para trocar de comentário
dadosProposta7 = dados["query"]["pages"]["61666"]["revisions"][7]["comment"] ## Altere [0] para qualquer número para trocar de comentário

## Esplanada/Geral
dadosPropostaGeral = dados2["query"]["pages"]["62633"]["revisions"][0]["comment"] ## Altere [0] para qualquer número para trocar de comentário
dadosPropostaGeral1 = dados2["query"]["pages"]["62633"]["revisions"][1]["comment"] ## Altere [0] para qualquer número para trocar de comentário
dadosPropostaGeral2 = dados2["query"]["pages"]["62633"]["revisions"][2]["comment"] ## Altere [0] para qualquer número para trocar de comentário
dadosPropostaGeral3 = dados2["query"]["pages"]["62633"]["revisions"][3]["comment"] ## Altere [0] para qualquer número para trocar de comentário
dadosPropostaGeral4 = dados2["query"]["pages"]["62633"]["revisions"][4]["comment"] ## Altere [0] para qualquer número para trocar de comentário
dadosPropostaGeral5 = dados2["query"]["pages"]["62633"]["revisions"][5]["comment"] ## Altere [0] para qualquer número para trocar de comentário
dadosPropostaGeral6 = dados2["query"]["pages"]["62633"]["revisions"][6]["comment"] ## Altere [0] para qualquer número para trocar de comentário
dadosPropostaGeral7 = dados2["query"]["pages"]["62633"]["revisions"][7]["comment"] ## Altere [0] para qualquer número para trocar de comentário

### Arquivo de CheckUp
ArquivoCheckUpPropostas = open('/FotosDoDia/ArquivoCheckUpPropostas.json','r')
dadosArquive = ArquivoCheckUpPropostas.read()

import re
#### Propostas para serem postadas
## Esplanada/Propostas
print("Esplanada/Propostas:")
MensagemCheckUpPropostas = "'', "
if "novo tópico" in dadosProposta:
    ##print("Tem 'novo tópico'")
    ##print("Esplanada/Propostas:")
    Proposta = re.findall("\(\[\[([^\]\|\#]*)|\[\[([^\|]*)\|\)", dadosProposta)
    Proposta = Proposta[0][0]
    Proposta = Proposta[23:]
    if Proposta in dadosArquive:
        ## Não faz nada, e ignora
        print("Proposta já foi postada")
    else:
        MensagemCheckUpPropostas = "'" + Proposta + "', "
        propostaPublica = print("OK!") ## Variável confirmando que pode ser publicada
        print(Proposta)
else:
    pass

if "novo tópico" in dadosProposta1:
    ##print("Tem 'novo tópico'")
    Proposta1 = re.findall("\(\[\[([^\]\|\#]*)|\[\[([^\|]*)\|\)", dadosProposta1)
    Proposta1 = Proposta1[0][0]
    Proposta1 = Proposta1[23:]
    if Proposta1 in dadosArquive:
        ## Não faz nada, e ignora
        print("Proposta já foi postada")
    else:
        MensagemCheckUpPropostas += "'" + Proposta1 + "', "
        propostaPublica1 = print("OK!") ## Variável confirmando que pode ser publicada
        print(Proposta1)
else:
    pass

if "novo tópico" in dadosProposta2:
    ##print("Tem 'novo tópico'")
    Proposta2 = re.findall("\(\[\[([^\]\|\#]*)|\[\[([^\|]*)\|\)", dadosProposta2)
    Proposta2 = Proposta2[0][0]
    Proposta2 = Proposta2[23:]
    if Proposta2 in dadosArquive:
        ## Não faz nada, e ignora
        print("Proposta já foi postada")
    else:
        MensagemCheckUpPropostas += "'" + Proposta2 + "', "
        propostaPublica2 = print("OK!") ## Variável confirmando que pode ser publicada
        print(Proposta2)
else:
    pass

if "novo tópico" in dadosProposta3:
    ##print("Tem 'novo tópico'")
    Proposta3 = re.findall("\(\[\[([^\]\|\#]*)|\[\[([^\|]*)\|\)", dadosProposta3)
    Proposta3 = Proposta3[0][0]
    Proposta3 = Proposta3[23:]
    if Proposta3 in dadosArquive:
        ## Não faz nada, e ignora
        print("Proposta já foi postada")
    else:
        MensagemCheckUpPropostas += "'" + Proposta3 + "', "
        propostaPublica3 = print("OK!") ## Variável confirmando que pode ser publicada
        print(Proposta3)
else:
    pass

if "novo tópico" in dadosProposta4:
    ##print("Tem 'novo tópico'")
    Proposta4 = re.findall("\(\[\[([^\]\|\#]*)|\[\[([^\|]*)\|\)", dadosProposta4)
    Proposta4 = Proposta4[0][0]
    Proposta4 = Proposta4[23:]
    if Proposta4 in dadosArquive:
        ## Não faz nada, e ignora
        print("Proposta já foi postada")
    else:
        MensagemCheckUpPropostas += "'" + Proposta4 + "', "
        propostaPublica4 = print("OK!") ## Variável confirmando que pode ser publicada
        print(Proposta4)
else:
    pass

if "novo tópico" in dadosProposta5:
    ##print("Tem 'novo tópico'")
    Proposta5 = re.findall("\(\[\[([^\]\|\#]*)|\[\[([^\|]*)\|\)", dadosProposta5)
    Proposta5 = Proposta5[0][0]
    Proposta5 = Proposta5[23:]
    if Proposta5 in dadosArquive:
        ## Não faz nada, e ignora
        print("Proposta já foi postada")
    else:
        MensagemCheckUpPropostas += "'" + Proposta5 + "', "
        propostaPublica5 = print("OK!") ## Variável confirmando que pode ser publicada
        print(Proposta5)
else:
    pass

#if "novo tópico" in dadosProposta6:
#    print("Tem 'novo tópico'")
#    Proposta6 = re.findall("\(\[\[([^\]\|\#]*)|\[\[([^\|]*)\|\)", dadosProposta6)
#    Proposta6 = Proposta6[0][0]
#    Proposta6 = Proposta6[23:]
#    print(Proposta6)
#else:
#    pass
#
#if "novo tópico" in dadosProposta7:
#    print("Tem 'novo tópico'")
#    Proposta7 = re.findall("\(\[\[([^\]\|\#]*)|\[\[([^\|]*)\|\)", dadosProposta7)
#    Proposta7 = Proposta7[0][0]
#    Proposta7 = Proposta7[23:]
#    print(Proposta7)
#else:
#    pass

## Esplanada/Geral
print("Esplanada/geral:")
if "novo tópico" in dadosPropostaGeral:
    ##print("Tem 'novo tópico'")
    PropostaGeral = re.findall("\(\[\[([^\]\|\#]*)|\[\[([^\|]*)\|\)", dadosPropostaGeral)
    PropostaGeral = PropostaGeral[0][0]
    PropostaGeral = PropostaGeral[19:]
    if PropostaGeral in dadosArquive:
        ## Não faz nada, e ignora
        print("Proposta já foi postada")
    else:
        MensagemCheckUpPropostas += "'" + PropostaGeral + "', "
        propostaPublicaGeral = print("OK!") ## Variável confirmando que pode ser publicada
        print(PropostaGeral)
else:
    pass

if "novo tópico" in dadosPropostaGeral1:
    ##print("Tem 'novo tópico'")
    PropostaGeral1 = re.findall("\(\[\[([^\]\|\#]*)|\[\[([^\|]*)\|\)", dadosPropostaGeral1)
    ##print(PropostaGeral1)
    PropostaGeral1 = PropostaGeral1[0][0]
    PropostaGeral1 = PropostaGeral1[19:]
    if PropostaGeral1 in dadosArquive:
        ## Não faz nada, e ignora
        print("Proposta já foi postada")
    else:
        MensagemCheckUpPropostas += "'" + PropostaGeral1 + "', "
        propostaPublicaGeral1 = print("OK!") ## Variável confirmando que pode ser publicada
        print(PropostaGeral1)
else:
    pass

if "novo tópico" in dadosPropostaGeral2:
    ##print("Tem 'novo tópico'")
    PropostaGeral2 = re.findall("\(\[\[([^\]\|\#]*)|\[\[([^\|]*)\|\)", dadosPropostaGeral2)
    PropostaGeral2 = PropostaGeral2[0][0]
    PropostaGeral2 = PropostaGeral2[19:]
    if PropostaGeral2 in dadosArquive:
        ## Não faz nada, e ignora
        print("Proposta já foi postada")
    else:
        MensagemCheckUpPropostas += "'" + PropostaGeral2 + "', "
        propostaPublicaGeral2 = print("OK!") ## Variável confirmando que pode ser publicada
        print(PropostaGeral2)
else:
    pass

if "novo tópico" in dadosPropostaGeral3:
    ##print("Tem 'novo tópico'")
    PropostaGeral3 = re.findall("\(\[\[([^\]\|\#]*)|\[\[([^\|]*)\|\)", dadosPropostaGeral3)
    PropostaGeral3 = PropostaGeral3[0][0]
    PropostaGeral3 = PropostaGeral3[19:]
    if PropostaGeral3 in dadosArquive:
        ## Não faz nada, e ignora
        print("Proposta já foi postada")
    else:
        MensagemCheckUpPropostas += "'" + PropostaGeral3 + "', "
        propostaPublicaGeral3 = print("OK!") ## Variável confirmando que pode ser publicada
        print(PropostaGeral3)
else:
    pass

if "novo tópico" in dadosPropostaGeral4:
    ##print("Tem 'novo tópico'")
    PropostaGeral4 = re.findall("\(\[\[([^\]\|\#]*)|\[\[([^\|]*)\|\)", dadosPropostaGeral4)
    PropostaGeral4 = PropostaGeral4[0][0]
    PropostaGeral4 = PropostaGeral4[19:]
    if PropostaGeral4 in dadosArquive:
        ## Não faz nada, e ignora
        print("Proposta já foi postada")
    else:
        MensagemCheckUpPropostas += "'" + PropostaGeral4 + "', "
        propostaPublicaGeral4 = print("OK!") ## Variável confirmando que pode ser publicada
        print(PropostaGeral4)
else:
    pass

if "novo tópico" in dadosPropostaGeral5:
    ##print("Tem 'novo tópico'")
    PropostaGeral5 = re.findall("\(\[\[([^\]\|\#]*)|\[\[([^\|]*)\|\)", dadosPropostaGeral5)
    PropostaGeral5 = PropostaGeral5[0][0]
    PropostaGeral5 = PropostaGeral5[19:]
    if PropostaGeral5 in dadosArquive:
        ## Não faz nada, e ignora
        print("Proposta já foi postada")
    else:
        MensagemCheckUpPropostas += "'" + PropostaGeral5 + "', "
        propostaPublicaGeral5 = print("OK!") ## Variável confirmando que pode ser publicada
        print(PropostaGeral5)
else:
    pass

if MensagemCheckUpPropostas == "'', ":
    print("As propostas mais recentes já foram postadas")
    time.sleep(15)
    exit()

ArquivoCheckUpPropostas = open('C:/Users/User/Documents/FotosDoDia/ArquivoCheckUpPropostas.json','a+')
TextoCheckUpPropostas = "[(" + MensagemCheckUpPropostas + " '')]"
TextoCheckUpPropostas = TextoCheckUpPropostas.strip()
ArquivoCheckUpPropostas.write(TextoCheckUpPropostas)
ArquivoCheckUpPropostas.close()

#if "novo tópico" in dadosPropostaGeral6:
#    print("Tem 'novo tópico'")
#    PropostaGeral6 = re.findall("\(\[\[([^\]\|\#]*)|\[\[([^\|]*)\|\)", dadosPropostaGeral6)
#    PropostaGeral6 = PropostaGeral6[0][0]
#    PropostaGeral6 = PropostaGeral6[19:]
#    print(PropostaGeral6)
#else:
#    pass
#
#if "novo tópico" in dadosPropostaGeral7:
#    print("Tem 'novo tópico'")
#    PropostaGeral7 = re.findall("\(\[\[([^\]\|\#]*)|\[\[([^\|]*)\|\)", dadosPropostaGeral7)
#    PropostaGeral7 = PropostaGeral7[0][0]
#    PropostaGeral7 = PropostaGeral7[19:]
#    print(PropostaGeral7)
#else:
#    pass


#### Check Up de existência de variáveis (para extrair o nome da proposta)
mensagemProposta = "<b>Esses são as propostas abertas:</b>"

import emoji
## Esplanada/Propostas
if "propostaPublica" in globals():
    ##print("Funcionando!")
    linkProposta = "https://pt.wikipedia.org/wiki/Wikipédia:Esplanada/propostas/" + Proposta.replace(" ", "_")
    mensagemProposta += '\n' + emoji.emojize(':backhand_index_pointing_right:') + emoji.emojize(':backhand_index_pointing_right:') + ' <a href="' + linkProposta + '">[[' + Proposta + ']] ' + emoji.emojize(':backhand_index_pointing_left:') + emoji.emojize(':backhand_index_pointing_left:') + '</a>'
    print(mensagemProposta)
    
if "propostaPublica1" in locals():
    ##print("Funcionando!")
    linkProposta1 = "https://pt.wikipedia.org/wiki/Wikipédia:Esplanada/propostas/" + Proposta1.replace(" ", "_")
    mensagemProposta += '\n' + emoji.emojize(':backhand_index_pointing_right:') + emoji.emojize(':backhand_index_pointing_right:') + ' <a href="' + linkProposta1 + '">[[' + Proposta1 + ']] ' + emoji.emojize(':backhand_index_pointing_left:') + emoji.emojize(':backhand_index_pointing_left:') + '</a>'
    print(mensagemProposta)

if "propostaPublica2" in globals():
    ##print("Funcionando!")
    linkProposta2 = "https://pt.wikipedia.org/wiki/Wikipédia:Esplanada/propostas/" + Proposta2.replace(" ", "_")
    mensagemProposta += '\n' + emoji.emojize(':backhand_index_pointing_right:') + emoji.emojize(':backhand_index_pointing_right:') + ' <a href="' + linkProposta2 + '">[[' + Proposta2 + ']] ' + emoji.emojize(':backhand_index_pointing_left:') + emoji.emojize(':backhand_index_pointing_left:') + '</a>'
    print(mensagemProposta)

if "propostaPublica3" in globals():
    ##print("Funcionando!")
    linkProposta3 = "https://pt.wikipedia.org/wiki/Wikipédia:Esplanada/propostas/" + Proposta3.replace(" ", "_")
    mensagemProposta += '\n' + emoji.emojize(':backhand_index_pointing_right:') + emoji.emojize(':backhand_index_pointing_right:') + ' <a href="' + linkProposta3 + '">[[' + Proposta3 + ']] ' + emoji.emojize(':backhand_index_pointing_left:') + emoji.emojize(':backhand_index_pointing_left:') + '</a>'
    print(mensagemProposta)

if "propostaPublica4" in globals():
    ##print("Funcionando!")
    linkProposta4 = "https://pt.wikipedia.org/wiki/Wikipédia:Esplanada/propostas/" + Proposta4.replace(" ", "_")
    mensagemProposta += '\n' + emoji.emojize(':backhand_index_pointing_right:') + emoji.emojize(':backhand_index_pointing_right:') + ' <a href="' + linkProposta4 + '">[[' + Proposta4 + ']] ' + emoji.emojize(':backhand_index_pointing_left:') + emoji.emojize(':backhand_index_pointing_left:') + '</a>'
    print(mensagemProposta)

if "propostaPublica5" in globals():
    ##print("Funcionando!")
    linkProposta5 = "https://pt.wikipedia.org/wiki/Wikipédia:Esplanada/propostas/" + Proposta5.replace(" ", "_")
    mensagemProposta += '\n' + emoji.emojize(':backhand_index_pointing_right:') + emoji.emojize(':backhand_index_pointing_right:') + ' <a href="' + linkProposta5 + '">[[' + Proposta5 + ']] ' + emoji.emojize(':backhand_index_pointing_left:') + emoji.emojize(':backhand_index_pointing_left:') + '</a>'
    print(mensagemProposta)

## Esplanada/geral
if "propostaPublicaGeral" in globals():
    ##print("Funcionando!")
    linkPropostaGeral = "https://pt.wikipedia.org/wiki/Wikipédia:Esplanada/geral/" + PropostaGeral.replace(" ", "_")
    mensagemProposta += '\n' + emoji.emojize(':backhand_index_pointing_right:') + emoji.emojize(':backhand_index_pointing_right:') + ' <a href="' + linkPropostaGeral + '">[[' + PropostaGeral + ']] ' + emoji.emojize(':backhand_index_pointing_left:') + emoji.emojize(':backhand_index_pointing_left:') + '</a>'
    print(mensagemProposta)
    
if "propostaPublicaGeral1" in globals():
    ##print("Funcionando!")
    linkPropostaGeral1 = "https://pt.wikipedia.org/wiki/Wikipédia:Esplanada/geral/" + PropostaGeral1.replace(" ", "_")
    mensagemProposta += '\n' + emoji.emojize(':backhand_index_pointing_right:') + emoji.emojize(':backhand_index_pointing_right:') + ' <a href="' + linkPropostaGeral1 + '">[[' + PropostaGeral1 + ']] ' + emoji.emojize(':backhand_index_pointing_left:') + emoji.emojize(':backhand_index_pointing_left:') + '</a>'
    print(mensagemProposta)

if "propostaPublicaGeral2" in globals():
    ##print("Funcionando!")
    linkPropostaGeral2 = "https://pt.wikipedia.org/wiki/Wikipédia:Esplanada/geral/" + PropostaGeral2.replace(" ", "_")
    mensagemProposta += '\n' + emoji.emojize(':backhand_index_pointing_right:') + emoji.emojize(':backhand_index_pointing_right:') + ' <a href="' + linkPropostaGeral2 + '">[[' + PropostaGeral2 + ']] ' + emoji.emojize(':backhand_index_pointing_left:') + emoji.emojize(':backhand_index_pointing_left:') + '</a>'
    print(mensagemProposta)

if "propostaPublicaGeral3" in globals():
    ##print("Funcionando!")
    linkPropostaGeral3 = "https://pt.wikipedia.org/wiki/Wikipédia:Esplanada/geral/" + PropostaGeral3.replace(" ", "_")
    mensagemProposta += '\n' + emoji.emojize(':backhand_index_pointing_right:') + emoji.emojize(':backhand_index_pointing_right:') + ' <a href="' + linkPropostaGeral3 + '">[[' + PropostaGeral3 + ']] ' + emoji.emojize(':backhand_index_pointing_left:') + emoji.emojize(':backhand_index_pointing_left:') + '</a>'
    print(mensagemProposta)

if "propostaPublicaGeral4" in globals():
    ##print("Funcionando!")
    linkPropostaGeral4 = "https://pt.wikipedia.org/wiki/Wikipédia:Esplanada/geral/" + PropostaGeral4.replace(" ", "_")
    mensagemProposta += '\n' + emoji.emojize(':backhand_index_pointing_right:') + emoji.emojize(':backhand_index_pointing_right:') + ' <a href="' + linkPropostaGeral4 + '">[[' + PropostaGeral4 + ']] ' + emoji.emojize(':backhand_index_pointing_left:') + emoji.emojize(':backhand_index_pointing_left:') + '</a>'
    print(mensagemProposta)

if "propostaPublicaGeral5" in globals():
    ##print("Funcionando!")
    linkPropostaGeral5 = "https://pt.wikipedia.org/wiki/Wikipédia:Esplanada/geral/" + PropostaGeral5.replace(" ", "_")
    mensagemProposta += '\n' + emoji.emojize(':backhand_index_pointing_right:') + emoji.emojize(':backhand_index_pointing_right:') + ' <a href="' + linkPropostaGeral5 + '">[[' + PropostaGeral5 + ']] ' + emoji.emojize(':backhand_index_pointing_left:') + emoji.emojize(':backhand_index_pointing_left:') + '</a>'
    print(mensagemProposta)

print(dadosProposta)
##dadosJSON = str(dados["query"]["pages"]["-1"]["imageinfo"])

#Teste
##dados2 = dados["query"]["pages"]["-1"]["imageinfo"][0]['extmetadata']
##author = dados2["Artist"]["value"]

##if 'CC BY-SA 3.0' in dadosJSON:
##    print("Palavra encontrada!")
##else:
##    print("Palavra não encontrada!")
#Teste
    #####Localizar Licença da foto
##if 'CC BY-SA 3.0' in dadosJSON:
##    LicenseFoto = "CC BY-SA 3.0"
##elif 'CC BY-SA 4.0' in dadosJSON:
##    LicenseFoto = "CC BY-SA 4.0"
##elif 'Public domain' in dadosJSON:
##    LicenseFoto = "Domínio Público"
##elif 'CC BY 4.0' in dadosJSON:
##    LicenseFoto = "CC BY 4.0"
##elif 'CC BY 3.0' in dadosJSON:
##    LicenseFoto = "CC BY 3.0"
##elif 'FAL' in dadosJSON: #Free Art License
##    LicenseFoto = "Free Art License"
##else:
##    LicenseFoto = dados2["LicenseShortName"]["value"]
##print(LicenseFoto)

bot.send_message(-1001569914422, mensagemProposta, parse_mode="HTML")
print("As propostas foram enviadas com sucesso")
##print("Enviado mensagens compartilhando as notícias do Wikinotícias")
time.sleep(15)
exit()

bot.polling()
