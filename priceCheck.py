# Bibliotecas
import time,requests
from bs4 import BeautifulSoup
import json
import re
from requests_html import HTML, HTMLSession
from os import system

# Funções para checar o nome das placas e os preços

def check3090(data):
    code = ['3','0','9','0','*']
    nome = data['nome'].replace(" ","").replace(",","")
    hit = 0
    for letra in nome:
        if letra.upper() == code[0]:
            code.pop(0)
            hit += 1
        elif hit != 0:
            break
    return (len(code)==1)

def checkPrice3090(data):
    return (data['preco_desconto'] < 14000)

def check3080(data):
    code = ['3','0','8','0','*']
    nome = data['nome'].replace(" ","").replace(",","")
    hit = 0
    for letra in nome:
        if letra.upper() == code[0]:
            code.pop(0)
            hit += 1
        elif hit != 0:
            break
    return (len(code)==1)

def checkPrice3080(data):
    return (data['preco_desconto'] < 11000)

def check3070(data):
    code = ['3','0','7','0','*']
    nome = data['nome'].replace(" ","").replace(",","")
    hit = 0
    for letra in nome:
        if letra.upper() == code[0]:
            code.pop(0)
            hit += 1
        elif hit != 0:
            break
    return (len(code)==1)

def checkPrice3070(data):
    return (data['preco_desconto'] < 7000)

def check3060Ti(data):
    code = ['3','0','6','0','T','I','*']
    nome = data['nome'].replace(" ","").replace(",","")
    hit = 0
    for letra in nome:
        if letra.upper() == code[0]:
            code.pop(0)
            hit += 1
        elif hit != 0:
            break
    return (len(code)==1)

def checkPrice3060Ti(data):
    return (data['preco_desconto'] < 7000)

def check2060(data):
    code = ['2','0','6','0','*']
    nome = data['nome'].replace(" ","").replace(",","")
    hit = 0
    for letra in nome:
        if letra.upper() == code[0]:
            code.pop(0)
            hit += 1
        elif hit != 0:
            break
    return (len(code)==1)

def checkPrice2060(data):
    return (data['preco_desconto'] < 2800)

def check5600(data):
    code = ['5','6','0','0','*']
    nome = data['nome'].replace(" ","").replace(",","")
    hit = 0
    for letra in nome:
        if letra.upper() == code[0]:
            code.pop(0)
            hit += 1
        elif hit != 0:
            break
    return (len(code)==1)

def checkPrice5600(data):
    return (data['preco_desconto'] < 4500)

def check5500(data):
    code = ['5','5','0','0','*']
    nome = data['nome'].replace(" ","").replace(",","")
    hit = 0
    for letra in nome:
        if letra.upper() == code[0]:
            code.pop(0)
            hit += 1
        elif hit != 0:
            break
    return (len(code)==1)

def checkPrice5600(data):
    return (data['preco_desconto'] < 2800)

def check1660Super(data):
    code = ['1','6','6','0','S','U','P','E','R','*']
    nome = data['nome'].replace(" ","").replace(",","")
    hit = 0
    for letra in nome:
        if letra.upper() == code[0]:
            code.pop(0)
            hit += 1
        elif hit != 0:
            break
    return (len(code)==1)

def checkPrice1660Super(data):
    return (data['preco_desconto'] < 2200)
	
def checkAvailable(data):
	return data['disponibilidade']

