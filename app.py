import parseador
import errores
import reporte

data = parseador.Parser('eventos_gold.json')
razon = errores.Buscador(data.eventos,data.cliente)

html = reporte.GetHTML(razon.razones,data.cliente)
html.get_html()
