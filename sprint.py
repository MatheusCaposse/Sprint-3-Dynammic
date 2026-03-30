# ================================
# Sprint 3 - Dynamic Programming
# ================================

# -------------------------------
# 1. RECURSÃO - Verificar duplicidade
# -------------------------------

def verificar_duplicado(leads, novo_lead, index=0):
    if index >= len(leads):
        return False

    atual = leads[index]

    if (
        atual["nome"] == novo_lead["nome"] or
        atual["cpf"] == novo_lead["cpf"] or
        atual["telefone"] == novo_lead["telefone"] or
        atual["email"] == novo_lead["email"]
    ):
        return True

    return verificar_duplicado(leads, novo_lead, index + 1)


# -------------------------------
# 2. MEMOIZAÇÃO - Evitar repetição
# -------------------------------

def verificar_duplicado_memo(leads, novo_lead, index=0, memo=None):
    if memo is None:
        memo = {}

    chave = (index, novo_lead["cpf"])

    if chave in memo:
        return memo[chave]

    if index >= len(leads):
        return False

    atual = leads[index]

    if atual["cpf"] == novo_lead["cpf"]:
        memo[chave] = True
        return True

    resultado = verificar_duplicado_memo(leads, novo_lead, index + 1, memo)
    memo[chave] = resultado
    return resultado


# -------------------------------
# 3. SUBPROBLEMAS - Otimização de agenda
# -------------------------------

def melhor_agenda(intervalos, index=0, memo=None):
    if memo is None:
        memo = {}

    if index >= len(intervalos):
        return 0

    if index in memo:
        return memo[index]

    # opção 1: pular horário
    pular = melhor_agenda(intervalos, index + 1, memo)

    # opção 2: pegar horário atual
    proximo = index + 1
    while proximo < len(intervalos) and intervalos[proximo][0] < intervalos[index][1]:
        proximo += 1

    pegar = 1 + melhor_agenda(intervalos, proximo, memo)

    memo[index] = max(pegar, pular)
    return memo[index]


# -------------------------------
# TESTES 
# -------------------------------

if __name__ == "__main__":

    # Base de leads
    leads = [
        {"nome": "João", "cpf": "123", "telefone": "111", "email": "joao@email.com"},
        {"nome": "Maria", "cpf": "456", "telefone": "222", "email": "maria@email.com"},
        {"nome": "Carlos", "cpf": "789", "telefone": "333", "email": "carlos@email.com"},
    ]

    # Novo lead
    novo_lead = {
        "nome": "João",
        "cpf": "999",
        "telefone": "444",
        "email": "novo@email.com"
    }

    print("=== Verificacao Recursiva ===")
    print("Duplicado?", verificar_duplicado(leads, novo_lead))

    print("\n=== Verificacao com Memoizacao ===")
    print("Duplicado?", verificar_duplicado_memo(leads, novo_lead))

    # Intervalos de horários (inicio, fim)
    agenda = [
        (8, 9),
        (9, 10),
        (9, 11),
        (10, 12),
        (11, 13)
    ]

    print("\n=== Melhor encaixe de horarios ===")
    print("Maximo de consultas possiveis:", melhor_agenda(agenda))