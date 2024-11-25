# -*- coding: utf-8 -*-
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio():
    resultado = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        total_sin_descuento = cantidad * 9000

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_con_descuento = total_sin_descuento * (1 - descuento)

        resultado = {
            'nombre': nombre,
            'total_sin_descuento': total_sin_descuento,
            'total_con_descuento': total_con_descuento
        }

    return render_template('Ejercicio1.html', resultado=resultado)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = ""

    if request.method == 'POST':
        nombre = request.form['nombre']
        contraseña = request.form['contraseña']

        if nombre == "juan" and contraseña == "admin":
            mensaje = f"Bienvenido administrador {nombre}"
        elif nombre == "pepe" and contraseña == "user":
            mensaje = f"Bienvenido usuario {nombre}"
        else:
            mensaje = "Usuario o contraseña incorrecta."

    return render_template('Ejercicio2.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run()