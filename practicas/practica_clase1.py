## Variables y tipos de datos


producto = "Adifonos inalambricos"
precio = 45.99
en_oferta = True
cantidad_stock = 120

print (producto)
print (precio)
print (en_oferta)
print (type (producto), type (precio), type (en_oferta), type (cantidad_stock))


## una compra cuesta 18.75 y el cliente paga con un billete de 20. calcula e imprime la devuelta exacta


compra_total = 18.75
pago_cliente = 20
devuelta = pago_cliente - compra_total

print(f"devuelta: {devuelta}")

##  Un cajero tiene que dar 37 dólares en cambio, usando la menor cantidad posible de billetes de 10. Calcula cuántos billetes de 10 puede dar, y el sobrante en billetes mas pequeños


monto = 37
billetes_de_diez = monto // 10
sobrante = monto % 10
print(f"Billetes de diez: ", billetes_de_diez, "Sobrante", sobrante)


##  Con un monto de 48 hacer el mismo calculo
monto = 48
billetes_de_diez = monto // 10
sobrante = monto % 10
print(f"Billetes de diez: ", billetes_de_diez, "Sobrante", sobrante)


## Pídele al usuario 2 números distintos, uno a la vez, con input(). Conviértelos a número, y muestra con un f-string la suma de ambos

primer_numero = float(input("Escribe el primer numero: "))
segundo_numero = float(input("Escribe el segundo numero: "))
sum = primer_numero + segundo_numero
print(f"La suma de {primer_numero} y {segundo_numero} es {sum}")


## Crear una variable nota con un número del 0 al 100. Clasifícala en una letra: "A" si es 90 o más, "B" si es 80 o más, "C" si es 70 o más, y "F" en cualquier otro caso. Imprime la nota junto con su letra.


nota = 88
if nota >= 90:
    letra = "A"
elif nota >= 80:
    letra = "B"
elif nota >= 70:
    letra = "C"
else: 
    letra = "F"

print(f"Nota, {nota}: {letra}")


## Una tienda da descuento según el monto total de la compra: 15% si la compra es de $200 o más, 10% si es de $100 a $199, y sin descuento si es menos de $100. Pídele al usuario el monto de su compra con input(), calcula el descuento que le corresponde, y muestra con f-strings el monto original, el porcentaje de descuento aplicado, y el precio final después del descuento.


monto_de_compra = float(input("Ingrese el monto de compra: "))

if monto_de_compra >= 200:
    descuento = 0.15
elif monto_de_compra >= 100:
    descuento = 0.10
else:
    descuento = 0

precio_final = monto_de_compra - (monto_de_compra * descuento)

print(f"Monto original: ${monto_de_compra}")
print(f"Descuento aplicado: {int(descuento * 100)}%")
print(f"Precio final: ${precio_final}")


## Calculadora de propina inteligente

"""
Pídele al usuario el monto de la cuenta de un restaurante y la cantidad de personas en la mesa, ambos con input(). Calcula la propina sugerida según
estas reglas:
· Si la cuenta es menor a $20, la propina es del 10%.
· Si la cuenta es de $20 a $50, la propina es del 15%.
· Si la cuenta es mayor a $50, la propina es del 20%.
· Si además son más de 4 personas en la mesa, agrega un 5% adicional a la propina, sin importar el monto de la cuenta.
Muestra con f-strings: el monto de la propina, el total a pagar (cuenta más propina), y cuánto le toca pagar a cada persona si se divide el total entre
todos.
"""

monto_cuenta = float(input("Ingrese el monto de la cuenta: "))
cantidad_personas = int(input("Ingrese la cantidad de personas en la mesa: "))

if monto_cuenta < 20:
    propina = 0.10
elif monto_cuenta <= 50:
    propina = 0.15
else:
    propina = 0.20

if cantidad_personas > 4:
    propina += 0.05

total_propina = monto_cuenta * propina
total_a_pagar = monto_cuenta + total_propina
pago_por_persona = total_a_pagar / cantidad_personas

print(f"Propina: ${total_propina:.2f}")
print(f"Total a pagar: ${total_a_pagar:.2f}")
print(f"Pago por persona: ${pago_por_persona:.2f}")
