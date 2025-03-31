from flask import Flask
import threading
import time
import requests

app = Flask(__name__)

URLS = ["https://example1.com", "https://example2.com"]  # Replace with your URLs

def ping_urls():
    while True:
        for url in URLS:
            try:
                response = requests.get(url)
                print(f"Pinged {url}: Status Code {response.status_code}")
            except Exception as e:
                print(f"Failed to ping {url}: {e}")
        time.sleep(300)  # Wait for 5 minutes (300 seconds)

# Start the pinging task in a separate thread
thread = threading.Thread(target=ping_urls, daemon=True)
thread.start()

@app.route('/')
def home():
    return "Flask app is running and pinging URLs!"

if __name__ == '__main__':
    app.run(debug=True)
