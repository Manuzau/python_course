# Você acabou de saber que um de seus convidados não poderá comparecer ao jantar,
# portanto será necessário enviar um novo conjunto de convites.
# Você deverá pensar em outra pessoa para convidar.

guests = ['Adriana','Maria','Safira']
print('Old list of guests: ',guests)

#A Adriana nao ira aparecer ao jantar, entao a Iracelma vai ser convidada no lugar dela, portanto...
guests[0] = 'Iracelma'
print('New list of guests: ',guests,'Adriana foi removida!')

print('Convidados: \n')
print('Receba o seu convite com muito amor, esta sera uma sentada em que o Senhor/a ',guests[0],'sera a pessoa mais importante para mim! ')
print('Receba o seu convite com muito amor, esta sera uma sentada em que o Senhor/a ',guests[1],'sera a pessoa mais importante para mim! ')
print('Receba o seu convite com muito amor, esta sera uma sentada em que o Senhor/a ',guests[2],'sera a pessoa mais importante para mim! ')