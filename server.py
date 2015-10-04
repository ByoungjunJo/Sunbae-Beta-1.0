import sqlite3
import time
from flask import Flask, request, g, render_template, redirect

app = Flask(__name__)
app.debug = True
DATABASE = 'Comments.db'

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
	return db

@app.teardown_appcontext
def close_connection(exception):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()

def db_read_Comments():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM Comments")
    return cur.fetchall()

def db_add_hakk(name, comment):
    cur = get_db().cursor()
    t = str(time.time())
    Comment_info = (name, t, comment)
    cur.execute("INSERT INTO Comments VALUES (?, ?, ?)", Comment_info)
    get_db().commit()

@app.route("/")
def hello():
	Comments = db_read_Comments()
	print(Comments)
	return render_template('index.html', Comments=Comments)

@app.route("/api/hakk", methods =["POST"])
def receive_hakk():
	print(request.form)
	db_add_hakk(request.form['name'], request.form['comment'])
	return redirect("/")

@app.route("/api/display", methods =["GET"])
def display_hakk():
	Comments = [
		{
			'name': 'test_user',
			'comment': 'test commet here'
		},
		{
			'name': 'test_user2',
			'comment': 'test commet2 here'
		}]
	return render_template('index.html', Comments=Comments )

if __name__ == "__main__":
	app.run()
