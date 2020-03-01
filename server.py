from flask import Flask, render_template
app = Flask(__name__)

# Home route
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

# Blog route
@app.route('/blog')
def blog():
    return 'Hello again from Blog'

# Another blog route
@app.route('/blog/2020/dogs')
def blog2():
    return 'Dog Blog'