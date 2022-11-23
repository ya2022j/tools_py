


from flask import  Flask,render_template,url_for,redirect,request
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,DateField,DateTimeField
from wtforms.validators import DataRequired



from flask_bootstrap import Bootstrap

app = Flask(__name__)

boostrap  =Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return redirect(url_for("index"))


    return render_template('index.html')



if __name__ == "__main__":
    app.run()