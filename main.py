

from flask import Flask, render_template, request

app = Flask(__name__)  

@app.route('/')
def index():
    grupo="IDGS803"
    lista=["Juan", "Pedro", "Maria"]
    return render_template("index.html", grupo=grupo, lista=lista)

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
    app.run(debug=True)

    