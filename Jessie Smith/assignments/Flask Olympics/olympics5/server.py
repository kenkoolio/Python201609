from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process/<id>', methods = ['POST'])
def process(id):
    print ("I love flask! And {}".format(id))
    return redirect('/')


if __name__ == '__main__':
  app.run(debug = True)


"""
Will this work?  What
What will this print??? It will print I love flask and peaches to the terminal.
"""
