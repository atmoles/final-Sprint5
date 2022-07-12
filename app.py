import parseador
import errores

data = parseador.Parser('eventos_classic.json')
error = errores.Buscador(data.eventos_classic)
# print(data.eventos_black)
