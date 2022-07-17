class Razon():
    def __init__(self,error):
        self.tipo = error['tipo']

    def resolver(self,cliente,error):
        return {'error':False,'mensaje':''}
        
class RazonSaldoSuficiente(Razon):
    
    def resolver(self,cliente,error):
        res = (error["saldoEnCuenta"] >= error["monto"]) if self.tipo != 'TRANSFERENCIA_RECIBIDA' else True
        return {"error": not res ,"mensaje": "Saldo insuficiente en la cuenta" if not res else ""}
    
    

class RazonAltaChequera(Razon):
    
    def resolver(self,cliente,error):
        print(self.tipo)
        res = cliente.puede_crear_chequera(error["totalChequerasActualmente"]) if self.tipo == 'ALTA_CHEQUERA' else True
        return {"error": not res ,"mensaje": "Ya tiene el cupo de chequeras disponibles" if not res else ""}
    
    
class RazonAltaTarjetaCredito(Razon):
    
    def resolver(self,cliente,error):
        res = cliente.puede_crear_tarjeta_credito(error["totalTarjetasDeCreditoActualmente"]) if self.tipo == "ALTA_TARJETA_CREDITO" else True
        return {"error": not res ,"mensaje": "Ya tiene el cupo de tarjetas de credito disponibles" if not res else ""}

class RazonCompraDolar(Razon):
        
    def resolver(self,cliente,error):
        res = cliente.puede_comprar_dolar() if self.tipo == 'COMPRA_DOLAR' else True
        return {"error": not res ,"mensaje": "No tiene caja de ahorro en dolares" if not res else ""}

class RazonRetiroEfectivo(Razon):
        
        def resolver(self,cliente,error):
            res = error["cupoDiarioRestante"] >= error["monto"] if self.tipo == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO' else True
            return {"error": not res ,"mensaje": "${} es superior al cupo que resta del dia que es ${}".format(error["monto"],error["cupoDiarioRestante"]) if not res else ""}

class RazonTransferenciaEnviada(Razon):
            
        def resolver(self,cliente,error):
            errorTranferencia = error["saldoEnCuenta"] < error["monto"] * cliente.cuentas[0].costo_transferencias
            res = errorTranferencia if self.tipo == 'TRANSFERENCIA_ENVIADA' else True
            return {"error": not res ,"mensaje": f"Saldo insuficiente para cubrir la comision de {cliente.cuentas[0].costo_transferencias}" if not res else ""}

class RazonTransferenciaRecibida(Razon):
    
    def resolver(self,cliente,error):
        res = error["monto"] < cliente.cuentas[0].limite_transferencia_recibida if self.tipo == 'TRANSFERENCIA_RECIBIDA' else True
        return {"error": not res ,"mensaje": "La tranferencia excede el limite para el tipo de cuenta" if not res else ""}
