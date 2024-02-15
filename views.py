from utils import load_data, load_template, send_data, build_response
from urllib.parse import unquote_plus


def index(request):

    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
     
        for chave_valor in corpo.split('&'):
            chave, valor = chave_valor.split('=')
            valor_decodificado = unquote_plus(valor)
            params[chave] = valor_decodificado

        send_data(params)
        
    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    if request.startswith('POST'):
            return build_response(code=303, reason='See Other', headers='Location: /',body=load_template('index.html').format(notes=notes)) 

    return build_response(body=load_template('index.html').format(notes=notes)) 