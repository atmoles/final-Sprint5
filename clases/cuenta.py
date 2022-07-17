class Cuenta():
    def __init__(self,limite_extraccion_diario,limite_transferencia_recibida,monto  ,costo_transferencias ,saldo_descubierto_disponible  ):
        self.limite_extraccion_diario = limite_extraccion_diario
        self.limite_transferencia_recibida = limite_transferencia_recibida 
        self.monto = monto 
        self.costo_transferencias = costo_transferencias 
        self.saldo_descubierto_disponible = saldo_descubierto_disponible

caja_de_ahorro_p = Cuenta(10000,150000,-1,0.01,0)
caja_de_ahorro_d = Cuenta(15000,150000,-1,-1,0)
cuenta_corriente = Cuenta(20000,150000,-1,-1,0)
