from flask import Flask

app = Flask(__name__)

@app.route('/register_page')
def register ():
    return render template ("register.html")

if __name__ =="__main__":
    ip = "127.0.0.1"
    port = "8000"
    app.run (ip, port)

    

