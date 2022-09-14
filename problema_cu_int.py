def creare_lista():
	n = int(input('Nr. de elemente = '))
	lista_locala = []
	for i in range(n):
		elem = int(input('Elementul '+str(i)+' este:'))
		lista_locala.append(elem)
	return lista_locala
lista_int = creare_lista() 
print(lista_int)