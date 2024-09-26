import test.test
from lib.arquivo import escrever, pesquisar, exibir, excluir, alterar, gerarBoletim
import lib.menu as menu

menu.cls()
while True:
    menu.exibir()
    opcao = menu.selecionar()

    if opcao == "1":
        ra = menu.obterRA()
        aluno = pesquisar(ra)
        if aluno:
            exibir(ra, aluno)
        else:
            print("Aluno não encontrado")
    elif opcao == "2":
        dados = menu.obterDadosDoAluno()

        escrever(dados)
    elif opcao == "3":
        ra = menu.excluirAluno()
        excluir(ra)
    elif opcao == "4":
        ra = menu.alterarDadosAluno()
        alterar(ra)
    elif opcao == "5":
        ra = menu.gerarBoletimAluno()
        gerarBoletim(ra)
    else:
        break

#ricardo barsellis megasoft
