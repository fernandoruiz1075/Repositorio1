from flask import Flask, render_template, request
from database.db import connectionSQL, add_user
from controllers.admin_s3 import *
app = Flask(__name__)

@app.route ("/")
def home_page ():
    return render_template("home.html")

@app.route('/register_page')
def register_page ():
    return render_template("register.html")

@app.route('/register_user', methods = ["post"])
def register_user():
    data_user=request.form
    data_photo = request.files
    id = data_user["id"]
    name = data_user["name"]
    lastname = data_user["lastname"]
    birthday = data_user["birthday"]
    #print(data_user)
    photo = data_photo["photo"]
    confirm = add_user(id, name, lastname, birthday)
    #photo_path, photo_name = save_file(photo)
    #upload_file(photo_path, photo_name)
    if confirm:
        photo_path, photo_name = save_file(photo, id)
        upload_file(photo_path, photo_name)
        return "User added>"
    else:
        return "<h1> Error creating the user <h1/>"

if __name__ =="__main__":
    ip = "0.0.0.0"
    port = "5000"
    print("hola")
    app.run (ip, port, debug=True)