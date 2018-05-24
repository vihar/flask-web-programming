from flask import Flask
app = Flask(__name__)


@app.route('/greet')
def greet():
    user = {'username': 'John', 'age': 20}
    return '''
<html>
    <head>
        <title>Templating</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!, you’re ''' + user['age'] + ''' years old.</h1>
    </body>
</html>'''


if __name__ == '__main__':
   app.run(debug = True,port=8080)