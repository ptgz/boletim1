# r leitura, w = sobrescreve, a = adiciona ao final || utf-8 pra permitir acento
from lib.media import media
import json

DATAPATH = "database/dados.json"


def escrever(dados: list):
    print(dados)
    mediaCalculada = media(dados[2:])
    dados.append(mediaCalculada)

    with open(DATAPATH, "r+", encoding="utf-8") as file:
        fread = file.read()
        data = json.loads(fread)

    data[dados[0]] = {
        "nome": dados[1],
        "notas": [dados[2], dados[3], dados[4]]
    }

    with open(DATAPATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def pesquisar(ra):
    with open(DATAPATH, 'r', encoding="utf-8") as file:
        data = json.load(file)
    try:
        aluno = data[ra]
    except:
        return {}
    if aluno:
        return aluno
    return {}


def formatarDados(ra, dados):
    media = sum(dados['notas']) / 3
    formato = f'''
    =========================
    |       U N A S P       |
    =========================
    | RA: {ra}{" " * (11 - len(ra))}       |
    | NOME: {(dados['nome'] + ((" ") * (12 - len(dados['nome'])))) if len(dados['nome']) < 9 else dados['nome'][0:9] + "..."}    |
    |			            |
    =========================
    |    BOLETIM ESCOLAR	|
    =========================
    | NOTA 01       |  {"" if float(dados['notas'][0]) >= 10 else " "}{int(float(dados['notas'][0]) * 10) / 10} |
    | NOTA 02       |  {"" if float(dados['notas'][1]) >= 10 else " "}{int(float(dados['notas'][1]) * 10) / 10} |
    | NOTA 03       |  {"" if float(dados['notas'][2]) >= 10 else " "}{int(float(dados['notas'][2]) * 10) / 10} |
    +---------------+-------+
    | MÉDIA         |  {"" if float(media) >= 10 else " "}{int(float(media) * 10) / 10} |
    =========================
            '''
    return formato


def exibir(ra, dados):
    formato = formatarDados(ra, dados)
    if dados:
        print(formato)
    else:
        print("Aluno não encontrado")


def alterar(ra):
    dados = pesquisar(ra)
    print("Qual dado deseja alterar?")
    print(f'''
    1 - Nome: {dados['nome']}
    2 - Nota 1: {dados['notas'][0]}
    3 - Nota 2: {dados['notas'][1]}
    4 - Nota 3: {dados['notas'][2]}
    ''')
    opcao = int(input("Escolha uma opção: "))

    with open(DATAPATH, "r", encoding="utf-8") as file:
        fread = file.read()
        data = json.loads(fread)

    if opcao == 1:
        novoNome = input("Digite o novo nome: ")
        dados['nome'] = novoNome
    elif opcao == 2:
        novaNota1 = float(input("Digite a nova nota 1: "))
        dados['notas'][0] = novaNota1
    elif opcao == 3:
        novaNota2 = float(input("Digite a nova nota 2: "))
        dados['notas'][1] = novaNota2
    elif opcao == 4:
        novaNota3 = float(input("Digite a nova nota 3: "))
        dados['notas'][2] = novaNota3
    else:
        print("Opção inválida!")
        return

    data[ra] = dados

    with open(DATAPATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    pass


def excluir(ra):
    if pesquisar(ra):
        with open(DATAPATH, "r", encoding="utf-8") as file:
            fread = file.read()
            data = json.loads(fread)

        data.pop(ra)

        with open(DATAPATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)


def gerarBoletim(ra):
    dados = pesquisar(ra)
    formato = formatarDados(ra, dados)
    with open(f"boletins/BOLETIM_{ra}.txt", "w", encoding="utf-8") as file:
        file.write(formato)
