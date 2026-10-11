Este repositório contém a entrega da atividade prática sobre o ciclo TDD (Test-Driven Development) da disciplina de Engenharia de Software.

## 🎯 Objetivo do Protótipo
O código implementa um sistema simples de cálculo de dano para um RPG, focado em três classes diferentes: **Cavaleiro**, **Explorador** e **Sacerdote**. A regra de negócio varia para cada classe, o que justifica a escolha do domínio para aplicar a refatoração.

## 🔄 Fases do Ciclo TDD Aplicadas
O histórico de commits documenta o processo passo a passo:
1. **Red:** Criação de `test_personagem.py` com os testes falhando (ausência de código de produção).
2. **Green:** Criação de `personagem.py` com uma lógica provisória e direta (uso de `ifs`) apenas para fazer os testes passarem.
3. **Refactor:** Reestruturação do código de produção aplicando o Padrão de Projeto **Strategy**, isolando cada algoritmo de ataque em sua própria classe concreta (`AtaqueCavaleiro`, `AtaqueExplorador`, `AtaqueSacerdote`), mantendo os testes 100% funcionais.

## 🚀 Como Executar
O projeto utiliza a biblioteca `pytest` para a execução dos testes automatizados. 
Para rodar a suíte de testes localmente, certifique-se de ter o Python e o pytest instalados, e execute o comando abaixo no terminal:

```bash
pytest test_personagem.py
