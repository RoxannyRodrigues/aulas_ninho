class Conta:

    def __init__(self, titular, salvo):
        self._titular = titular
        self._salvo = salvo

        def get_saldo(self):
            return self.__saldo
        
        def set_saldo(self,saldo):
            self._saldo = saldo
        
        def get_titular(self):
            return self.titular
        
        def set_titular(self,titular):
            return self._titular
        
        def set_titular (self,titular):
            self._titular = titular

conta1 = Conta("João", 300)

print(conta1.getSaldo())
print(conta1.getTitular())

conta1.setSaldo(500)
conta1.setTitular("Maria")

print(conta1.getSaldo())
print(conta1.getTitular())



