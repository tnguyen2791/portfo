from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data ["email"]
        subject = data["subject"]
        message = data ["message"]
        csv_writer = csv.writer(database2, lineterminator='\n', delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':ˇ
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            print(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong try again'