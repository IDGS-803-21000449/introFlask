

from flask import Flask, render_template, request
from flask import g
from flask import flash
from flask_wtf.csrf import CSRFProtect

import forms

app = Flask(__name__)  
app.secret_key="Esta es la clave secreta"
csrf=CSRFProtect()

@app.errorhandler(400)
def page_not_foun(e):
    return render_template('404.html'), 404

@app.before_request
def before_request():
    g.nombre="Mario"
    print('Before request 1')

@app.after_request
def after_request(response):
    print('Before request 3')
    return response

@app.route('/')
def index():
    grupo="IDGS803"
    lista=["Juan", "Pedro", "Maria"]
    print('Index 2')
    print("Hola {}".format(g.nombre))
    return render_template("index.html", grupo=grupo, lista=lista)

@app.route('/alumnos',methods=["GET", "POST"])
def alumnos():
    mat=""
    nom=""
    edad=""
    correo=""
    ape=""

    alumno_clase=forms.UserFrom(request.form)

    if request.method=='POST' and alumno_clase.validate():
        mat=alumno_clase.matricula.data
        nom=alumno_clase.nombre.data
        ape=alumno_clase.apellidos.data
        edad=alumno_clase.edad.data
        correo=alumno_clase.email.data
        mensaje='Bienvenido{}'.format(nom)
        flash(mensaje)

    return render_template("alumnos.html", form=alumno_clase, mat=mat, nom=nom, ape=ape, edad=edad, correo=correo)



@app.route("/OperaBas")
def operas():
    return render_template("OperaBas.html")

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    if request.method == "POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")

    return "La suma de {} y {} es: {} ".format(num1, num2, int(num1)+ int(num2))


@app.route('/cal', methods=['GET', 'POST'])
def calcular():

    resultado = ""

    if request.method == 'POST':
        n1 = int(request.form.get('n1', 0))
        n2 = int(request.form.get('n2', 0))
        resultado = str(n1 + n2)

    return render_template("OperaBas.html", resultado=resultado)


@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route("/hola")
def hola():
    return "Hola!!"

@app.route("/user/<string:user>")
def user(user):
    return f"Hola {user}!!!"

@app.route("/numero/<int:n>")
def numero(n):
    return "Número: {}".format(n)

@app.route("/user/<string:user>/<int:id>")
def username(user, id):
    return f"Nombre: {user} id: {id}!!!"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "La suma es {}!!!".format(n1 + n2)


@app.route("/cinepolis")
def cine():
    return render_template("cine.html")

@app.route("/layout")
def layout():
    return render_template("layout.html")



@app.route('/fin', methods=['GET', 'POST'])
def fin():
    resultado = ""

    if request.method == 'POST':
        nombre = request.form.get('nombre', "")
        compradores = int(request.form.get('compradores', 0))
        boletos = int(request.form.get('boletos', 0))
        tarjeta = request.form.get('tarjeta', "No especificado")

        max_boletos = compradores * 7

        if boletos > max_boletos:
            resultado = f"Compra fallida: Con {compradores} comprador(es) solo puede comprar hasta {max_boletos} boletos. Usted intentó comprar {boletos} boletos."
        else:
            if boletos > 6:
                total = boletos * 12
                total2 = total * 0.15
                total3 = total - total2

                if tarjeta == "Si":
                    total4 = total3 * .10
                    totalfin = total3 - total4
                    resultado = f"Se compraron {boletos} boletos, por {compradores} compradores, a nombre de {nombre} (Tarjeta Cineco: {tarjeta}), con un costo total de ${totalfin}"
                else:
                    resultado = f"Se compraron {boletos} boletos, por {compradores} compradores, a nombre de {nombre} (Tarjeta Cineco: {tarjeta}), con un costo total de ${total3}"

            elif boletos >= 3 and boletos <= 5:
                total = boletos * 12
                total2 = total * 0.10
                total3 = total - total2

                if tarjeta == "Si":
                    total4 = total3 * .10
                    totalfin = total3 - total4
                    resultado = f"Se compraron {boletos} boletos, por {compradores} compradores, a nombre de {nombre} (Tarjeta Cineco: {tarjeta}), con un costo total de ${totalfin}"
                else:
                    resultado = f"Se compraron {boletos} boletos, por {compradores} compradores, a nombre de {nombre} (Tarjeta Cineco: {tarjeta}), con un costo total de ${total3}"
            else:
                total = boletos * 12

                if tarjeta == "Si":
                    total4 = total * .10
                    totalfin = total - total4
                    resultado = f"Se compraron {boletos} boletos, por {compradores} compradores, a nombre de {nombre} (Tarjeta Cineco: {tarjeta}), con un costo total de ${totalfin}"
                else:
                    resultado = f"Se compraron {boletos} boletos, por {compradores} compradores, a nombre de {nombre} (Tarjeta Cineco: {tarjeta}), con un costo total de ${total}"


    return render_template("cine.html", resultado=resultado)

if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True)

    