import flask
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["DEBUG"] = True


class MyPython_Flask:

    # Create some test data for our catalog in the form of a list of dictionaries.
    books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
    ]


    @app.route('/', methods=['GET'])
    def initialMethod():
        return "<h1>MyPython Project Home Page</h1><p>This site is a prototype of my python and flask experiments.</p>"


    @app.route('/home',methods=['GET'])
    def home():
        return "<h1>You're Home</h1>"

    # A route to return all of the available entries in our catalog.
    @app.route('/api/v1/resources/books/all', methods=['GET'])
    def getAllBooks():
        return jsonify(MyPython_Flask.books)

    @app.route('/api/v1/resources/books')
    def getBookByID_RquestArgs():
        if 'id' in request.args:
            try:
                id = int(request.args['id'])
            except:
                return "Error: Input is not an integer"

            result=[]
            for book in MyPython_Flask.books:
                if(book['id']==id):		
                    result.append(book)
                    return(jsonify(result))
        else:
            return "Error: No id field provided. Please specify an id."

    @app.route('/api/v1/resources/books/<int:id>')
    def getBookByID_Number(id):
        print("x")
        try:
            print("y")
            id = int(id)
        except:
            return "Error: Input is not an integer"

        result=[]
        for book in MyPython_Flask.books:
            if(book['id']==id):
                result.append(book)
                return(jsonify(result))

if __name__ == '__main__':
    app.run()
