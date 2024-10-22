from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    # return render_template('home.html') to render HTML
    return render_template('home.html')  # Fixed: proper return with quotes

if __name__ == "__main__":  
    app.run(host='0.0.0.0', debug=True)
