import parseador
import errores

data = parseador.Parser('eventos_classic.json')
error = errores.Buscador(data.eventos)
# print(data.eventos_black)
# print(data.cliente.direccion.pais)
