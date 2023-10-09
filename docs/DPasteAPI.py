import requests

data = {
    "content": '''# 9 October 2023

from HostTor import VicksTor
import VicksTor as vix
vix.run_server('flask')

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1> Hello, World! </h1> <br> Welcome to Dark Web.'

if __name__ == '__main__':
    app.run(debug=False)
''', 

    "syntax": "python", 
    "expiry_days": 365
}

headers = {"User-Agent": "My Python Project"}
r = requests.post("https://dpaste.com/api/", data=data, headers=headers)
print(f"URL: {r.text}")

# Output:
# URL: https://dpaste.com/993CLNSDK
