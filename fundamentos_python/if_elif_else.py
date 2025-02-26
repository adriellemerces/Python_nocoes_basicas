# if e else são condições de *faça* e *se não, faça* , no meio deles podemos usar outra condição chamada elif, onde podemos adicionar quantas quisermos antes do else


numero = 20

if numero < 12:
    print("Bom dia")

elif numero < 17:
    print("Boa tarde")  

else:
    print("Boa noite")    

############################################################################################

salario = 2699 + 30

if salario < 2000:
    print("O salario não esta correto")

elif salario < 2500:
    print("O salario tambem nao esta correto")  

elif salario > 2500:
    print("O salario esta correto")  

else:
    print("O funcionario deve perguntar ao rh sobre seu salario, para entender porque nao esta correto")    


#####################################################################################################################################
#abaixo existem duas condições if, isso faz com que a resposta das duas saiam no console e não apenas uma

Segunda = "Feriado"
Terça = "Nao e feriado"

if Segunda == "Feriado":
    print(Segunda + " nao havera aula")

if Terça == "Nao e feriado":
    print(Terça + " havera aula normal")


