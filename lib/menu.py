import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    pass


def exibir():
    MENU = '''
============================
|      BOLETIM ESCOLAR     |
============================
| 1 | Consultar RA         |
| 2 | Cadastrar Aluno      |
| 3 | Excluir Aluno        |
| 4 | Alterar Notas        |
| 5 | Gerar Boletim        |
----------------------------
| x | Sair do Sistema      |
============================
'''
    print(MENU)


def selecionar():
    return input("Escolha uma opção: ")


def obterRA():
    ra = input("Digite o RA: ")
    cls()
    return ra


def obterDadosDoAluno():
    cls()
    ra = input("Digite seu RA: ")
    nome = input("Digite seu nome: ")

    nota1 = float(input(f"Insira a nota 1: "))
    nota2 = float(input(f"Insira a nota 2: "))
    nota3 = float(input(f"Insira a nota 3: "))
    return [ra, nome, nota1, nota2, nota3]


def excluirAluno():
    cls()
    ra = input("Digite o RA a ser excluido: ")
    return ra


def gerarBoletimAluno():
    cls()
    ra = input("Digite o RA para imprimir um boletim: ")
    return ra


def alterarDadosAluno():
    cls()
    ra = input("Digite o RA do aluno a ser alterado: ")
    return ra
