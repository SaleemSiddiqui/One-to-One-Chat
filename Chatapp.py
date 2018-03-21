from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextField

app= Flask(__name__)
app.config['SECRET_KEY']= 'saleem'

@app.route('/form')
def form():
    message=list(range(0,9))
    for i in range(0,9):
        message[i]="my name is saleem"
    
    header1="<h5>"
    header2="</h5"
    StringHeader=""
    for s in message:
        StringHeader+=header1+s+header2
    return render_template('chat.html',SDoc=StringHeader)

if __name__ == '__main__':
    app.run(debug=True)