Sanitize User Input:

    The sanitize function ensures that any HTML special characters in the user input are escaped.
    This prevents any inserted scripts from being executed.

Use textContent Instead of innerHTML:

    By setting textContent, the user input is treated as plain text and not HTML.
    This prevents any HTML or JavaScript from being executed, effectively neutralizing the XSS attack vector.