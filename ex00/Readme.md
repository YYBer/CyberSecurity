1. Outputting User Input Directly into the DOM (DOM-based XSS):
```
function displayText() {
    var userInput = document.getElementById("inputText").value;
    document.getElementById("output").innerHTML = "<b>" + userInput + "</b>";
}
```

This part of the code directly inserts user input into the HTML without sanitization, making it vulnerable to XSS. 


2. Appending User Input as a Script (DOM-based XSS):
```
var script = document.createElement("script");
script.textContent = userInput;
document.body.appendChild(script);
```
This part of the code takes the user input and appends it as a script.An attacker could insert malicious JavaScript code that would be executed immediately.


3. display cookie
```
document.getElementById("output").innerHTML= document.cookie;
```


to run autotest, you need install:
```
pip3 install selenium
pip3 install selenium.webdriver
```