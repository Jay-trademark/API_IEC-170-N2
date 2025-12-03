import requests
from prettytable import PrettyTable

def obtener_user_api(url):
    id == 0
    url == (f'https://jsonplaceholder.typicode.com/users/{id}')


def obtener_usuarios_api(url):
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

def obtener_posts_api(url):
    tabla_posts = PrettyTable()
    tabla_posts.field_names=['N°','Autor','Titulo','Contenido']

    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        listado_posts = respuesta.json()
        for post in listado_posts:
            tabla_posts.add_row([
                post['id'],
                post['userId'],
                post['title'],
                post['body']
            ])
        print(tabla_posts)

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

def guardar_user_api():
    pass

def modificar_user_api():
    pass

def eliminar_user_api():
    pass


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
