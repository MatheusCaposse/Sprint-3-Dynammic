import heapq

grafo = {
    "Lead": {
        "Cadastro": 2,
        "Contato": 5
    },

    "Cadastro": {
        "Triagem": 2
    },

    "Contato": {
        "Consulta": 4
    },

    "Triagem": {
        "Consulta": 1
    },

    "Consulta": {
        "Confirmacao": 3
    },

    "Confirmacao": {}
}


def dijkstra(grafo, inicio, fim):

    fila = [(0, inicio)]

    distancias = {
        no: float('inf') for no in grafo
    }

    distancias[inicio] = 0

    caminhos = {
        inicio: []
    }

    while fila:

        custo_atual, no_atual = heapq.heappop(fila)

        if no_atual == fim:
            return caminhos[no_atual] + [fim], custo_atual

        for vizinho, peso in grafo[no_atual].items():

            novo_custo = custo_atual + peso

            if novo_custo < distancias[vizinho]:

                distancias[vizinho] = novo_custo

                caminhos[vizinho] = caminhos[no_atual] + [no_atual]

                heapq.heappush(fila, (novo_custo, vizinho))

    return None


if __name__ == "__main__":

    caminho, custo = dijkstra(
        grafo,
        "Lead",
        "Confirmacao"
    )

    print("Menor caminho encontrado:")
    print(" -> ".join(caminho))

    print("\nCusto total:")
    print(custo)