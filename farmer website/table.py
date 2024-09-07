from flask import Flask, render_template
import MySQLdb
app = Flask("")

# Database configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'your_database'

# Initialize MySQL
db = MySQLdb.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    passwd=app.config['MYSQL_PASSWORD'],
    db=app.config['MYSQL_DB']
)

# Route to display data
@app.route('/')
def index():
    cursor = db.cursor()
    cursor.execute("SELECT id, name, price FROM products")
    data = cursor.fetchall()  # Fetch all data from the query
    return render_template('index.html', products=data)

if _name_ == '_main_':
    app.run(debug=True)