from classes.ListaProductos import ListaProductos
from classes.Producto import Producto
import tkinter as tk
from tkinter import filedialog

class Menu:
    lista_productos = ListaProductos()
    
    def cargar_inventario_inicial(self):
        root = tk.Tk()
        root.withdraw()  # Ocultar la ventana principal de Tkinter

        archivo_inventario = filedialog.askopenfilename()  # Abrir el explorador de archivos y seleccionar un archivo_inventario
        
        #verificar que el archivo sea extension .inv
        if archivo_inventario.endswith(".inv"):  
        # Aquí puedes realizar acciones con el archivo_inventario seleccionado, por ejemplo, leer su contenido
            with open(archivo_inventario, 'r') as f:
                contenido = f.read()
                #recorrer cada linea del archivo
                for linea in contenido.splitlines():
                    #separar cada linea por comas
                    datos = linea.split(";")
                    nombre = datos[0].strip("crear_producto ")
                    #crear un objeto de tipo Producto y agregarlo a la lista de productos
                    producto = Producto(nombre, datos[1], datos[2], datos[3])
                    self.lista_productos.lista_productos.agregar(producto)
            print("\n¡Archivo cargado correctamente!\n")
        else:
            print("\nEl archivo que seleccionaste no tiene terminacion .inv.\n")

        #imprimir la lista de productos
        print("Lista de productos:")
        print("---------------------------------------------------------------------------")
        for producto in self.lista_productos.lista_productos:
            print(f"Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio unitario: {producto.precio_unitario}, Ubicacion: {producto.ubicacion}")
            print("---------------------------------------------------------------------------")
        print()
        root.destroy()
        self.menu_principal()
        
    def cargar_movimientos(self):
        root = tk.Tk()
        root.withdraw()  # Ocultar la ventana principal de Tkinter

        archivo_movimientos = filedialog.askopenfilename()  # Abrir el explorador de archivos y seleccionar un archivo_movimientos
        
        #verificar que el archivo sea extension .mov
        if archivo_movimientos.endswith(".mov"):  
        # Aquí puedes realizar acciones con el archivo_movimientos seleccionado, por ejemplo, leer su contenido
            with open(archivo_movimientos, 'r') as f:
                contenido = f.read()
                
                #recorrer cada linea del archivo
                print("\n-----------------------------------------------------------------------------")
                for linea in contenido.splitlines():
                    #separar cada linea por comas
                    datos = linea.split(";")
                    #convertir datos[1] a entero
                    cantidad_agregar = int(datos[1])
                    #verificar si datos[0] contine la cadena "agregar_stock " o "vender_producto "
                    if datos[0].startswith("agregar_stock "):
                        producto_agregar = datos[0].replace("agregar_stock ", "")
                        for producto_lista in self.lista_productos.lista_productos:
                            #convertir producto_lista.cantidad a entero
                            cantidad_existente = int(producto_lista.cantidad)
                            producto_encontrado = False
                            #verificar si el producto a agregar es igual al nombre del producto en la lista de productos
                            if producto_agregar == producto_lista.nombre:
                                #actulizar la cantidad del producto en la lista de productos
                                cantidad_total = cantidad_existente + cantidad_agregar
                                print(f"El producto {producto_agregar} se agrego correctamente, su nueva cantidad es {cantidad_total}")
                                #Actualizando producto en la lista
                                producto_actualizado = Producto(producto_lista.nombre, cantidad_total, producto_lista.precio_unitario, producto_lista.ubicacion)
                                self.lista_productos.lista_productos.agregar(producto_actualizado)
                                producto_encontrado = True
                                break
                        if producto_encontrado == False:
                            print(f"El producto {producto_agregar} no existe en el inventario")
                    elif datos[0].startswith("vender_producto "):
                        producto_vender = datos[0].strip("vender_producto ")
                        for producto_lista in self.lista_productos.lista_productos:
                            encontrado = False
                            if producto_vender == producto_lista.nombre:
                                cantidad_existente = int(producto_lista.cantidad)
                                if cantidad_agregar <= cantidad_existente:
                                    #actualizar la cantidad del producto en la lista de productos
                                    cantidad_total = cantidad_existente - cantidad_agregar
                                    print(f"El producto {producto_vender} se vendio correctamente, su nueva cantidad es {cantidad_total}")
                                    #actualizar producto en la lista
                                    producto_actualizado = Producto(producto_lista.nombre, cantidad_total, producto_lista.precio_unitario, producto_lista.ubicacion)
                                    self.lista_productos.lista_productos.agregar(producto_actualizado)
                                    encontrado = True
                                    break
                                elif cantidad_agregar >= cantidad_existente:
                                    print(f"El producto {producto_vender} no tiene suficiente cantidad para vender")
                                    encontrado = True
                                    break
                        if encontrado == False:
                            print(f"El producto {producto_vender} no existe en el inventario")
                print("-----------------------------------------------------------------------------\n")
        else:
            print("\nEl archivo que seleccionaste no tiene terminacion .inv.\n")
        root.destroy()
        self.menu_principal()
        
    
    def crear_informe_inventario(self):
        #exportar en un archivo .txt la informacion de cada producto
        with open("informe_inventario.txt", "w") as f:
            f.write("Informe de Inventario:\n\n")
            f.write("Producto\tCantidad\tPrecio unitario\t\tValor Total\tUbicacion\n")
            f.write("------------------------------------------------------------------------------------\n")
            valor_total_producto = 0
            for producto in self.lista_productos.lista_productos:
                valor_total_producto = round(float(producto.cantidad) * float(producto.precio_unitario), 2)
                f.write(f"{producto.nombre}\t\t{producto.cantidad}\t\tQ{producto.precio_unitario}\t\tQ{valor_total_producto}\t\t{producto.ubicacion}\n")
        print("\n¡Informe de inventario creado correctamente!\n")
        
        self.menu_principal()
        
    
    def menu_principal(self):
        print("-------------- MENU PRINCIPAL -------------")
        print("| 1. Cargar inventario inicial            |")
        print("| 2. Cargar instrucciones de movimientos  |")
        print("| 3. Crear informe de inventario          |")
        print("| 4. Salir                                |")
        print("-------------------------------------------")
        # Validar que la opción ingresada sea un número
        try:
            opcion = int(input("\nIngrese una opción: "))
            if opcion == 1:
                self.cargar_inventario_inicial()
            elif opcion == 2:
                self.cargar_movimientos()
            elif opcion == 3:
                self.crear_informe_inventario()
            elif opcion == 4:
                print("Saliendo...")
                exit()
            else:
                print("\nLa opción ingresada no es válida\n")
                self.menu_principal()
        except ValueError:
            print("\nLa opción ingresada no es válida\n")
            self.menu_principal()
        
               
    
        