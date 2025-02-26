#Os tipos de dados são básicos em python são: inteiros, strings, floats e booleanos
#Para verificar o tipo de um valor podemos verifica-lo usando *type()*

dado = True
numero = 59.9090
nome = "Adrielle Merces"
idade = 22

print(type(dado))
print(type(numero))
print(type(nome))
print(type(idade))


#####################################################################################
#Convertendo dados

votos = "500"
print(type(votos))

convertendo_votos = int(votos)
print(type(convertendo_votos))
print(convertendo_votos < 1000)