def searchBoard(data, codigo):
	cont = 0
	for dados in data:
		if check3090(dados) and checkPrice3090(dados) and checkAvailable(dados):
			if not dados['codigo'] in codigoPlacas:
				print('Notificando 3090...')
				codigoPlacas.append(dados['codigo'])
				message = 'https://www.kabum.com.br'+dados['link_descricao']
				urlSendMessage = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(token,chatId,message)
				requests.get(urlSendMessage)
				cont += 1
			# print(not dados['codigo'] in codigoPlacas)
		elif check3080(dados) and checkPrice3080(dados) and checkAvailable(dados):
			if not dados['codigo'] in codigoPlacas:
				print('Notificando 3080...')
				codigoPlacas.append(dados['codigo'])
				message = 'https://www.kabum.com.br'+dados['link_descricao']
				urlSendMessage = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(token,chatId,message)
				requests.get(urlSendMessage)
				cont += 1
			# print(not dados['codigo'] in codigoPlacas)
		elif check3070(dados) and checkPrice3070(dados) and checkAvailable(dados):
			if not dados['codigo'] in codigoPlacas:
				print('Notificando 3070...')
				codigoPlacas.append(dados['codigo'])
				message = 'https://www.kabum.com.br'+dados['link_descricao']
				urlSendMessage = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(token,chatId,message)
				requests.get(urlSendMessage)
				cont += 1
			# print(not dados['codigo'] in codigoPlacas)
		elif check3060Ti(dados) and checkPrice3060Ti(dados) and checkAvailable(dados):
			if not dados['codigo'] in codigoPlacas:
				print('Notificando 3060 Ti...')
				codigoPlacas.append(dados['codigo'])
				message = 'https://www.kabum.com.br'+dados['link_descricao']
				urlSendMessage = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(token,chatId,message)
				requests.get(urlSendMessage)
				cont += 1
			# print(not dados['codigo'] in codigoPlacas)
		elif check1660Super(dados) and checkPrice1660Super(dados) and checkAvailable(dados):
			if not dados['codigo'] in codigoPlacas:
				print('Notificando 1660 Super...')
				codigoPlacas.append(dados['codigo'])
				message = 'https://www.kabum.com.br'+dados['link_descricao']
				urlSendMessage = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(token,chatId,message)
				requests.get(urlSendMessage)
				cont += 1
			# print(not dados['codigo'] in codigoPlacas)
		elif check5600(dados) and checkPrice5600Super(dados) and checkAvailable(dados):
			if not dados['codigo'] in codigoPlacas:
				print('Notificando 5600...')
				codigoPlacas.append(dados['codigo'])
				message = 'https://www.kabum.com.br'+dados['link_descricao']
				urlSendMessage = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(token,chatId,message)
				requests.get(urlSendMessage)
				# print(urlSendMessage)
				cont += 1
		elif check5500(dados) and checkPrice5500Super(dados) and checkAvailable(dados):
			if not dados['codigo'] in codigoPlacas:
				print('Notificando 5500...')
				codigoPlacas.append(dados['codigo'])
				message = 'https://www.kabum.com.br'+dados['link_descricao']
				urlSendMessage = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(token,chatId,message)
				requests.get(urlSendMessage)
				# print(urlSendMessage)
				cont += 1
		elif check2060(dados) and checkPrice2060Super(dados) and checkAvailable(dados):
			if not dados['codigo'] in codigoPlacas:
				print('Notificando 2060...')
				codigoPlacas.append(dados['codigo'])
				message = 'https://www.kabum.com.br'+dados['link_descricao']
				urlSendMessage = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(token,chatId,message)
				requests.get(urlSendMessage)
				# print(urlSendMessage)
				cont += 1
		else:
			pass
	if cont == 0:
		 print('Não Encontrei uma placa nos critérios desejados.')
	else:
		print('Foram encontradas: {} placas.'.format(cont))

print('Incializando...')
time.sleep(5)

codigoPlacas = []
# Página Web
urlPlacas = "https://www.kabum.com.br/hardware/placa-de-video-vga?pagina=1&ordem=4&limite=100&prime=false&marcas=[]&tipo_produto=[]&filtro=[]"

# Bot Telegram INFO
token = 'set telegram bot token here'
chatId = 'set chat id here'

while True:
	
	system('cls')
	try:
		print('Requisitando Página Web')
		# Requisição HTML
		session = HTMLSession()
		response = session.get(urlPlacas)
		script = response.html.find('script')[21]
		#parse variável listagemDados
		initIndex = script.text.find('const listagemDados')+6
		endIndex = script.text.find('const listagemErro')-1
		var = script.text[initIndex:endIndex]
		#define regex match pattern
		match_scripts = re.findall(r'(.*) (=) ([^;].*)', var)
		#     transforma str em JSON
		data = json.loads(match_scripts[0][2])
		
		print('Procurando placas...')
		searchBoard(data,codigoPlacas)
		
	except:
		pass
	print('Nova Busca em 5 segundos...')
	time.sleep(5)