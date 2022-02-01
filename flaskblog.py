from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author':'John',
        'title': 'Post 1',
        'content': 'Content for post 1'
    },
     {
        'author':'Tom',
        'title': 'Post 2',
        'content': 'Content for post 2'
    }

]

@app.route("/")
def home_page():
    return render_template('home.html', my_posts = posts)

@app.route("/about")
def about_page():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)