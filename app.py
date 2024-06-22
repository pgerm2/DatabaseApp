from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__) #create flack app
#part of the url after the domain name
@app.route('/') #registered a route to the app.
def hello_world():
    return render_template ('home.html')
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True) #starts app