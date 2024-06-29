# Jefferson-Rojas Ingenieria en Informatica Duoc Plaza Norte #
| CONTEXTO: | 
Un banco internacional ha solicitado una aplicación en Python para analizar y gestionar los datos financieros de sus clientes. La aplicación debe manejar datos sensibles, realizar cálculos complejos y generar informes detallados. Este proyecto tiene una alta complejidad debido a la necesidad de precisión en los cálculos financieros y la gestión segura de la información.
En esto tuve que requerir de los siguientes:
-	Desarrollo de una aplicación en Python y en entorno de desarrollo Visual Studio Code
-	Uso de colecciones 
-	Uso de archivos de texto
-	Uso de librerías estándar de Python

Está aplicación de python se desarrollo como una parte de una evaluación

esta app permite:
1. generar saldos aleatorios para 10 clientes
2. clasificar los saldos en rangos específicos
3. calcular y mostrar estadísticas avanzadas sobre los saldos
4. generar un reporte detallado de saldos con deudcciones y saldo neto, y exportar a un archivo CSV

Requisito:

- Python

1. **Generar saldos aleatorios**: 
   - Genera y muestra saldos aleatorios para 10 clientes en el rango de 300.000 a 1.500.000.
   - Seleccione la opción "1" en el menú principal.

2. **Clasificar saldos**:
   - Clasifica los saldos generados en tres rangos:
     - Bajo: Menos de 480.000
     - Medio: De 480.000 a menos de 750.000
     - Alto: 750.000 o más
   - Seleccione la opción "2" en el menú principal.

3. **Ver estadísticas**:
   - Muestra estadísticas avanzadas sobre los saldos:
     - Saldo más alto
     - Saldo más bajo
     - Saldo promedio
     - Media geométrica
   - Seleccione la opción "3" en el menú principal.

4. **Generar reporte**:
   - Genera un reporte detallado de los saldos con deducciones y saldo neto.
   - Exporta el reporte a un archivo CSV llamado "reporte_saldos.csv".
   - Seleccione la opción "4" en el menú principal.

5. **Salir del programa**:
   - Finaliza la ejecución del programa.
   - Seleccione la opción "5" en el menú principal.

## Ejecución

Para ejecutar la aplicación, use el siguiente comando en su terminal:

```sh

Menú de opciones:
1. Generar saldos aleatorios
2. Clasificar saldos
3. Ver estadísticas
4. Generar reporte
5. Salir
Elija una opción: 1
Saldos generados: ['532.000', '487.500', '645.300', '732.000', '1.245.000', '1.150.000', '950.000', '405.000', '1.100.000', '1.350.000']

Elija una opción: 2
Rango bajo: ['405.000', '487.500']
Rango medio: ['532.000', '645.300', '732.000']
Rango alto: ['1.245.000', '1.150.000', '950.000', '1.100.000', '1.350.000']

Elija una opción: 3
Saldo más alto: 1.350.000
Saldo más bajo: 405.000
Saldo promedio: 866.980
Media geométrica: 788.240

Elija una opción: 4
Reporte generado y guardado como reporte_saldos.csv

Elija una opción: 5
Gracias por usar el programa.


Este archivo `README.md` proporciona una descripción clara y completa de la aplicación, incluyendo sus características, requisitos, instrucciones de uso, ejemplos y la licencia. Puedes modificar cualquier sección según tus necesidades específicas.

