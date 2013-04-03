from flask import Flask, render_template, redirect, request
import model

app = Flask(__name__)

# @app.route("/")
# def index():
# 	# do sign up stuff here
# 	return render_template("index.html")

# @app.route("/user_list")
@app.route("/")
def user_list():
	# queries all the users, returns in a list
	user_list = model.session.query(model.User).limit(5).all()
	# "redirects" to user_list.html, feeding argument of list of user objects
	return render_template("user_list.html", users=user_list)

# @app.route("/user_ratings")
# def user_ratings():
# 	user_ratings = model.session.query(model.Ratings).all()



if __name__ == "__main__":
	app.run(debug = True)