"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
"""

usuario = input('Nome de Usuário: ').lower()
senha = input('Senha: ').lower()

while usuario == senha:
    print('A senha não pode ser igual ao usuário!')
    senha = input('Digite a senha: ').lower()

print('Conta criada com sucesso!')
