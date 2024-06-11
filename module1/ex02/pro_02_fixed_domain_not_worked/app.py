from flask import Flask, request
import os
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <html>
    <head><title>SSRF + LFI fixed Example</title></head>
    <body>
        <h1>SSRF + LFI fixed Example</h1>
        <form method="GET" action="/fetch">
            <label for="url">Enter URL:</label>
            <input type="text" id="url" name="url">
            <button type="submit">Fetch URL</button>
        </form>
        <div id="content"></div>
    </body>
    </html>
    """

@app.route('/fetch', methods=['GET'])
def fetch():
    url = request.args.get('url')
    if url:
        if url.startswith('file:///'):
            return "Access to local files is not allowed.", 403
        if not (url.startswith('http://') or url.startswith('https://')):
            return "Invalid URL scheme. Only http and https are allowed.", 400
        allowed_domains = ["https://www.google.com/", "https://www.google.fr/"]
        domain = url.split('/')[2]  # Extract the domain from the URL
        if domain not in allowed_domains:
            return "Domain not allowed.", 403
        try:
            response = requests.get(url, allow_redirects=False)
            content = response.text
            return """
            <html>
            <head><title>SSRF + LFI Result</title></head>
            <body>
                <h1>SSRF + LFI Result</h1>
                <div>Content fetched from URL:</div>
                <pre>{}</pre>
            </body>
            </html>
            """.format(content)
        except Exception as e:
            return "Error fetching content: {}".format(str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8010)