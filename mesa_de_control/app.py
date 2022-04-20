from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
#import controlador


app = Flask(__name__)


@app.route("/")
def index():
    #flash('Mensaje de prueba!')
    return render_template('index.html')

@app.route("/consultaRFC", methods=['POST'])
def consultaRFC():
    form_data = request.form.to_dict()
    print(form_data)
    #flash('Mensaje de prueba!')
    return redirect(url_for('index'))




if __name__== "__main__":
    app.run(debug=True)
