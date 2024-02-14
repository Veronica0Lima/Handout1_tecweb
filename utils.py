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
