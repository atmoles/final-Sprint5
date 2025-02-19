from clases.cuenta import Cuenta
from clases.direccion import Direccion

class Cliente:
    def __init__(self,data):
        self.tipo=data['tipo']
        self.dni=data['dni']
        self.nombre=data['nombre']
        self.apellido=data['apellido']
        self.direccion = Direccion(data['direccion'])
        print('Se creo cliente: '+self.dni)
        
    def baja(self):
        self.tipo='baja'

class ClienteClassic(Cliente):
    def puede_comprar_dolar(self):
        return False
    def puede_crear_chequera(self):
        return False
    def puede_crear_tarjeta_credito(self):
        return False 
    
    def __init__(self, data):
        print('Se creo classic')
        super().__init__(data) 
        self.caja_de_ahorro = Cuenta(10000,150000,0,0.01,0)
        print(self.caja_de_ahorro)

class ClienteGold(Cliente):
    def puede_comprar_dolar(self):
        return True
    def puede_crear_chequera(self):
        return True
    def puede_crear_tarjeta_credito(self):
        return True 
    def __init__(self, data):
        print('Se creo gold')  
        super().__init__(data)
        self.max_credito = 1
        self.max_chequera = 1
        self.cuenta_corriente = Cuenta(20000,500000,0,0.005,10000)
        self.caja_de_ahorro_d = Cuenta(20000,500000,0,0.005,0)




class ClienteBlack(Cliente):
    def puede_comprar_dolar(self):
        return True
    def puede_crear_chequera(self):
        return True
    def puede_crear_tarjeta_credito(self):
        return True 
    def __init__(self, data):
        print('Se creo black')
        super().__init__(data)
        self.max_credito = 5
        self.max_chequera = 2
        self.cuenta_corriente = Cuenta(100000,0,0,0,10000)
        self.caja_de_ahorro_d = Cuenta(100000,0,0,0,0)
        self.caja_de_ahorro_p = Cuenta(100000,0,0,0,0)


