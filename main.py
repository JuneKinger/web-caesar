from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form action="/" id="userform" method="post">
        <label for="rotate">Rotate by: 
            <input type="text" id="rotate" name="rot" value="0"/>
            <div>
                <br>
            </div>
        </label>
        <textarea name="text" form="userform">{0}</textarea>
        <input type="submit" />
      </form>

    </body>
</html>
"""

@app.route("/")
def index():
    return form.format()

@app.route("/", methods=["POST"])
def encrypt():
    rot_value = request.form["rot"]
    rot_value_int = int(rot_value)
    text_value = request.form["text"]
    encrypted_str = rotate_string(text_value, rot_value_int)
    encrypt_format = encrypted_str
    return form.format(encrypt_format)
app.run()