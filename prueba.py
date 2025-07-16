productos = {
'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}
def stock_marca():
    marca = input("ingrese el nombre de la marca a consultar stock disponible: ")
    for marca, in stock, productos.items():
        print(f"el stock es: {marca}")

def busqueda_precio():
    while True:
        try:
            precio_min = int(input("ingrese un precio minimo a buscar :"))
            precio_max = int(input("ingrese un precio maximo a buscar :")) 
            if precio_min and precio_max not in [stock]
            buscar_producto = precio_min and precio_max
               print("“No hay notebooks en ese rango de precios.”")
            else:
                for precio_min, precio_max in stock:
                    print(f"Los notebooks entre los precios consultas son: {[buscar_producto]}") 
                    True  

        except ValueError:
           print("“Debe ingresar valores enteros!!”")     

def actualizar_precio():
    while True:
        try: 

            modelo = input("Ingrese modelo a actualizar: ")
            precio = int(input("ingrese nuevo precio para el modelo: "))
            for modelo, precio in productos.items():
               modelo[producto]
            False = input("Desea actualizar otro precio (s/n)?:")   
            if False == 'n'
               false = True
            print("Precio actualizado!!" )
            break
        except ValueError:
            print("opcion no valida")
            print("intente nuevamente...")

def mostrar_menu():
   print("*** MENU PRINCIPAL ***")
   print("1. Stock marca.")
   print("2. Búsqueda por precio.")
   print("3. Actualizar precio.")
   print("4. Salir.")

while True: 
    mostrar_menu()   
    opcion = int(input("ingrese una opcion entre (1-4): "))
    if opcion == 1:
        stock_marca()
    elif opcion == 2:
        busqueda_precio()
    elif opcion == 3:
        actualizar_precio()    
    elif opcion == 4:
        print("saliendo del programa...")
        break
    else:
        print("ingrese una opcion valida..")  
          






