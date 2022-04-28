from flask import Flask


app=Flask(__name__)

@app.route("/")
def hello():
    return"Hello World"


@app.route("/number")
def rand_num():
    import random
    from random import randint

    random_number = random.randint(1,1000)
    return str(random_number)

if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0")