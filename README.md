CRM Hospital São Rafael - Sprint 3 (Dynamic Programming)

## Descrição do Projeto

Este projeto faz parte do desenvolvimento de um sistema CRM hospitalar, com foco na aplicação de técnicas de **Programação Dinâmica**, incluindo **recursão**, **memoização** e **resolução de subproblemas**.

O objetivo é otimizar processos internos do sistema, como verificação de duplicidade de cadastros e organização de horários de atendimento.

---

## Objetivo

Modelar e implementar soluções eficientes para:

- Verificar duplicidade de leads/cadastros
- Evitar processamento repetido
- Otimizar o uso de horários disponíveis

---

## Funcionalidades

### 1. Verificação Recursiva de Duplicidade
Função que percorre uma lista de leads e verifica se um novo cadastro já existe, comparando dados como:

- Nome
- CPF
- Telefone
- Email

---

###  2. Memoização (Otimização)
Utilização de cache para evitar repetir comparações já realizadas, melhorando a performance do sistema.

---

### 3. Otimização de Agenda (Subproblemas)
Algoritmo que encontra a melhor combinação de horários disponíveis para consultas, evitando conflitos e maximizando o número de atendimentos.

---

## Conceitos Utilizados

- Recursão
- Memoização
- Programação Dinâmica
- Divisão em Subproblemas

---

## Exemplo de Execução

O sistema simula:

- Uma base de leads cadastrados
- Um novo lead sendo inserido
- Verificação de duplicidade
- Organização de horários disponíveis

---

## Estrutura do Projeto

- Sprint.py

## Como Executar

1. Instale o Python (caso não tenha)
2. Clone o repositório
3. Rode o codigo em uma IDE

## Integrantes

Matheus Machado Caposse
Caio Berardo
Vitor de Lima
Giovanni
