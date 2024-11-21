horario = (input("Digite uma seu horario de trabalho, M-Matutino, V-Vespertino, N-Noturno : "))

if horario == 'M' or horario == 'm':
    print("Seu horario é no periodo da manhã")

elif horario == 'V' or horario == 'v':
    print(f"Seu horario é no periodo da tarde ")

elif horario == 'N' or horario == 'n':
    print(f"Seu horario é no periodo da noite ")

else:
    print("Seu horario não existe")