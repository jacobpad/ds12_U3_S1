##  RUN THIS CODE IN MAC WITH  ##
##  FLASK_APP=hello.py flask run  ##

'''Minimal flask app'''

from flask import Flask

# Make the application
app = Flask(__name__) # Because I've imported Flask up top, I can use it here

# Make the rout
@app.route("/")

# Define a function
def hello():
    return "Hello World!"

###################################################################
# THIS MOST BASIC APP RETURNS THE FOLLOWING IN THE SERVER
# 127.0.0.1 - - [23/Mar/2020 16:17:09] "GET / HTTP/1.1" 200 -
# (ADDRESS - DATE / TIME - WHAT HAPPENED - ??? - SERVER CODE
# 
# SERVER CODES:
#   
###################################################################

