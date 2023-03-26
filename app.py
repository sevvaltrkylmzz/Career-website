from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS =[
  {'id':1,
   'title':'Data Analyst',
   'location':'Istanbul, Turkey',
   'salary':'40.000$'},
  {'id':2,
   'title':'Data Scientist',
   'location':'San Francisco, USA',             
   'salary':'100.000$'},
  {'id':3,
   'title':'Backend Developer',
   'location':'Berlin, Germany'},
  {'id':4,
   'title':'Frontend Developer',
   'location':'Warsaw, Poland', 
  'salary':'30.000£'}
]

@app.route("/")
def hello_world():
    return render_template("home.html",jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__=='__main__':
  app.run(host='0.0.0.0', debug=True)