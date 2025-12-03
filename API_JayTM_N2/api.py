from negocio.negocio_users import obtener_posts_api, obtener_usuarios_api, crear_user_api, modificar_user_api, eliminar_user_api
url = 'https://jsonplaceholder.typicode.com/users'
url2 = 'https://jsonplaceholder.typicode.com/users/1'

menu = True
while menu:
    print('\n=====[ MENU ]=====')
    print('[1] Obtener Usuarios')
    print('[2] Obtener Posts')
    print('[3] Crear Usuario')
    print('\nPresione ENTER para salir del Menu')
    opcion = input('==>  ')
    if opcion == '1':
        print('')
        obtener_usuarios_api('https://jsonplaceholder.typicode.com/users')
    elif opcion == '2':
        print('')
        obtener_posts_api('https://jsonplaceholder.typicode.com/posts')
    elif opcion == '3':
        print('')
        crear_user_api(url)
    elif opcion == '4':
        print('')
        modificar_user_api(url2)
    elif opcion == '5':
        print('')
        eliminar_user_api(url2)
    elif opcion == '':
        print('Nos vidrios')
        menu = False
    else:
        print('\nya po no me echi a perder el programita :(')
