from flask import Flask, render_template

app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/establecimientos')
def establecimientos():
    return render_template('establecimientos.html')

@app.route('/comprar')
def comprar():
    return render_template('comprar.html')

@app.route('/vender')
def vender():
    return render_template('vender.html')

@app.route('/ingresar')
def ingresar():
    return render_template('ingresar.html')

if __name__ == "__main__":
    app.run(debug=True)