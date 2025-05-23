import json
import os
import time
from datetime import datetime

# Arquivos de dados
USUARIOS_FILE = "usuarios.json"
RESPOSTAS_FILE = "respostas.json"
ACESSOS_FILE = "acessos.json"
TEMPO_FILE = "tempo_uso.json"

# Funções auxiliares
def carregar_dados(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def salvar_dados(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# Função para registrar acessos por dia
def registrar_acesso(cpf):
    acessos = carregar_dados(ACESSOS_FILE)
    data_hoje = datetime.now().strftime("%Y-%m-%d")

    if data_hoje not in acessos:
        acessos[data_hoje] = []

    acessos[data_hoje].append(cpf)
    salvar_dados(ACESSOS_FILE, acessos)

# Cadastrar usuário com idade
def cadastrar_usuario():
    print("\n== Cadastrar Novo Usuário ==")
    nome = input("Nome: ")
    cpf = input("CPF (apenas números): ")
    idade = input("Idade: ")

    usuarios = carregar_dados(USUARIOS_FILE)

    if cpf in usuarios:
        print("Usuário já cadastrado.")
        return cpf

    usuarios[cpf] = {
        "nome": nome,
        "idade": idade
    }

    salvar_dados(USUARIOS_FILE, usuarios)
    print(f"Usuário {nome} cadastrado com sucesso.")
    return cpf

# Exercício simples
def fazer_exercicio(cpf):
    print("\n== Exercício de Lógica ==")
    pergunta = "Qual é o valor de x no código: x = 2 + 3?"
    resposta_correta = "5"

    print(f"Pergunta: {pergunta}")
    resposta_usuario = input("Sua resposta: ")

    respostas = carregar_dados(RESPOSTAS_FILE)

    if cpf not in respostas:
        respostas[cpf] = []

    respostas[cpf].append({
        "pergunta": pergunta,
        "resposta": resposta_usuario,
        "correta": resposta_usuario.strip() == resposta_correta
    })

    salvar_dados(RESPOSTAS_FILE, respostas)

    if resposta_usuario.strip() == resposta_correta:
        print("Resposta correta! Muito bem!\n")
    else:
        print("Ops! Resposta incorreta. A resposta certa é 5.\n")

# Ver desempenho nos exercícios
def ver_desempenho(cpf):
    print("\n== Ver Desempenho ==")
    respostas = carregar_dados(RESPOSTAS_FILE)

    if cpf not in respostas or not respostas[cpf]:
        print("Nenhum exercício realizado ainda.\n")
        return

    acertos = sum(1 for r in respostas[cpf] if r["correta"])
    total = len(respostas[cpf])
    print(f"Você respondeu {total} exercício(s) e acertou {acertos}.")
    print("Continue praticando!\n")

# Ver relatórios gerais
def ver_relatorios():
    print("\n== Relatórios da Plataforma ==")

    # Acessos por dia
    acessos = carregar_dados(ACESSOS_FILE)
    print("\nAcessos por dia:")
    for data, lista in acessos.items():
        print(f"- {data}: {len(lista)} acesso(s)")

    # Tempo médio de uso
    tempos = carregar_dados(TEMPO_FILE)
    tempos_lista = [sum(v)/len(v) for v in tempos.values() if len(v) > 0]
    if tempos_lista:
        media = sum(tempos_lista) / len(tempos_lista)
        print(f"\nTempo médio de uso por sessão: {round(media/60, 2)} minutos")
    else:
        print("\nAinda não há dados de tempo de uso.")

    # Idade dos usuários
    usuarios = carregar_dados(USUARIOS_FILE)
    if usuarios:
        idades = [int(d["idade"]) for d in usuarios.values()]
        media_idade = sum(idades) / len(idades)
        print(f"\nMédia de idade dos usuários: {round(media_idade, 2)} anos")
    else:
        print("\nNenhum usuário cadastrado.")

# Menu principal
def menu_principal():
    print("=== BrightBits ONG - Aprenda Programação com Segurança ===")
    cpf_usuario = None

    inicio = time.time()  # Início do tempo de uso

    while True:
        print("\nMenu:")
        print("1. Cadastrar usuário")
        print("2. Fazer exercício de lógica")
        print("3. Ver desempenho")
        print("4. Ver relatórios gerais")
        print("5. Sair")

        opcao = input("Escolha uma opção (1-5): ")

        if opcao == "1":
            cpf_usuario = cadastrar_usuario()
            registrar_acesso(cpf_usuario)
        elif opcao == "2":
            if not cpf_usuario:
                print("Por favor, cadastre-se primeiro.")
            else:
                fazer_exercicio(cpf_usuario)
        elif opcao == "3":
            if not cpf_usuario:
                print("Por favor, cadastre-se primeiro.")
            else:
                ver_desempenho(cpf_usuario)
        elif opcao == "4":
            ver_relatorios()
        elif opcao == "5":
            print("Obrigado por usar o programa da BrightBits ONG. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

    fim = time.time()  # Fim do tempo de uso
    tempo_uso = fim - inicio

    # Registrar tempo de uso
    if cpf_usuario:
        tempos = carregar_dados(TEMPO_FILE)
        if cpf_usuario not in tempos:
            tempos[cpf_usuario] = []
        tempos[cpf_usuario].append(tempo_uso)
        salvar_dados(TEMPO_FILE, tempos)

        print(f"\nVocê usou o sistema por {round(tempo_uso/60, 2)} minutos.")

# Inicia o programa
if __name__ == "__main__":
    menu_principal()
