from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    my_text = {
            "name": "Максим Степаненков",
            "pic": "http://old.301-1.ru/gen-mems/img_mems/2015_04_04_59e4547772c712fec3f002a2ed48bd2d.jpg",
            "pint": "https://www.pinterest.ru/stepanenkov25/",
            "skill": "Python"
            }

    return render_template('me.html', my=my_text)

app.run()

