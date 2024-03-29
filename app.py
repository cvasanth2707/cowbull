# importing Flask and other modules
from flask import Flask, request, render_template
import main as m

# Flask constructor
app = Flask(__name__)


# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods=["GET", "POST"])
def gfh():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        first_name = request.form.get("fname")
        # getting input with name = lname in HTML form
        last_name = request.form.get("lname")
        return "Your name is " + first_name + last_name
        #return render_template("play.html")
    return render_template("game.html")


if __name__ == '__main__':
    app.run(debug=True)
