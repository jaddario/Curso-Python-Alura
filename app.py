# -*- coding: UTF-8 -*-

def cadastrar(lista_de_nomes):
    print 'Digite o nome que você quer cadastrar:'
    nome = raw_input()
    lista_de_nomes.append(nome)

def listar_nomes(lista_de_nomes):
    print 'Listando os nomes contidos na lista:'
    for nome in lista_de_nomes:
        print nome

def remover_nome_da_lista(lista_de_nomes):
	print 'Digite o nome que você deseja remover'
	nome = raw_input()
	if nome in lista_de_nomes:
		lista_de_nomes.remove(nome)
	else:
		print 'Nome não consta na lista'	

def altera_nome_da_lista(lista_de_nomes):
	print 'Digite o nome que deseja alterar'
	nome_a_alterar = raw_input()
	if nome_a_alterar in lista_de_nomes:
		print 'Digite o nome correto'
		nome_correto = raw_input()
		posicao = lista_de_nomes.index(nome_a_alterar)
		lista_de_nomes[posicao] = nome_correto
	else:
		print 'Nome não consta na  lista'

def procurar_nome_da_lista(lista_de_nomes):
	print 'Digite o nome que deseja procurar'
	nome_desejado = raw_input()
	if nome_desejado in lista_de_nomes:
		print 'O convidado %s está na lista' % (nome_desejado)
	else:
		print 'Não existe esse convidado na lista'				

def menu():
    lista_de_nomes = []
    escolha = ''
    while(escolha != '0'):    
        print 'Digite: 1 para cadastrar, 2 para listar, 3 para remover, 4 para alterar, 5 para procurar por um nome e 0 para terminar'
        escolha = raw_input()

        if(escolha == '1'):
            cadastrar(lista_de_nomes)

        if(escolha == '2'):
            listar_nomes(lista_de_nomes)

        if(escolha == '3'):
            remover_nome_da_lista(lista_de_nomes)

        if(escolha == '4'):
            altera_nome_da_lista(lista_de_nomes)    

        if(escolha == '5'):
            procurar_nome_da_lista(lista_de_nomes)    
menu()