from Cuenta import Cuenta_Bancaria

class CuentaCorriente (Cuenta_Bancaria):

    def __init__(self, numero= None, nombrepropietario= None, saldo:float= 0, tiene_cheque=bool):
        self._tiene_cheque= tiene_cheque
        super(CuentaCorriente, self).__init__(numero=numero, nombrepropietario=nombrepropietario, saldo=saldo)

    @property
    def cheque(self):
        return self._cheque

    @cheque.setter
    def cheque(self, cheque):
        self._cheque = cheque
        return self._saldo

    def pagar_cheque(self):
        self._saldo = self._saldo + ((float (self._saldo) - int (self._pagar_cheque)))
        return self._saldo

if __name__=='__main__':
    CuentaCorriente = CuentaCorriente('0909272878', 'LUCAS', '260', bool)

    CuentaCorriente.mostrar_saldo()
    CuentaCorriente.credito(1400)

    CuentaCorriente.mostrar_saldo()
    CuentaCorriente.debito(30)

    print(CuentaCorriente)