from flask import Flask, request, render_template_string, escape

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
    <head>
        <title>Template Injection Fixed App</title>
    </head>
    <body>
        <h1>Template Injection Fixed App</h1>
        <form method="POST" action="/render">
            <label for="input">Enter your input:</label>
            <input type="text" id="input" name="input">
            <button type="submit">Render</button>
        </form>
        <div id="result">{{ result }}</div>
    </body>
    </html>
    '''

@app.route('/render', methods=['POST'])
def render():
    user_input = request.form.get('input')
    safe_user_input = escape(user_input)
    template = f'Hello, {{ {safe_user_input} }}!'
    return render_template_string(index(), result=template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010)
