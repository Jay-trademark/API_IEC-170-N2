import requests
from prettytable import PrettyTable

def obtener_user_api(url):
    tabla_usuarios = PrettyTable()
    tabla_usuarios.field_names=['N°','Nombre','Nombre Usuario','Correo','Latitud']

    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        listado_usuarios = respuesta.json()
        for usuario in listado_usuarios:
            tabla_usuarios.add_row([
                usuario['id'],
                usuario['name'],
                usuario['username'],
                usuario['email'],
                usuario['address']['geo']['lat']
            ])
        print(tabla_usuarios)

def crear_user_api(url):
    url = 'https://jsonplaceholder.typicode.com/users'
    nombre = input('Nombre:     ')
    username = input('Nombre de Usuario:    ')
    correo = input('Correo Electrónico:     ')
    numero = input('Número de Teléfono:     ')
    web = input('Sitio Web:     ')
    user = {
    'name': nombre,
    'username': username,
    'email': correo,
    'phone': numero,
    'website': web
    }

    respuesta = requests.post(url,data=user)
    print(respuesta.text)

def modificar_user_api(url):
    nombre = input('Nombre:     ')
    username = input('Nombre de Usuario:    ')
    correo = input('Correo Electrónico:     ')
    numero = input('Número de Teléfono:     ')
    web = input('Sitio Web:     ')
    user = {
    'name': nombre,
    'username': username,
    'email': correo,
    'phone': numero,
    'website': web
    }

    respuesta = requests.put(url,data=user)
    print(respuesta.text)

def eliminar_user_api(url):
    nombre = input('Nombre:     ')
    username = input('Nombre de Usuario:    ')
    correo = input('Correo Electrónico:     ')
    numero = input('Número de Teléfono:     ')
    web = input('Sitio Web:     ')
    user = {
    'name': nombre,
    'username': username,
    'email': correo,
    'phone': numero,
    'website': web
    }

    respuesta = requests.put(url,data=user)
    print(respuesta.text)
