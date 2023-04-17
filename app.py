from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/mypage/me', methods=['GET'])

def me():
    return render_template("index.html")

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
   if request.method == 'GET':
       print("We received GET")
       return render_template("index2.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")

if __name__ == "__main__": 
    app.run()

