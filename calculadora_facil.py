#Calculadora básica en python a prueba de errores por inputs no deseados @psre423p45

while True:
			try:
				calculo = eval(input("Ingrese una operación matemática:	"))
				print(f"El resulrado es {calculo}.")
			except:
				print("Operación erronea, intente de nuevo.")