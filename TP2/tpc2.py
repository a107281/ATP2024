# Solução do TPC2

print("Bem-vindo! Este é o Jogo do 'Adivinha o Número'!")
print("Adivinha o número em que estou a pensar. Está entre 0 e 100.")

import random
numero = random.randint(0,100)

t = 1
adivinha = int(input("Adivinha o número em que estou a pensar. Está entre 0 e 100."))


while adivinha != numero:
    if adivinha > numero:
        adivinha = int(input("O número em que pensei é menor."))
        print("O número que pensei é menor.")
    if adivinha < numero:
        adivinha = int(input("O número que pensei é maior."))
        print("O número que pensei é maior.")
    t = t + 1

print(f"Acertou! O número que pensei era {numero}.")
print(f"Precisou de {t} tentativas.")