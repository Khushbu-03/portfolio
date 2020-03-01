from flask import Flask, render_template, url_for, redirect, request
app = Flask(__name__)
import csv
#print(app)

@app.route('/')
def my_home():
   return render_template('index.html')

@app.route('/<string:page_name>')
def about(page_name):
   return render_template(page_name)

def write_to_csv(data):
	with open('database.csv', newline='', mode ='a') as db:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_write = csv.writer(db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_write.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
		except:
			return 'Did not save to db!!'		
		return redirect('/thankyou.html')
	else:
		return 'Something went wrong!!'