def cria_baralho():
    Baralho=['2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠','2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♦', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣']

    from random import shuffle
    shuffle(Baralho)
    return Baralho

def extrai_naipe(carta):
    for i in carta:
        if i=='♦' or i=='♥' or i=='♣' or i=='♠':
            return i

def extrai_valor(carta):
    if len(carta)==3:
        return carta[0]+carta[1]
    else:
        return carta[0]

def lista_movimentos_possiveis(lista,indice):
    lista_de_movimentos=[]
    if indice-1<0:
        return lista_de_movimentos
    if lista[indice][0]==lista[indice-1][0] or lista[indice][len(lista[indice])-1]==lista[indice-1][len(lista[indice-1])-1]:
        lista_de_movimentos.append(1)
    if indice>2:
        if lista[indice][0]==lista[indice-3][0] or lista[indice][len(lista[indice])-1]==lista[indice-3][len(lista[indice-3])-1]:
            lista_de_movimentos.append(3)
    return lista_de_movimentos
#lista_de_movimentos pode ser [],[1],[1,3],[3]

def empilha(baralho,p_origem,p_destino):
    valor_q_vai=baralho[p_origem]
    baralho.remove(baralho[p_origem])
    baralho[p_destino]=valor_q_vai
    return baralho


def possui_movimentos_possiveis(baralhao):
    x=[]
    for n in range(len(baralhao)):
        x=lista_movimentos_possiveis(baralhao,n)
        if len(x)>0:
            return True
    return False


#########===================FIM DAS FUNCOES======================#########


baralho=cria_baralho()

resultado=False
l=0
z=0
x=1
carta=[]
b=0
p='sla'
#lista_numerada=[]
um=[]
tres=[]
escolha1='sla'
escolha3='sla'
posicao_de_escolha=0

print('Paciência Acordeão')
print('===================')
while possui_movimentos_possiveis(baralho):
    x=1
    lista_numerada=[]
    print('===================')
    print('Atual Situação:')
    print('-------------------')
    #numerar lista
    for i in baralho:
        numeração='{0}. {1}'.format(x,i)
        x+=1
        lista_numerada.append(numeração)
    print(lista_numerada)
    #fim da numeracao da lista
    print(''.ljust(200))
    n=int(input('Coloque aqui uma posição EXISTENTE de uma carta que quer mover(1-{0}): '.format(len(lista_numerada))))
    while n<1 or n>len(lista_numerada):
        print('Tente colocar um valor dentro da escala mostrada')
        n=int(input('Coloque aqui uma posição EXISTENTE de uma carta que quer mover(1-{0}): '.format(len(lista_numerada))))
    while lista_movimentos_possiveis(baralho,n-1)==[]:
        print('Escolha outra posição')
        print()
        n=int(input('Coloque aqui uma posição EXISTENTE de uma carta que quer mover(1-{0}): '.format(len(lista_numerada))))
    print(''.ljust(200))
    print('Sobre qual carta você quer empilhar o {} ?'.format(baralho[n-1]))  
    
    if lista_movimentos_possiveis(baralho,n-1)==[1]:
       um=lista_numerada[n-2].split(' ')
       escolha1='1. '+um[1]
       print(escolha1)
       l=1
       z=1
    if lista_movimentos_possiveis(baralho,n-1)==[3]:
        l=2
        z=2
        tres=lista_numerada[n-4].split(' ')
        escolha3='2. '+tres[1]
        print(escolha3)
    if lista_movimentos_possiveis(baralho,n-1)==[1,3]:
        um=lista_numerada[n-2].split(' ')
        escolha1='1. '+um[1]
        print(escolha1)
        tres=lista_numerada[n-4].split(' ')
        escolha3='2. '+tres[1]
        print(escolha3)
        l=1
        z=2
    print()
    posicao_de_escolha=int(input('Digite a posição aqui({0}-{1}): '.format(l,z)))
    while posicao_de_escolha!=l and posicao_de_escolha!=z:
        print('Tente digitar uma opção possível de ser empilhada')
        print()
        posicao_de_escolha=int(input('Digite a posição aqui({0}-{1}): '.format(l,z)))

    #
    #Momento de mudar e empilhar o baralho:
    if posicao_de_escolha==1:
        empilha(baralho, n-1,n-2)
    if posicao_de_escolha==2:
        empilha(baralho, n-1,n-4 )


    #parte final:
    def possui_movimentos_possiveis(baralhao):
        x=[]
        b=0
        for n in range(len(baralhao)):
            x=lista_movimentos_possiveis(baralhao,n)
            if len(x)>0:
                b=10
        return b

    if len(baralho)==1:
        print('============================')
        print('PARABÉNS, VOCÊ VENCEU!!!!!!')
        print('============================')
        pergunta=input('Gostaria de jogar novamente?: ')
    if len(baralho)>1 and possui_movimentos_possiveis(baralho)==0:
        print('============================')
        print('Você PERDEU.') 
        print()
    if len(baralho)>1 and possui_movimentos_possiveis(baralho)==0 or len(baralho)==1: 
        pergunta=input('Gostaria de jogar novamente?(responda sim ou não): ')
        while pergunta!='sim' and pergunta!='não':
            print('--------------------------')
            print('coloque uma resposta válida')
            pergunta=input('Gostaria de jogar novamente?(responda sim ou não): ')
        if pergunta=='sim':
            baralho=cria_baralho()
        if pergunta=='não':
            baralho=[]

    def possui_movimentos_possiveis(baralhao):
        x=[]
        for n in range(len(baralhao)):
            x=lista_movimentos_possiveis(baralhao,n)
            if len(x)>0:
                return True
        return False

    
