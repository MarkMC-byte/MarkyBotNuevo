from modulos import rostro

print("=== PRUEBA DE RECONOCIMIENTO FACIAL ===")
print("1. Registrar un rostro nuevo")
print("2. Reconocer un rostro")
opcion = input("Selecciona una opción (1 o 2): ")

if opcion == "1":
    nombre = input("Ingresa tu nombre: ")
    rostro.capturar_rostro(nombre)

elif opcion == "2":
    nombre_detectado = rostro.reconocer_rostro()
    if nombre_detectado:
        print(f"Rostro reconocido: {nombre_detectado}")
    else:
        print("No se reconoció ningún rostro.")

else:
    print("Opción no válida.")
