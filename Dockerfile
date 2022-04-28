from flask import Flask


app=Flask(__name__)

@app.route("/")
def hello():
    return"hello world"


@app.route("/number")
def rand_numb():
    import random

    from random import randint

    Random_number=random.randint(1,1000)
    return str(Random_number)


if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0")