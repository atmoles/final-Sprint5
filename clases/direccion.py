class Direccion():
    def __init__(self,data):
        self.calle = data['calle']
        self.numero = data['numero']
        self.ciudad = data['ciudad']
        self.provincia = data['provincia']
        self.pais = data['pais']