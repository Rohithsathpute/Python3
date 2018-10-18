"""
This script will create a sample site at localhost"
Steps to execute:
1.Install Flask (pip install flask)
2.Run the script (python website.py)
"""
from flask import Flask

app=Flask(__name__)


@app.route("/test")

def main():
    return "Hey there,this is your sample website!"

if __name__=="__main__":
    app.run(debug=True)

