Flask Basics and Template Injection Vulnerability (SSTI)

Template Injection Vulnerability (SSTI)
What is SSTI?

Server-Side Template Injection (SSTI) occurs when an attacker is able to inject malicious template code into a server-side template, allowing arbitrary code execution on the server. This is possible because templates are often rendered with high privileges, allowing access to sensitive data and system functions.

user input is directly embedded into the template string without any sanitization, making it vulnerable to SSTI. An attacker can input malicious code to execute arbitrary commands.

To prevent SSTI vulnerabilities, you should never directly embed user input into templates. Instead, use the proper templating mechanisms provided by the framework.

useful url: https://xz.aliyun.com/t/12163?time__1311=mqmhD5DK8GO8DsoYYK0%3DWPAKG%3DCD%3D%3DH54D&alichlgref=https%3A%2F%2Fwww.google.com%2F