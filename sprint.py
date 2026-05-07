import heapq

# ==================================================
# SPRINT 4 - GRAFOS E ALGORITMO DE DIJKSTRA
# Sistema CRM Hospitalar
# ==================================================

# --------------------------------------------------
# GRAFO DIRECIONADO DO CRM
# Cada conexão possui um custo operacional
# --------------------------------------------------

grafo = {

    "Lead": {
        "Cadastro": 2,
        "Atendimento WhatsApp": 5,
        "Atendimento Emergencial": 8
    },

    "Cadastro": {
        "Validacao Convenio": 2,
        "Triagem": 4
    },

    "Validacao Convenio": {
        "Triagem": 1
    },

    "Atendimento WhatsApp": {
        "Triagem": 3
    },

    "Atendimento Emergencial": {
        "Consulta Clinica": 2
    },

    "Triagem": {
        "Consulta Clinica": 3,
        "Consulta Pediatrica": 4
    },

    "Consulta Clinica": {
        "Pagamento": 2
    },

    "Consulta Pediatrica": {
        "Pagamento": 3
    },

    "Pagamento": {
        "Confirmacao": 1
    },

    "Confirmacao": {}
}


# --------------------------------------------------
# ALGORITMO DE DIJKSTRA
# Encontra o menor caminho entre dois nós
# --------------------------------------------------

def dijkstra(grafo, inicio, fim):

    # Fila de prioridade
    fila = [(0, inicio)]

    # Armazena as menores distâncias
    distancias = {
        no: float('inf') for no in grafo
    }

    # Nó inicial começa com custo 0
    distancias[inicio] = 0

    # Armazena o caminho percorrido
    predecessores = {}

    # Nós já visitados
    visitados = set()

    while fila:

        # Remove o nó com menor custo
        custo_atual, no_atual = heapq.heappop(fila)

        # Evita processamento repetido
        if no_atual in visitados:
            continue

        visitados.add(no_atual)

        # Percorre os vizinhos do nó atual
        for vizinho, peso in grafo[no_atual].items():

            novo_custo = custo_atual + peso

            # Atualiza se encontrar caminho menor
            if novo_custo < distancias[vizinho]:

                distancias[vizinho] = novo_custo

                predecessores[vizinho] = no_atual

                heapq.heappush(fila, (novo_custo, vizinho))

    # --------------------------------------------------
    # Reconstrução do caminho
    # --------------------------------------------------

    caminho = []

    atual = fim

    while atual in predecessores:

        caminho.insert(0, atual)

        atual = predecessores[atual]

    caminho.insert(0, inicio)

    return caminho, distancias[fim], distancias


# --------------------------------------------------
# EXECUÇÃO PRINCIPAL
# --------------------------------------------------

if __name__ == "__main__":

    caminho, custo, distancias = dijkstra(
        grafo,
        "Lead",
        "Confirmacao"
    )

    print("=" * 60)
    print(" SISTEMA CRM HOSPITALAR - ALGORITMO DE DIJKSTRA ")
    print("=" * 60)

    print("\nFluxo mais eficiente encontrado:\n")

    print(" -> ".join(caminho))

    print(f"\nCusto total do fluxo: {custo}")

    # --------------------------------------------------
    # Exibição das distâncias mínimas
    # --------------------------------------------------

    print("\n" + "=" * 60)
    print(" DISTANCIAS MINIMAS A PARTIR DO LEAD ")
    print("=" * 60)

    for no, distancia in distancias.items():

        print(f"{no}: {distancia}")

    # --------------------------------------------------
    # Interpretação do resultado
    # --------------------------------------------------

    print("\n\n\n\n" + "=" * 60)
    print(" INTERPRETACAO DO RESULTADO ")
    print("=" * 60)

    print("""
O algoritmo de Dijkstra encontrou o caminho mais eficiente
entre Lead e Confirmacao.

Fluxo encontrado:
Lead -> Cadastro -> Validacao Convenio -> Triagem
-> Consulta Clinica -> Pagamento -> Confirmacao

Esse caminho possui o menor custo operacional dentro do CRM.

O custo total foi calculado somando os pesos de cada etapa,
resultando em um fluxo mais rápido e eficiente para o hospital.

Fluxos alternativos, como Atendimento Emergencial ou
Atendimento WhatsApp, possuem custos maiores, tornando-se
menos eficientes segundo a análise do algoritmo.
""")