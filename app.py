from flask import Flask

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return "Hi this is the main page" + "<br><br><a href = '2'>Go to second page</a>"

@my_app.route('/2')
def second():
    return "This is the second page" + "<br><br><a href = 'http://127.0.0.1:5000/3'> On to third? </a>"

@my_app.route('/3') 
def third():
    return "This is the third page" + "<br><br><a href = '/'> Back to main </a>"

if __name__ == "__main__":
   my_app.debug = True
   my_app.run() #run the web app
