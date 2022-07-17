import json
from clases import cliente
from clases import direccion
from clases import cuenta
# lo q hace esta clase es parsearme el json para que lo pueda usar 
class Parser():
    #creo el constructor
    def __init__(self,file):
        self.file=file
        #se ejecuta este metodo q defino para levantar el json
        self.load()
        self.get_cliente()
        self.eventos = self.data['transacciones']
        # metodo para levantar el json,obtngo el diccionario parseado
        
    def load(self):
        f=open(self.file)
        self.data=json.load(f)
        f.close()
    
    def get_cliente(self):
        if self.data['tipo'] == 'BLACK':
            self.cliente=cliente.ClienteBlack(self.data)
            self.cliente.crear_cuenta(cuenta.caja_de_ahorro_p)
            self.cliente.crear_cuenta(cuenta.caja_de_ahorro_d)
            self.cliente.crear_cuenta(cuenta.cuenta_corriente)
        elif self.data['tipo'] == 'GOLD':
            self.cliente=cliente.ClienteGold(self.data)
            self.cliente.crear_cuenta(cuenta.caja_de_ahorro_p)
            self.cliente.crear_cuenta(cuenta.caja_de_ahorro_d)
        else:
            self.cliente=cliente.ClienteClassic(self.data)
            self.cliente.crear_cuenta(cuenta.caja_de_ahorro_p)

 
