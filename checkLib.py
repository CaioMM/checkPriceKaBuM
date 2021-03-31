import json, re
from requests_html import HTMLSession

disponibilidade = 0
notificacao = 1

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

def check5700(data):
	code = ['5','7','0','0','*']
	nome = data['nome'].replace(" ","").replace(",","")
	hit = 0
	for letra in nome:
		if letra.upper() == code[0]:
			code.pop(0)
			hit += 1
		elif hit != 0:
			break
	return (len(code)==1)

def checkPrice5700(data):
	return (data['preco_desconto'] < 5500)

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

def checkPrice5500(data):
	return (data['preco_desconto'] < 2800)



def checkAvailable(data):
	return data['disponibilidade']

def requestKabumVGAPages():
	dados = []
	tries = 0
	page = 1
	while (page <= 5):

		statusCode = 0
		kaBumWebPage = f'https://www.kabum.com.br/hardware/placa-de-video-vga?pagina={page}&ordem=4&limite=100&prime=false&marcas=[]&tipo_produto=[]&filtro=[]'
		session = HTMLSession()

		try:

			response = session.get(url=kaBumWebPage, timeout=2)

		except Exception as e:

			print(e)
			tries += 1
			if (tries == 3):
				print('next page.')
				page += 1
				tries = 0

		else:

			statusCode = response.status_code
#             print(f'Status: {statusCode}')
			print(f'Page: {page}')

			if statusCode == 200:

				# zera número de tentativas
				tries = 0
				# avança para a próxima página
				page += 1

				# procura pelo script referente aos produtos na página
				script = response.html.find('script')[21]
				#parse variável listagemDados
				initIndex = script.text.find('const listagemDados')+6
				endIndex = script.text.find('const listagemErro')-1
				var = script.text[initIndex:endIndex]
				#define regex match pattern
				match_scripts = re.findall(r'(.*) (=) ([^;].*)', var)
				#     transforma str em JSON
				dado = json.loads(match_scripts[0][2])

				# caso haja uma listagem dos produtos na página
				if any(dado):
					dados.append(dado)
#                     print(f'{len(dado)} itens nesta página.')
				else:
					# print('Nenhum item nesta página.')
					break
	return dados

def createDb():
	
	# requisita página web
	dados = requestKabumVGAPages()
	itensKabum = {}
	notificado = False
	
	for page in dados:
		for dado in page:
			itensKabum[dado['codigo']] = [dado['disponibilidade'], notificado]
#             itensKabum.append({dado['codigo']: [dado['disponibilidade'], False]})
	
	return [itensKabum, dados]

def checkAMD(data, cont, itensKabum):

	alertSent = False
	
	if check5700(data) and checkPrice5700(data):
		
		cont += 1
		
		if not itensKabum[data['codigo']][notificacao]:
			
			alertSent = telegramSendAlert(data['link_descricao'])
		
		else:
			print('Já notifiquei esta placa.')
		
		if(alertSent):
			
			itensKabum[data['codigo']][notificacao] = alertSent
			print('RX 5700 Notificada.')
			
	if check5600(data) and checkPrice5600(data):
		
		cont += 1
		
		if not itensKabum[data['codigo']][notificacao]:
			
			alertSent = telegramSendAlert(data['link_descricao'])
		
		else:
			print('Já notifiquei esta placa.')
		
		if(alertSent):
			
			itensKabum[data['codigo']][notificacao] = alertSent
			print('RX 5600 Notificada.')
	
	if check5500(data) and checkPrice5500(data):
		
		cont += 1
		
		if not itensKabum[data['codigo']][notificacao]:
			
			alertSent = telegramSendAlert(data['link_descricao'])
		
		else:
			print('Já notifiquei esta placa.')
		
		if(alertSent):
			
			itensKabum[data['codigo']][notificacao] = alertSent
			print('RX 5500 Notificada.')

def checkNividia(data, cont, itensKabum):
	
	alertSent = False
	
	if check3090(data) and checkPrice3090(data):
		
		cont += 1
		
		if not itensKabum[data['codigo']][notificacao]:
			
			alertSent = telegramSendAlert(data['link_descricao'])
		
		else:
			print('Já notifiquei esta placa.')
		
		if(alertSent):
			
			itensKabum[data['codigo']][notificacao] = alertSent
			print('3090 Notificada.')

	if check3080(data) and checkPrice3080(data):
		
		cont += 1
		
		if not itensKabum[data['codigo']][notificacao]:
			
			alertSent = telegramSendAlert(data['link_descricao'])
		
		else:
			print('Já notifiquei esta placa.')
		
		if(alertSent):
			
			itensKabum[data['codigo']][notificacao] = alertSent
			print('3080 Notificada.')

	if check3070(data) and checkPrice3070(data):
		
		cont += 1
		
		if not itensKabum[data['codigo']][notificacao]:
			
			alertSent = telegramSendAlert(data['link_descricao'])
		
		else:
			print('Já notifiquei esta placa.')
		
		if(alertSent):
			
			itensKabum[data['codigo']][notificacao] = alertSent
			print('3070 Notificada.')

	if check3060Ti(data) and checkPrice3060Ti(data):
		
		cont += 1
		
		if not itensKabum[data['codigo']][notificacao]:
			
			alertSent = telegramSendAlert(data['link_descricao'])
		
		else:
			print('Já notifiquei esta placa.')
		
		if(alertSent):
			
			itensKabum[data['codigo']][notificacao] = alertSent
			print('3060 ti Notificada.')

	if check2060(data) and checkPrice2060(data):
		
		cont += 1
		
		if not itensKabum[data['codigo']][notificacao]:
			
			alertSent = telegramSendAlert(data['link_descricao'])
		
		else:
			print('Já notifiquei esta placa.')
		
		if(alertSent):
			
			itensKabum[data['codigo']][notificacao] = alertSent
			print('2060 Notificada.')

	if check1660Super(data) and checkPrice1660Super(data):
		
		cont += 1
		
		if not itensKabum[data['codigo']][notificacao]:
			
			alertSent = telegramSendAlert(data['link_descricao'])
		
		else:
			print('Já notifiquei esta placa.')
		
		if(alertSent):
			
			itensKabum[data['codigo']][notificacao] = alertSent
			print('1660 Super Notificada.')

def checkState(dado, itensKabum):
	
	
	if dado['disponibilidade'] != itensKabum[dado['codigo']][disponibilidade]:
		
		itensKabum[dado['codigo']][disponibilidade] = dado['disponibilidade']
		itensKabum[dado['codigo']][notificacao] = False
		
		print(f"Disponibilidade do Produto {dado['codigo']} Alterado para: {dado['disponibilidade']}")

def telegramSendAlert(urlProduto):
	
	# criando a mensagem
	message = 'https://www.kabum.com.br' + urlProduto
	
	# inicializando variáveis do bot bot
	
	
	# protótipo de mensagem
	# message = "https://www.kabum.com.br/produto/129973/placa-de-v-deo-asus-nvidia-geforce-gtx-1650-4gb-gddr6-tuf-gtx1650-o4gd6-p-gaming"
	
	# url para envio da mensagem
	url = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(token,chatId,message)
	session = HTMLSession()
	
	tries = 0
	while tries < 3:
		try:

			response = session.get(url, timeout=1)

		except Exception as e:

				print(f'Error: {e}')
				tries += 1

		else:
			return True
	