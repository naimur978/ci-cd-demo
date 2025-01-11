# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def index():
#     return "5 + 3 = 8"

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8000)

def add(a, b):
    return a + b

if __name__ == "__main__":
    print(f"5 + 3 = {add(5, 3)}")
