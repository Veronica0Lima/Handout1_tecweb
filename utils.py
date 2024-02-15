import json
from pathlib import Path

def extract_route(request):
    fi = request.find(' ')
    si = request.find(' ', fi + 1)
    route = request[fi + 2:si]
    return route

def read_file(path):
    file = open(path, 'rb')
    content = file.read()
    file.close()
    return content

def load_data(archive):
    path = './data/' + archive
    file = open(path, 'r')
    content = file.read()
    content = json.loads(content)
    file.close()
    return content 

def load_template(name):
    path = './templates/' + name
    file = open(path, 'r')
    content = file.read()
    file.close()
    return content 

def send_data(parametros):
    # path = './data/notes.json'
    # file = open(path, 'r')
    # content0 = file.read()
    # content0 = json.loads(content0)
    # file.close()

    # content0.append(dic)

    # file = open(path, 'w')
    # file.write(json.dumps(content0))
    # file.close()

    with open(f'./data/notes.json', 'r') as arquivo:
        notas = json.load(arquivo)
    notas.append(parametros)
    with open(f'./data/notes.json', 'w') as arquivo:
        json.dump(notas, arquivo, indent=2)

def build_response(body='', code=200, reason="OK", headers=''):
    if len(headers) > 0:
        return "HTTP/1.1 {} {}\n{}\n\n{}". format(code, reason, headers, body).encode()
    return "HTTP/1.1 {} {}\n\n{}". format(code, reason, body).encode()