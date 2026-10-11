"""
--- PLANO de 10 minutos ---
Problema: Calcular o dano de ataque para diferentes classes de um RPG, Cavaleiro, Explorador e Sacerdote.
Casos de teste: 
1. Dano do Cavaleiro: Força base + bônus de armadura pesada.
2. Dano do Explorador: Força base * multiplicador de velocidade.
3. Dano do Sacerdote: Força base + bônus de luz.
Padrão de Projeto: Strategy. Escolhi este padrão porque a regra de cálculo de dano varia totalmente dependendo
da classe do personagem, permitindo isolar cada algoritmo.
Tempo estimado: 20 min para fazer o RED, 20 min para fazer o GREEN e 60 min para REFACTOR.
Uso de IA: Usei para fazer os testes em pytest, simular o domínio do RPG e organizar as mensagens de
commit conforme a regra do TDD.
--------------------------
"""
import pytest
from personagem import Personagem, AtaqueCavaleiro, AtaqueExplorador, AtaqueSacerdote

def test_ataque_cavaleiro():
    personagem = Personagem(AtaqueCavaleiro())
    dano = personagem.atacar(forca_base=10)
    assert dano == 15  # 10 + 5

def test_ataque_explorador():
    personagem = Personagem(AtaqueExplorador())
    dano = personagem.atacar(forca_base=10)
    assert dano == 20  # 10 * 2

def test_ataque_sacerdote():
    personagem = Personagem(AtaqueSacerdote())
    dano = personagem.atacar(forca_base=10)
    assert dano == 12  # 10 + 2
