guests = ['Adriana','Maria','Safira']

# vamos adicionar mais convidados para a o jantar:

guests.insert(0,'Mario')
guests.insert(2,'Estenio')
guests.append('Bruno')

print('New List: ',guests)

#Aviso:
print('Voce so pode convidar apenas duas pessoas!')

#Modificando:
print('Infelizmente nao havera mais espaço ',guests[6-1])
guests.pop(-1)

print('Infelizmente nao havera mais espaço ',guests[5-1])
guests.pop(4) 

print('Infelizmente nao havera mais espaço ',guests[4-1])
guests.pop(3)

print('Infelizmente nao havera mais espaço ',guests[3-1])
guests.pop(2)

# mostrando:
print(guests)

# apagando:
del guests[0]
print(guests)

del guests[0]
print('Empty list: ',guests)