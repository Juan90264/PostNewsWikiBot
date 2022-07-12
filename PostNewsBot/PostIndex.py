#### Teste index
#### Código inspirado (incluindo os scripts chamados abaixo) no https://github.com/albertoleoncio/wikipedia/blob/master/rss.php, do usuário albertoleoncio
import time
import include

###### Posta a imagem do dia no canal
##def run_file(path):
##    return exec(open(path).read());
##run_file('C:/Users/User/Desktop/PostImageApagar.py');

##time.sleep(2)

print("**********************************************")
print("**********************************************")
print("*******INICIANDO POSTAGEM DAS MENSAGENS*******")
print("*******NO CANAL DA WIKIPÉDIA NO TELEGRAM******")
print("*************NO TOTAL: (3 ETAPAS)*************")
print("**********************************************")
print("**********************************************")
time.sleep(5)
print("\n(1/3) ETAPA: Postagem do artigo em destaque na Página Principal")
###### Posta o artigo em destaque na Página Principal no canal
def run_fileArtigoEAD(pathArtigoEAD):
    return include.path(pathArtigoEAD)
run_fileArtigoEAD('PostEAD.py'); ## Chama o arquivo PostEAD.py

time.sleep(2)
print("\n(2/3) ETAPA: Postagem da curiosidade atual da Wikipédia:Sabia que?")
###### Posta a curiosidade do Sabia que? no canal
def run_fileSabiaQue(pathSabiaQue):
    return include.path(pathSabiaQue)
run_fileSabiaQue('PostSabiaQue.py'); ## Chama o arquivo PostSabiaQue.py

time.sleep(2)
print("\n(3/3) ETAPA: Postagem do evento atual que está aparecendo na Página Principal")
###### Posta o evento atual que está aparecendo na Página Principal no canal
def run_fileEventoAtual(pathEventoAtual):
    return include.path(pathEventoAtual)
run_fileEventoAtual('PostEventosAtuais.py'); ## Chama o arquivo PostEventosAtuais.py

print("\nAs etapas foram concluídas com sucesso, postagens enviadas!")
time.sleep(2)
print("\nFinalizando código....")
time.sleep(15)
exit()

bot.polling()
