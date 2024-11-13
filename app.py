# Proyecto de Dianna Monsalve
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    nombre = "Dianna Monsalve"
    return render_template('index.html', name=nombre)

# Ejercicio 1 -->
@app.route('/ejercicio_1', methods=['GET', 'POST'])
# Se define función
def ejercicio_1():
    # Se definen las variables (inicialización)
    promedio = None
    estado = None
    # Verificación del metodo http
    if request.method == 'POST':
        #Se capturan los datos del formulario
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])
        # Se calcula promedio
        promedio = (nota1 + nota2 + nota3) / 3
        # Acá quise redondear a 1 decimal, pero lo cambié y deje directo en el html
        #promedio = round(promedio, 1)
        # Acá hago la validación del estado (Arobado/ Reprobado)
        if promedio >= 40 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"
    # Retorno de respuestas
    return render_template('ejercicio_1.html', promedio=promedio, estado=estado)

# Ejercicio 2 -->
@app.route('/ejercicio_2', methods=['GET', 'POST'])
# Se define función
def ejercicio_2():
    # Se declaran variables (inicialización)
    nombre = None
    longitud = None
    # Verificación metodo http
    if request.method == 'POST':
        # Se capturan los datos del formulario
        nombre1 = request.form.get('nombre1')
        nombre2 = request.form.get('nombre2')
        nombre3 = request.form.get('nombre3')
        # Se crea una lista de nombres para guardar los nombres ingresados
        nombres = [nombre1, nombre2, nombre3]
        # Se adquiere nombre más largo, encontrandolo con max y comparando con key=len
        nombre = max(nombres, key=len)
        # Con la función len capturo el numero de caracteres del nombre más largo
        longitud = len(nombre)
    # Devuelvo la respuesta
    return render_template('ejercicio_2.html', nombre=nombre, longitud=longitud)

if __name__ == '__main__':
    app.run()
