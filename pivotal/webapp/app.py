#!/usr/bin/env python3

##################################################
# This is the main application file.
# It has been kept to a minimum using the design
# principles of Models, Views, Controllers (MVC).
##################################################

# Import modules required for app
import os
from flask import Flask, render_template, request
import models

# Create a Flask instance
app = Flask(__name__)

### Avoid to decode Nonetype that redis returns if getting empty key
def check_decode(v):
    return "NaN" if v is None else v.decode()

##### Define routes #####
@app.route('/')
def home():
    r = models.redis()
    temp = check_decode(r.get("temp"))
    humid = check_decode(r.get("humid"))
    timestamp = check_decode(r.get("timestamp"))
    return render_template('default.html', temp=temp, humid=humid, timestamp=timestamp)

##### Run the Flask instance, browse to http://<< Host IP or URL >>:5000 #####
if __name__ == "__main__":
	app.run(debug=False, host='0.0.0.0', port=int(os.getenv('PORT', '5000')), threaded=True)
