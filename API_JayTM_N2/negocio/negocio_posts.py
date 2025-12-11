import requests
from prettytable import PrettyTable

#   POSTS
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


def crear_post_api(url):
    url = 'https://jsonplaceholder.typicode.com/posts'
    userid = '1'
    titulo = input('Titulo:    ')
    cuerpo = input('Contenido:     ')
    post = {
    'userid': userid,
    'title': titulo,
    'body': cuerpo
    }

    respuesta = requests.post(url,data=post)
    print(respuesta.text)

def modificar_post_api(url):
    url = 'https://jsonplaceholder.typicode.com/posts/101'
    userid = '1'
    titulo = input('Titulo:    ')
    cuerpo = input('Contenido:     ')
    post = {
    'userid': userid,
    'title': titulo,
    'body': cuerpo
    }

    respuesta = requests.put(url,data=post)
    print(respuesta.text)

def eliminar_post_api(url):
    url = 'https://jsonplaceholder.typicode.com/posts/101'
    respuesta = requests.delete(url)
    print(respuesta.text)