# from flask import Flask
# app = Flask(__name__)
# 
# @app.route('/')
# def hello_geek():
#     return '<h1>Hello from Flask & Docker</h2>'
# 
# 
# if __name__ == "__main__":
#     app.run(debug=True)
	
from flask import Flask, jsonify
import mysql.connector as db
import os as os

app = Flask(__name__)

try:
  mydb = db.connect(
	host = os.environ.get('DBHOST'),
	user = os.environ.get('DBUSER'),
	password = os.environ.get('DBPASSWORD'),
	database = os.environ.get('DBNAME')
	)
  print ("Connection successful to " + os.environ.get('DBHOST'))
except Exception as e:
  print ("Connection unsuccessful due to " + str(e))
  

@app.route('/')
def index():
	# Execute a SELECT query
	cursor = mydb.cursor()
#     cursor.execute("SELECT * FROM S_GROUP_DESC")
	cursor.execute("SELECT * FROM cpi_inflation")
	results = cursor.fetchall()

	# Return the query results as JSON
	return jsonify(results)

if __name__ == '__main__':
	app.run()
