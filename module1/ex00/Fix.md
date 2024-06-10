```
def render():
    user_input = request.form.get('input')
    safe_user_input = escape(user_input)
    template = f'Hello, {{ {safe_user_input} }}!'
    return render_template_string(index(), result=template)
```
Escape User Input: The escape function from flask ensures that any special characters in the user input are properly escaped, which prevents them from being interpreted as code by the template engine.
Safe Rendering: By using the escape function, we prevent the possibility of executing arbitrary code injected through user input.

With this approach, the user input is treated as plain text, preventing any malicious template code from being executed.


install escape:
```
pip install escape
```