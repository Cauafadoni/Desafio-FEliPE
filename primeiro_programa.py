
import datetime

estoque = {}  # Dicionário para armazenar as peças em estoque
vendas = []   # Lista para armazenar as vendas realizadas

def cadastrar_peca(codigo, descricao, preco, quantidade):
    """Cadastra uma nova peça no estoque."""
    estoque[codigo] = {
        "descricao": descricao,
        "preco": preco,
        "quantidade": quantidade,
    }
    print(f"Peça {descricao} cadastrada com sucesso!")

def alterar_peca(codigo, descricao=None, preco=None, quantidade=None):
    """Altera os dados de uma peça no estoque."""
    if codigo in estoque:
        if descricao:
            estoque[codigo]["descricao"] = descricao
        if preco:
            estoque[codigo]["preco"] = preco
        if quantidade:
            estoque[codigo]["quantidade"] = quantidade
        print(f"Peça {estoque[codigo]['descricao']} alterada com sucesso!")
    else:
        print("Peça não encontrada.")

def excluir_peca(codigo):
    """Exclui uma peça do estoque."""
    if codigo in estoque:
        del estoque[codigo]
        print("Peça excluída com sucesso!")
    else:
        print("Peça não encontrada.")

def realizar_venda(codigo, quantidade):
    """Realiza uma venda de uma peça."""
    if codigo in estoque:
        if estoque[codigo]["quantidade"] >= quantidade:
            estoque[codigo]["quantidade"] -= quantidade
            preco_unitario = estoque[codigo]["preco"]
            preco_total = preco_unitario * quantidade
            desconto = preco_total * 0.05
            preco_final = preco_total - desconto

            venda = {
                "codigo": codigo,
                "descricao": estoque[codigo]["descricao"],
                "quantidade": quantidade,
                "preco_unitario": preco_unitario,
                "preco_total": preco_total,
                "desconto": desconto,
                "preco_final": preco_final,
                "data": datetime.datetime.now(),
            }
            vendas.append(venda)

            print(f"Venda realizada com sucesso!")
            print(f"Valor sem desconto: R$ {preco_total:.2f}")
            print(f"Valor com desconto: R$ {preco_final:.2f}")
        else:
            print("Quantidade insuficiente em estoque.")
    else:
        print("Peça não encontrada.")

def mostrar_estoque():
    """Mostra o estoque total."""
    total_itens = sum(item["quantidade"] for item in estoque.values())
    print(f"Estoque total: {total_itens} itens")

def calcular_total_vendas():
    """Calcula o total de vendas e média por dia."""
    total_vendas = len(vendas)
    if total_vendas > 0:
        primeira_venda = vendas[0]["data"]
        ultima_venda = vendas[-1]["data"]
        dias_venda = (ultima_venda - primeira_venda).days + 1
        vendas_por_dia = total_vendas / dias_venda
        print(f"Total de vendas: {total_vendas}")
        print(f"Média de vendas por dia: {vendas_por_dia:.2f}")
    else:
        print("Nenhuma venda realizada.")

def calcular_vendas_por_periodo(periodo):
    """Calcula o total de vendas por período (dia, semana, mês, ano)."""
    hoje = datetime.datetime.now()
    if periodo == "dia":
        vendas_periodo = [venda for venda in vendas if venda["data"].date() == hoje.date()]
    elif periodo == "semana":
        inicio_semana = hoje - datetime.timedelta(days=hoje.weekday())
        vendas_periodo = [venda for venda in vendas if venda["data"].date() >= inicio_semana.date()]
    elif periodo == "mes":
        vendas_periodo = [venda for venda in vendas if venda["data"].month == hoje.month]
    elif periodo == "ano":
        vendas_periodo = [venda for venda in vendas if venda["data"].year == hoje.year]
    else:
        print("Período inválido.")
        return

    print(f"Vendas no {periodo}: {len(vendas_periodo)}")

# Exemplos de uso
cadastrar_peca("123", "Filtro de óleo", 25.00, 10)
cadastrar_peca("456", "Pastilha de freio", 50.00, 5)
realizar_venda("123", 2)
alterar_peca("456", preco=55.00)
excluir_peca("123")
mostrar_estoque()
calcular_total_vendas()
calcular_vendas_por_periodo("dia")
calcular_vendas_por_periodo("semana")
calcular_vendas_por_periodo("mes")
calcular_vendas_por_periodo("ano")