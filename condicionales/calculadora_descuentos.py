"""""
productos={

    "pan"=1000




}


pan=1000
leche=2000
huevo=3000
fruta=4000
"""""

precio_del_producto=int(input("ingresa el precio del producto"))
porcentaje_de_descuento=int(input("Dame el porcentaje de descuento "))

precio_final=precio_del_producto-precio_del_producto*porcentaje_de_descuento/100  

if precio_final>10000:
    print("Compra grande")

    print(precio_final)
