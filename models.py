# _*_ coding: UTF-8 _*_
class Perfil(object):
	'Classe padrão de Perfil'
	
	def __init__(self, nome, telefone, empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa	

	def imprimir(self):
		print "Nome : %s, Empresa : %s, Telefone : %s" % (self.nome, self.telefone, self.empresa)	


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

	
										