from flask import Flask,  render_template,url_for

app = Flask(__name__ )

@app.route("/")
def main():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/pricing")
def pricing():
    return render_template('pricing.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')


@app.route("/teachers")
def teachers():
    return render_template('teachers.html')



    if __name__ == "__main__":
         app.run()
