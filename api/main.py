from flask import Flask,render_template,jsonify,request
from gerador import Gerador

app = Flask("__main__")
ge = Gerador("anuncios.txt")
anuncios = []
@app.route("/home")
def home_page():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    if request.method == 'POST':
        req = request.json
        try:
            desc = req["desc"]
            sku = req["sku"]
            comp = req["comp"]
            larg = req["larg"]
            alt = req["alt"]
            pos = req["pos"]

            temp_dic = {"desc":desc,"sku":sku,"comp":comp,"larg":larg,"alt":alt,"pos":pos}

            anuncios.append(temp_dic)
            
            st = f"descrição: {desc}, sku: {sku}, CxLxA: {comp}x{larg}x{alt}, posição: {pos}"
            response = {
                "descricao":desc,
                "sku": sku,
                "comprimento": comp,
                "largura": larg,
                "altura": alt,
                "posicao":pos
            }
        
            return jsonify(response)
        except:
            return jsonify({"message":"missing arguments"})

@app.route("/gerar")
def gerar():

    ge.gerar(anuncios)

    anuncios.clear()

    return jsonify({"status":"created"})

if __name__ == "__main__":
    app.run(debug=True)