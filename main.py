
from flask import Flask,redirect,request,url_for,render_template
app = Flask(__name__)

all_books = []

@app.route('/')
def home():
    return render_template('index.html', books="Hello")


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/addBook', methods=['POST'])
def book():
    if request.method == "POST":

        title = request.form["title"]
        author = request.form["author"]
        rating = request.form["rating"]


        # new_book = Book(id=2, title=title, author=author, rating=rating)
        # db.session.add(new_book)
        # db.session.commit()

        all_books = [title,author,rating]
        print(all_books)

        return redirect(url_for('home'))

if __name__== '__main__':
    app.run(debug=True)



