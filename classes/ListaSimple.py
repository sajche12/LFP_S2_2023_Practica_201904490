

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaSimple:
    
    # Constructor
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0
    
    # Metodo agregar nodo
    def agregar(self, dato):
        nuevo = Nodo(dato)
        if self.primero == None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
        self.size += 1
    
    #Metodo para imprimir la lista
    def __iter__(self):
        actual = self.primero
        while actual != None:
            yield actual.dato
            actual = actual.siguiente
    
    #Metodo para buscar un nodo en la lista
    def buscar(self, dato):
        actual = self.primero
        while actual != None:
            if actual.dato == dato:
                return actual.dato
            actual = actual.siguiente
        return None      
    
    #metodo para actualizar la cantidad en self.productos.lista_productos de un producto
    def actualizar_cantidad(self, nombre, cantidad):
        from classes.ListaProductos import ListaProductos
        lista = ListaProductos()
        for producto in lista.lista_productos:
            if producto.nombre == nombre:
                producto.cantidad = cantidad
                break
    
    