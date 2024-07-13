inventario = {}

def agregar_producto(nombre, cantidad, precio):
    if nombre in inventario:
        print(f'El producto "{nombre}" ya existe en el inventario.')
    else:
        inventario[nombre] = {'cantidad': cantidad, 'precio': precio}
        print(f'Producto "{nombre}" agregado al inventario.')

def eliminar_producto(nombre):
    if nombre in inventario:
        del inventario[nombre]
        print(f'Producto "{nombre}" eliminado del inventario.')
    else:
        print(f'El producto "{nombre}" no existe en el inventario.')

def mostrar_inventario():
    if not inventario:
        print('El inventario está vacío.')
    else:
        print('Inventario:')
        for nombre, informacion in inventario.items():
            print(f'Producto: {nombre} | Cantidad: {informacion["cantidad"]} | Precio: ${informacion["precio"]}')

# Función principal para interactuar con el usuario
def main():
    while True:
        print('\n--- Sistema de Inventario ---')
        print('1. Agregar producto')
        print('2. Eliminar producto')
        print('3. Mostrar inventario')
        print('4. Salir')

        opcion = input('Selecciona una opción (1-4): ')

        if opcion == '1':
            nombre = input('Ingrese el nombre del producto: ')
            cantidad = int(input('Ingrese la cantidad: '))
            precio = float(input('Ingrese el precio por unidad: '))
            agregar_producto(nombre, cantidad, precio)

        elif opcion == '2':
            nombre = input('Ingrese el nombre del producto a eliminar: ')
            eliminar_producto(nombre)

        elif opcion == '3':
            mostrar_inventario()

        elif opcion == '4':
            print('Saliendo del programa.')
            break

        else:
            print('Opción inválida. Por favor, seleccione una opción válida (1-4).')

if __name__ == '__main__':
    main()