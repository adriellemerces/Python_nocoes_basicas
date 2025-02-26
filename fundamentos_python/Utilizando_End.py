# Podemos executar um código utilizando uma ou mais condições como no exemplo abaixo, caso seja a pessoa tenha 18 anos e a permissão seja TRUE ela pode dirigir, caso uma das condições seja FALSE ela não pode dirigir.

idade = 18
possui_Habilitacao = False

if idade >= 18 and possui_Habilitacao:
    print("Essa pessoa pode dirigir")

else:
    print("Essa pessoa nao pode dirigir")


###################################################################################
#Para executar um código caso apenas uma das condições sejam TRUE então usamos o operador *OR*, com o OR o código só é iguinorado se todas as condições forem falsas, o or serve para adicionar condições alternativas

nota1 = 9
nota2 = 10
nota3 = 5

if nota1 >= nota2 or nota3 > nota2:
    print("Pelomenos uma das condicoes são verdadeiras")
else:
    print("nenhuma das condicoes sao verdadeiras")