```
if request.method == 'POST':
        xml = request.form['xml']
        parser = etree.XMLParser(no_network=True, resolve_entities=False) # to enable network entity. see xmlparser-info.txt
```

By using no_network=True and resolve_entities=False, you prevent the XML parser from accessing external resources and resolving entities, which effectively mitigates XXE vulnerabilities.