def ordenacao_total(list):
    return sorted(list,key=len, reverse=True)

lista = ['maçã', 'banana','uva' , 'laranja', 'abacate']
print("Lista original:", lista)
print("Lista ordenada:", ordenacao_total(lista))