from abc import ABC, abstractmethod

# --- PADRÃO DE PROJETO: STRATEGY ---
# A regra de negócio foi separada em classes de estratégia específicas.

# Strategy (Interface)
class EstrategiaAtaque(ABC):
    @abstractmethod
    def calcular_dano(self, forca_base: int) -> int:
        pass

# Concrete Strategies
class AtaqueCavaleiro(EstrategiaAtaque):
    def calcular_dano(self, forca_base: int) -> int:
        return forca_base + 5

class AtaqueExplorador(EstrategiaAtaque):
    def calcular_dano(self, forca_base: int) -> int:
        return forca_base * 2

class AtaqueSacerdote(EstrategiaAtaque):
    def calcular_dano(self, forca_base: int) -> int:
        return forca_base + 2

# Context
class Personagem:
    def __init__(self, estrategia_ataque: EstrategiaAtaque):
        self.estrategia_ataque = estrategia_ataque

    def atacar(self, forca_base: int) -> int:
        return self.estrategia_ataque.calcular_dano(forca_base)


"""
--- AUTOAVALIAÇÃO ---
Autoavaliação: Acabou que as fases de RED e GREEN foram mais demorados do que eu coloquei no plano, já a refatoração
foi mais rápida do que o planejado, usei mais IA para fazer a refatoração e também já tinha entendido melhor como fazer,
mas mesmo assim foi dificil, tentei me manter dentro dos 120 minutos estipulados e consegui ficar dentro do tempo.
Critérios atingidos: Os testes foram criados em arquivo separado. O histórico conta com três commits demarcando as
fases red, green e refactor. O commit vermelho subiu apenas os testes falhos. Apliquei o padrão de projeto Strategy,
com os participantes devidamente nomeados, e todos os testes passaram na verificação final.
O que mudou na estrutura Green vs Refactor: Na fase Verde, a classe Personagem violava o princípio Aberto/Fechado
(OCP), pois usava uma cadeia de ifs baseados no tipo do objeto para calcular o dano. Na refatoração, extraí a lógica
matemática para as classes concretas de Strategy AtaqueCavaleiro, AtaqueExplorador e AtaqueSacerdote. A classe
Personagem agora apenas delega a execução para a interface.
Maior dificuldade: A parte que deu mais trabalho foi adequar a tipagem estática e as importações abstratas (ABC) do
Python para garantir que a interface fosse respeitada sem quebrar os testes originais.
Uso de IA: A inteligência artificial ajudou a formatar a autoavaliação e a modularizar a aplicação do padrão Strategy
de forma rápida para não estourar o tempo de 120 minutos da atividade.
----------------------------------
"""
