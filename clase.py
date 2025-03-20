class Conta:
    numero = 000000
    saldo = 0.0
    
    def deposito (self,valor):
        self.saldo += valor
    
    def saque (self,valor):
      if  (self.saldo > 0 ):
          self.saldo -= valor
      else:
          print("Saldo Insuficiente")
    
    
objConta=Conta()
objConta.saldo = 20
objConta.numero = "13131-2"
objConta.deposito = input()
print("saldo da conta: ",objConta.saldo)
print("Numero da conta: ",objConta.numero)