# Proyecto de Dianna Monsalve
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    nombre = "Dianna Monsalve"
    return render_template('index.html', name=nombre)

#Ejercicio 1 -->
@app.route('/ejercicio_1', methods=['GET', 'POST'])
def ejercicio_1():
    promedio = None
    estado = None
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        promedio = (nota1 + nota2 + nota3) / 3
        #promedio = round(promedio, 1)
        if promedio >= 40 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"
    return render_template('ejercicio_1.html', promedio=promedio, estado=estado)

#Ejercicio 2 -->
@app.route('/ejercicio_2', methods=['GET', 'POST'])
def ejercicio_2():
    nombre = None
    longitud = None
    if request.method == 'POST':
        nombre1 = request.form.get('nombre1')
        nombre2 = request.form.get('nombre2')
        nombre3 = request.form.get('nombre3')

        nombres = [nombre1, nombre2, nombre3]
        nombre = max(nombres, key=len)
        longitud = len(nombre)

    return render_template('ejercicio_2.html', nombre=nombre, longitud=longitud)

if __name__ == '__main__':
    app.run()
