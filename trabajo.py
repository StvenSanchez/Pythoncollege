precio_producto = int(input("Cual es el precio del producto ? "))
cantidad = int(input("Cuanto desea comprar ? "))

precio_de_los_productos = precio_producto * cantidad 

print("El precio de los productos sin IVA ni descuento  es $",precio_de_los_productos )

precio_descuento = (precio_de_los_productos * 10) / 100

print("El precio de los productos con descuento  es $",precio_de_los_productos - precio_descuento )

precio_iva = (precio_descuento * 100 * 13) / 100

print("El precio de los productos con IVA  es $",precio_de_los_productos + precio_iva )


