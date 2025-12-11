from negocio.negocio_users import obtener_user_api, crear_user_api, modificar_user_api, eliminar_user_api
from negocio.negocio_posts import obtener_posts_api
url = 'https://jsonplaceholder.typicode.com/users'
url2 = 'https://jsonplaceholder.typicode.com/users/1'

invalido = 'Opción No Válida'
invalido2 = 'Opción No Válida'

menu = True
while menu:
    print('\n=====[ MENU PRINCIPAL ]=====')
    print('[1] Métodos Usuarios')
    print('[2] Métodos Posts')
    print('[3] Activar Modo Navideño')
    print('\nPresione ENTER para salir del Menu')
    opcion = input('==>  ')

#   users
    if opcion == '1':
        loop = True
        while loop:
            print('\n=====[ MENU USUARIOS ]=====')
            print('[1] Obtener Usuarios [GET]')
            print('[2] Crear Usuario [POST]')
            print('[3] Modificar Usuario [PUT]')
            print('[4] Eliminar Usuario [DELETE]')
            print('[0] Volver al Menú Principal')
            print('\nPresione ENTER para salir del Menú')
        
            opcion2 = input('==>  ')

            if opcion2 == '1':
                obtener_user_api()
            elif opcion2 == '2':
                crear_user_api()
            elif opcion2 == '3':
                modificar_user_api()
            elif opcion2 == '4':
                eliminar_user_api()
            elif opcion2 == '0':
                loop = False
            elif opcion2 == '':
                print('Nos vidrios')
                loop = False
                menu = False
            else:
                print(invalido2)

#   posts
    elif opcion == '2':
        loop = True
        while loop:
            print('\n=====[ MENU POSTS ]=====')
            print('[1] Obtener Posts [GET]')
            print('[2] Crear Post [POST]')
            print('[3] Modificar Post [PUT]')
            print('[4] Eliminar Post [DELETE]')
            print('[0] Volver al Menú Principal')
            print('\nPresione ENTER para salir del Menu')
            
            opcion2 = input('==>  ')

            if opcion2 == '1':
                obtener_posts_api()
            elif opcion2 == '2':
                pass
            elif opcion2 == '3':
                pass
            elif opcion2 == '4':
                pass
            elif opcion2 == '0':
                loop = False
            elif opcion2 == '':
                print('Nos vidrios')
                loop = False
                menu = False
            else:
                print(invalido2)
    elif opcion == '3':
        invalido = '\n❄Feliz Navidad❄ ♫♪♪ ❄Feliz Navidad❄ ♫♪♪\nNo me eche a perder el programita :('
        invalido2 = '♫♪♪ ❄AWANAWICHU❄ ♪ A ♪ ❄MERI❄CRISMAS❄ ♫♪♪'
        print('Work: OFF\nJolly: ON')
    elif opcion == '':
        print('Nos vidrios')
        menu = False
    else:
        print(invalido)

