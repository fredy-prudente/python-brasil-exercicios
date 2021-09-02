"""
Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';
"""

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
salario = float(input('Digite seu salário: '))
sexo = input('Digite seu sexo (F ou M): ').lower()
estadocivil = input('Digite seu Estado Civil: (S, C, V, D): ').lower()

while len(nome) <= 3:
    print('Seu nome precisa ter mais de 3 caracteres!')
    nome = input('Digite seu nome: ')

while idade < 0 or idade > 150:
    print('Sua idade precisa está entre 0 e 150 anos!')
    idade = int(input('Digite sua idade: '))

while salario < 0:
    print('Seu salário precisa ser maior que R$0 reais!')
    salario = float(input('Digite seu salário: '))

while 'f' != sexo != 'm':
    print('Seu sexo precisa ser F ou M!')
    sexo = input('Digite seu sexo (F ou M): ').lower()

while estadocivil != 's' != estadocivil != 'c' != estadocivil != 'v' != estadocivil != 'd':
    print('Seu estado civil precisa ser S ou C ou V, ou D!')
    estadocivil = input('Digite seu Estado Civil: (S, C, V, D): ').lower()

print('Informações validadas!')
