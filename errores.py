from clases.razones import Razon
class Buscador():
    razones = []
    def __init__(self,eventos,cliente):
        self.eventos = [ x for x in eventos if x['estado']== 'RECHAZADA']
        for evento in eventos:
            if evento['estado'] == 'ACEPTADA':
                self.razones.append({'Fecha ': evento['fecha'],'Tipo ': evento["tipo"],'Estado ': evento["estado"], 'Monto' : evento["monto"],'Razon': ""})
                continue    
            self.buscar(evento,cliente)
            
    
    def buscar(self,error,cliente):

        for razon in Razon.__subclasses__():
            resul = razon(error).resolver(cliente,error)

            if resul['error']:
                self.razones.append({'Fecha ': error['fecha'],'Tipo ': error["tipo"],'Estado ': error["estado"], 'Monto' : error["monto"],'Razon': resul['mensaje']})
                break
