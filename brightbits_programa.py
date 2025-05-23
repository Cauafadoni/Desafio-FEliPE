# Programa Educativo - BrightBits ONG

import json
import os
import time
from datetime import datetime

# Arquivos usados
DADOS_FILE = "usuarios.json"
ACESSOS_FILE = "acessos.json"
TEMPO_FILE = "tempos.json"

def carregar_dados(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def salvar_dados(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def boas_vindas():
    print("========================================")
    print(" Bem-vindo(a) ao Programa BrightBits ONG")
    print("========================================\n")
    print("Nosso objetivo é te ensinar o básico de lógica de programação")
    print("e também como se proteger na internet!\n")

def coletar_dados():
    print("\nAntes de começarmos, precisamos de algumas informações básicas.")
    print("Atenção: Seus dados serão usados apenas para fins educativos.\n")

    nome = input("Digite seu primeiro nome: ")
    idade = int(input("Digite sua idade: "))

    # Salvar idade no banco de dados
    dados = carregar_dados(DADOS_FILE)
    dados[nome] = {"idade": idade}
    salvar_dados(DADOS_FILE, dados)

    # Registrar acesso por data
    acessos = carregar_dados(ACESSOS_FILE)
    hoje = datetime.now().strftime("%Y-%m-%d")
    if hoje not in acessos:
        acessos[hoje] = []
    acessos[hoje].append(nome)
    salvar_dados(ACESSOS_FILE, acessos)

    print(f"\nOlá, {nome}! Vamos aprender juntos.\n")
    return nome

def aula_logica():
    print("===== Aula 1: Conceitos Básicos de Lógica de Programação =====\n")
    print("Em programação, usamos variáveis para guardar informações.")
    print("Exemplo:")
    print("nome = 'Ricardo'")
    print("idade = 22\n")

    print("Vamos fazer um pequeno teste com você!")

    resposta = input("Se idade = 17, essa pessoa é maior de idade? (sim/não): ").lower()
    if resposta == "não":
        print("Correto! Uma pessoa com 17 anos ainda não é maior de idade.\n")
    else:
        print("Ops, cuidado! A maioridade começa aos 18 anos.\n")

def aula_seguranca():
    print("===== Aula 2: Segurança na Internet =====\n")
    print("Dicas importantes:")
    print("- Nunca compartilhe sua senha com outras pessoas.")
    print("- Use senhas fortes: combine letras, números e símbolos.")
    print("- Desconfie de links suspeitos.")
    print("- Proteja seus dados pessoais.\n")

    senha_segura = input("Digite uma senha segura para praticar (ela não será armazenada): ")
    if len(senha_segura) >= 8:
        print("Boa! Sua senha tem um tamanho adequado.")
    else:
        print("Dica: Tente usar uma senha com pelo menos 8 caracteres.\n")

def encerrar(nome, tempo_total):
    print(f"\nParabéns, {nome}! Você deu os primeiros passos na programação e segurança digital.")
    print("Continue praticando e nunca pare de aprender!")
    print("\n--- BrightBits ONG ---")

    # Salvar tempo de uso
    tempos = carregar_dados(TEMPO_FILE)
    if nome not in tempos:
        tempos[nome] = []
    tempos[nome].append(tempo_total)
    salvar_dados(TEMPO_FILE, tempos)

    print(f"\nVocê usou o programa por {round(tempo_total/60, 2)} minutos.")

def ver_relatorios():
    print("\n=== Relatórios da Plataforma ===")

    # Acessos por dia
    acessos = carregar_dados(ACESSOS_FILE)
    print("\nAcessos por dia:")
    for data, lista in acessos.items():
        print(f"- {data}: {len(lista)} acesso(s)")

    # Média de idade
    dados = carregar_dados(DADOS_FILE)
    if dados:
        idades = [info["idade"] for info in dados.values()]
        media_idade = sum(idades) / len(idades)
        print(f"\nMédia de idade dos usuários: {round(media_idade, 2)} anos")
    else:
        print("\nNenhum dado de idade disponível.")

    # Tempo médio de uso
    tempos = carregar_dados(TEMPO_FILE)
    todos_tempos = [t for lista in tempos.values() for t in lista]
    if todos_tempos:
        media_tempo = sum(todos_tempos) / len(todos_tempos)
        print(f"Tempo médio de uso: {round(media_tempo / 60, 2)} minutos\n")
    else:
        print("Nenhum tempo de uso registrado ainda.\n")

# Execução principal
def main():
    inicio = time.time()
    boas_vindas()
    nome_usuario = coletar_dados()
    aula_logica()
    aula_seguranca()
    fim = time.time()
    tempo_total = fim - inicio
    encerrar(nome_usuario, tempo_total)

    ver_mais = input("\nDeseja ver os relatórios da plataforma? (s/n): ").lower()
    if ver_mais == "s":
        ver_relatorios()

if __name__ == "__main__":
    main()
