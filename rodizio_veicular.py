placa = int(input("Digite o final da placa do veiculo: "))

if placa==1 or placa==2:
    print("Rodizio na segunda-feira")
elif placa==3 or placa==4:
    print("Rodizio na terça-feira")
elif placa==5 or placa==6:
    print("Rodizio na quarta-feira")
elif placa==7 or placa==8:
    print("Rodizio na quinta-feira")
elif placa==9 or placa==0:
    print("Rodizio na sexta-feira")
else:
    print("Placa inválido")