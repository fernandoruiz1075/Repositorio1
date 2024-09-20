from flask import Flask

app = Flask(__name__)

@app.route('/register_page')
def register ():
    return render_template ("templates/register.html")

if __name__ =="__main__":
    ip = "172.31.31.189"
    port = "80"
    app.run (ip, port)
