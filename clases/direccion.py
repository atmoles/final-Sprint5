class Direccion():
    def __init__(self,data):
        self.calle = data['calle']
        self.numero = data['numero']
        self.ciudad = data['ciudad']
        self.provincia = data['provincia']
        self.pais = data['pais']
    
    def get_direccion(self):
        return self.calle + ' ' + self.numero + ' ' + self.ciudad
