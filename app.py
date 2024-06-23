from flask import Flask, json, jsonify, render_template, request, redirect, url_for, session

app = Flask(__name__) #create flack app
#part of the url after the domain name

JOBS = [
    {
        'id':1,
        'title': 'Data Analyst',   
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
        
    },

    {
        "id":2,
        'title': 'Data Sci',   
        'location': 'Dehli, India',
        'salary': 'Rs. 10,00,000'

    },
    {
        "id":3,
        'title': 'Data Engineer',   
        'location': 'Bengaluru, India',
        'salary': 'Rs. 12,00,000'

    },
    {
        "id":4,
        'title': 'Backend Analyst',   
        'location': 'USA',
        'salary': 'Rs. 15,00,000'

    },
]



#html endpoint
@app.route('/') #registered a route to the app.
def hello_world():
    return render_template ('home.html', 
                            jobs=JOBS)
#JSON endpoint
@app.route('/jobs')
def list_jobs():
    return jsonify(JOBS)
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True) #starts app
