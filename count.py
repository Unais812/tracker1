# this imports the flask image from the module flask to use in the code 
import os
from flask import Flask, render_template
import redis

redis_host=os.getenv('REDIS_HOST','redis')
redis_port=int(os.getenv('REDIS_PORT',6379))

app = Flask(__name__)
db = redis.Redis(host=redis_host, port=redis_port)  # <-- changed from localhost

@app.route('/')
def welcome_page():
    text = "Welcome to this page created by Unais, enjoy your stay!"
    return render_template('index.html', text=text)

@app.route('/count')
def store_count():
    visits = db.incr('visits')
    text = f"This page has been visited {visits} times."
    return render_template('count.html', text=text)

@app.route('/about')
def about_page():
    paragraphs = [ 
        "This project is more than just a visit counter, its a reflection of how far i have come on this journey into DevOps, " \
    "it showcases my passion and drive to become the youngest ever DevOps engineer, just a couple months ago i was completely oblivious to anything tech related" \
    " But now, this page which is currently being viewed has been made by me using a simple flask app code, containerised using a Dockerfile and docker-compose.yml file." \
    " I have also implemented the use of :" \
    " - volumes so that the container has persistent data storage for memory" \
    " - introduced nginx as a load balancer so the container can effortlessly handle increased traffic" \
    " - env variables so that the ports, hosts can be seamlessly changed rather than searching through the entire code to change the port number, host name" 
    ]
    return render_template('about.html', paragraphs=paragraphs)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)  # <-- use 0.0.0.0 for container