from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/hogar')
def hogar():
    return render_template("hogar.html")
@app.route('/vivienda')
def vivienda():
    return render_template("vivienda.html")
@app.route('/contacto')
def contacto():
    return render_template("contacto.html")
@app.route('/index', methods=['POST'])
def recibir_ubicacion():
    data = request.get_json()
    print("📍 Ubicación recibida:", data)
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(debug=True)
