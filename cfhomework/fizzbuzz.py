'''
multiple of 3 'Fizz' and 5 'Buzz' and both 'FizzBuzz'
'''
import os,sys
from flask import Flask
app = Flask(__name__)
@app.route("/")
#class FizzBuzz:
def numb():
    a=[]
    for i in range(1,101):
        if (i%3==0) and (i%5==0):
            a.append('FizzBuzz')
        elif (i%5)==0:
            a.append('Buzz')
        elif (i%3==0):
            a.append('Fizz')
        else:
            a.append(i)
    return str(a)
port = os.getenv('VCAP_APP_PORT', '5000')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port))


