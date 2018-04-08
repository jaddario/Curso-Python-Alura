# _*_ coding: UTF-8 _*_
class Perfil(object):
	'Classe padrão de Perfil'
	
	def __init__(self, nome, telefone, empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa
		self.__curtidas = 0	

	def imprimir(self):
		print "Nome : %s, Empresa : %s, Telefone : %s, Curtidas : %s" % (self.nome, self.telefone, self.empresa, self.__curtidas)

	def curtir(self):
		self.__curtidas+=1

	def obter_curtidas(self):
		return self.__curtidas

	@staticmethod	
	def gerar_perfis(nome_arquivo):
		perfis=[]
		arquivo = open(nome_arquivo, 'r')
		for linha in arquivo:
			valores = linha.split(',')

			if(len(valores)is not 3):
				raise Perfil_Error('Uma linha do arquivo deve ter 3 valores')

			perfis.append(Perfil(*valores))
		arquivo.close()	
		return perfis		 		

class Perfil_Vip(Perfil):
	'Classe padrão de Perfil Vip'
	def __init__ (self, nome, telefone, empresa, apelido=''):
		super(Perfil_Vip, self).__init__(nome, telefone, empresa)
		self.apelido = apelido

	def obter_creditos(self):
		return super(Perfil_Vip, self).obter_curtidas() * 10.0	

class Perfil_Error(Exception):
	def __init__(self, mensagem):
		self.mensagem = mensagem

	def __str__(self):
		return repr(self.mensagem) 	
		


class Data(object):
	"Classe data com metodo de formatação"
	def __init__(self, dia, mes, ano):
		self.dia = dia
		self.mes = mes
		self.ano = ano
	
	def imprimir_data_formatada(self):
		print "%s/%s/%s" % (self.dia, self.mes, self.ano)	

class Pessoa(object):	
	def __init__(self, nome, peso, altura):
		self.nome = nome
		self.peso = peso
		self.altura = altura

	def calcula_imc(self):
		imc = float(self.peso)/float((self.altura)*(self.altura))
		print 'Imc de %s: %s' % (self.nome, imc)	

	
										