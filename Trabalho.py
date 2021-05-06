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
    carta =carta.replace(carta[len(carta)-1],"")
    return carta

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



#VERIFICAR SE HA JOGADAS POSSIVEIS

while w!=0 and  possui_movimentos_possiveis(baralho)==1 or pergunta=='sim' :
    if w==0 and  possui_movimentos_possiveis(baralho)==-1:
        baralho=cria_baralho()

    x=1
    lista_numerada=[]
    w=0
    n=0
    carta_escolhida=0
    cartas_antes=3
    lista_jogaveis=[]
    resultado=True
    contador=0
    s=0
    para_tirar=0

    
    print('Paciência Acordeão')
    print('-------------------')
    print('Atual Situação:')
    for i in baralho:
        numeração='{0}. {1}'.format(x,i)
        x+=1
        lista_numerada.append(numeração)
    print(lista_numerada)
    
