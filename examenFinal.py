
class Sistema_vehiculos:

    # Control de Inventario
    def listar_vehiculos(self):
        self.cursor.execute("SELECT codigo, nombre, existencia, proveedor, precio FROM inventario")
        for (codigo, marca, modelo, precio, kilometraje) in self.cursor:
            print(f"Código: {codigo}, marca: {marca}, Modelo: {modelo}, Precio: {precio}, Kilometraje: {kilometraje}")

    def crear_vehiculo(self, codigo, nombre, existencia, proveedor, precio):
        query = "INSERT INTO inventario (codigo, nombre, existencia, proveedor, precio) VALUES (%s, %s, %s, %s, %s)"
        values = (codigo, nombre, existencia, proveedor, precio)
        self.cursor.execute(query, values)
        self.conexion.commit()
        print(f"Producto '{nombre}' creado con éxito.")


    def editar_vehiculo(self, codigo, kilometraje, precio):
        query = "UPDATE inventario SET existencia = existencia + %s WHERE codigo = %s"
        values = (kilometraje, codigo, precio)
        self.cursor.execute(query, values)
        self.conexion.commit()
        print(f"Existencias del producto editadas con éxito.")

    def eliminar_producto(self, codigo):
        query = "DELETE FROM inventario WHERE codigo = %s"
        self.cursor.execute(query, (codigo,))
        self.conexion.commit()
        print(f"Producto eliminado con éxito.")



def mostrar_menu():
    print("Menu:")
    print("1. Mantenimiento de vehiculos")
    print("2. Carga masiva de vehiculos")
    print("3. Salir")

def main():
    
    sistema = Sistema_vehiculos()

    
    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ")

        if opcion == "1":
            # Control de Inventario
            print("Mantenimiento de vehiculos:")
            print("a. Crear vehiculos")
            print("b. Editar vehiculo")
            print("c. Eliminar vehiculo")
            print("d. Listar vehiculos")
            sub_opcion = input("Elija una opción: ")

            if sub_opcion == "a":
                codigo = input("Código: ")
                nombre = input("Marca: ")
                existencia = int(input("Modelo: "))
                proveedor = input("Precio: ")
                precio = float(input("Kilometraje: "))
                sistema.crear_vehiculo(codigo, nombre, existencia, proveedor, precio)
            elif sub_opcion == "b":
                 codigo = input("Código del producto a editar existencias: ")
                 cantidad = int(input("Cantidad a agregar/reducir: "))
                 sistema.editar_vehiculo(codigo, cantidad)
            elif sub_opcion == "c":
                 codigo = input("Código del producto a eliminar: ")
                 sistema.eliminar_producto(codigo)
            elif sub_opcion == "d":
                codigo = input("Código del producto a editar existencias: ")
                cantidad = int(input("Cantidad a agregar/reducir: "))
                sistema.editar_existencias(codigo, cantidad)
            elif sub_opcion == "e":
                codigo = input("Código del producto a eliminar: ")
                sistema.eliminar_producto(codigo)

        elif opcion == "2":
          print("Ingrese la carga masiva de vehiculos(Código|Marca|Modelo|Precio|Kilometraje|CantidadFotos)")
          respuesta = input("Elija opcion: ")


        elif opcion == "3":
            print("Saliendo del sistema.")
          
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()


