from flask import Flask, render_template #import the Flask class
app = Flask(__name__) #creating new instance of the Flask class

# the '@' decorater assocaites the route with the following function
@app.route("/") # '/' is the index route
def index():
    return ("Hello World!")

#path variable/route varibale
@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<name>")
def show_user(name):
    return f"Hi {name}!"


@app.route("/repeat/<name>/<num>")
def repeat(num, name):
    return name * int(num)


if __name__ == "__main__":
    app.run(debug = True)
