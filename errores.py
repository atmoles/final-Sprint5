from clases.cliente import Cliente
import parseador
import clases.razones
class Buscador():
    def __init__(self,eventos,cliente):
        self.errores = [ x for x in eventos if x['estado']== 'RECHAZADA']
        # for x in self.errores:
        #     if(x["tipo"] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO"):
        #         self.razon = clases.razones.RazonRetiroEfectivo()
                # self.razon.resolver(parseador.cliente)
            
        # print(self.errores)
        # print(cliente["tipo"])