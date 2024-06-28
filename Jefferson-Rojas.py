import random
import csv
import math
import locale

locale.setlocale(locale.LC_ALL, '')

def main():
    saldos = []

    while True:
        print("- Menú de opciones: -")
        print("|1. Generar saldos aleatorios")
        print("|2. Clasificar saldos")
        print("|3. Ver estadísticas")
        print("|4. Generar reporte")
        print("|5. Salir")
        
        opcion = input("Elija una opción: ")
        
        if opcion == '1':
            saldos = generar_saldos()
            print("Saldos generados:", [format(saldo, ".0f") for saldo in saldos])
        elif opcion == '2':
            if saldos:
                clasificar_saldos(saldos)
            else:
                print("Primero debe generar los saldos (opción 1).")
        elif opcion == '3':
            if saldos:
                calcular_estadisticas(saldos)
            else:
                print("Primero debe generar los saldos (opción 1).")
        elif opcion == '4':
            if saldos:
                generar_reporte(saldos)
            else:
                print("Primero debe generar los saldos (opción 1).")
        elif opcion == '5':
            print("Gracias por usar el programa.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 5.")

def generar_saldos(num_clientes=10):
    saldos = [random.uniform(300000.0, 1500000.0) for _ in range(num_clientes)]
    return saldos

def clasificar_saldos(saldos):
    rango_bajo = [saldo for saldo in saldos if saldo < 480000]
    rango_medio = [saldo for saldo in saldos if 480000 <= saldo < 750000]
    rango_alto = [saldo for saldo in saldos if saldo >= 750000]
    
    print("Rango bajo:", [format(saldo, ".0f") for saldo in rango_bajo])
    print("Rango medio:", [format(saldo, ".0f") for saldo in rango_medio])
    print("Rango alto:", [format(saldo, ".0f") for saldo in rango_alto])

def calcular_estadisticas(saldos):
    saldo_max = max(saldos)
    saldo_min = min(saldos)
    saldo_prom = sum(saldos) / len(saldos)
    saldo_geom = math.prod(saldos) ** (1 / len(saldos))
    
    print(f"Saldo más alto: {format(saldo_max, '.0f')}")
    print(f"Saldo más bajo: {format(saldo_min, '.0f')}")
    print(f"Saldo promedio: {format(saldo_prom, '.0f')}")
    print(f"Media geométrica: {format(saldo_geom, '.0f')}")

def generar_reporte(saldos, filename="reporte_saldos.csv"):
    deducciones = [saldo * 0.1 for saldo in saldos]
    saldos_netos = [saldo - deduccion for saldo, deduccion in zip(saldos, deducciones)]
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Cliente", "Saldo", "Deducción", "Saldo Neto"])
        for i, (saldo, deduccion, saldo_neto) in enumerate(zip(saldos, deducciones, saldos_netos), 1):
            writer.writerow([i, format(saldo, ".0f"), format(deduccion, ".0f"), format(saldo_neto, ".0f")])
    
    print(f"Reporte generado y guardado como {filename}")

if __name__ == "__main__":
    main()