class AtaqueCavaleiro: pass
class AtaqueExplorador: pass
class AtaqueSacerdote: pass

class Personagem:
    def __init__(self, tipo_ataque):
        self.tipo_ataque = tipo_ataque

    def atacar(self, forca_base: int) -> int:
        # Implementação "suja" apenas para o teste passar (Fase Verde)
        if isinstance(self.tipo_ataque, AtaqueCavaleiro):
            return forca_base + 5
        elif isinstance(self.tipo_ataque, AtaqueExplorador):
            return forca_base * 2
        elif isinstance(self.tipo_ataque, AtaqueSacerdote):
            return forca_base + 2
        return forca_base
