from flask import Flask


app=Flask(__name__)

@app.route("/")
def hello():
    return"Welcome to my Hello World application"


@app.route("/number")
def rand_num():
    import random
    from random import randint

    random_number = random.randint(1,1000)
    return("The random number is :" +str(random_number))

if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0")