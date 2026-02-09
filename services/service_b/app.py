from flask import Flask
import random
import time

app = Flask(__name__)

@app.route("/health")
def health():
    time.sleep(random.uniform(0, 0.3))
    if random.random() < 0.85:
        return {"status": "OK"}, 200
    return {"status": "FAIL"}, 500

@app.route("/work")
def work():
    return {"message": "Services B running"}, 200

if __name__== "__main__":
    app.run(host="0.0.0.0", port=5002)

