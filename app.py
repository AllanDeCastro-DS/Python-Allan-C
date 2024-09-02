#escrever um programa que realiza a ordenação natural e ordenação customizada

itens = ['maçã', 'banana', 'laranja', 'uva', 'abacate']
itens2= [1,4,5,2,3,9,6,0,7,5,8]



def organiza(item):
    return sorted(item)


def organiza_Custom(item):
    return sorted(item, key=len)



print("Ordenação natural:", organiza(itens2))
print("Ordenação customizada:", organiza_Custom(itens))

