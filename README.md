# Sprint 4 — Grafos e Algoritmo de Dijkstra no CRM Hospitalar

## Objetivo do Projeto

O objetivo deste projeto é modelar o fluxo de um sistema CRM hospitalar utilizando grafos direcionados e aplicar o algoritmo de Dijkstra para encontrar o caminho mais eficiente entre as etapas do processo.

O sistema simula o fluxo de atendimento de um lead até a confirmação final, considerando diferentes caminhos e custos operacionais para cada etapa.

---

# Tecnologias Utilizadas

* Python
* Grafos
* Algoritmo de Dijkstra
* Heapq (fila de prioridade)

---

# Estrutura do Grafo

O fluxo do CRM foi representado através de um grafo direcionado, onde:

* Cada nó representa uma etapa do CRM;
* Cada aresta representa uma conexão entre etapas;
* Cada peso representa o custo operacional daquele fluxo.

## Fluxo do Sistema

Lead
├── Cadastro
├── Atendimento WhatsApp
└── Atendimento Emergencial

Cadastro
├── Validacao Convenio
└── Triagem

Validacao Convenio
└── Triagem

Triagem
├── Consulta Clinica
└── Consulta Pediatrica

Consulta Clinica
└── Pagamento

Consulta Pediatrica
└── Pagamento

Pagamento
└── Confirmacao

---

# Algoritmo Utilizado

Foi utilizado o algoritmo de Dijkstra para encontrar o menor caminho entre:

Lead → Confirmacao

O algoritmo calcula automaticamente o fluxo de menor custo dentro do CRM utilizando fila de prioridade e análise de distâncias mínimas.

---

# Interpretação do Resultado

Após a execução do algoritmo de Dijkstra, o sistema encontrou o seguinte menor caminho:

Lead → Cadastro → Validacao Convenio → Triagem → Consulta Clinica → Pagamento → Confirmacao

## Custo Total

O custo total encontrado foi:

11

## Por que esse fluxo é mais eficiente?

O algoritmo analisou todos os caminhos disponíveis dentro do CRM hospitalar e identificou que esse fluxo possui o menor custo operacional.

Fluxos alternativos, como Atendimento WhatsApp e Atendimento Emergencial, possuem pesos maiores, tornando o processo menos eficiente.

O caminho encontrado reduz:

* tempo de processamento;
* quantidade de etapas críticas;
* custo operacional;
* esforço necessário para concluir o atendimento.

Dessa forma, o algoritmo de Dijkstra permite identificar automaticamente o fluxo mais otimizado para transformar um lead em uma confirmação final dentro do sistema CRM.

---

# Como Executar o Projeto

## Clonar o repositório

git clone https://github.com/MatheusCaposse/Sprint-3-Dynammic.git

---

## Executar o projeto

python main.py

---

# Estrutura do Projeto

Sprint4/
│
├── sprint.py
├── README.md

---

# Grupo

Matheus Machado Caposse
Caio Berardo
Vitor de Lima
Giovanni
