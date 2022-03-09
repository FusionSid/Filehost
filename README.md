# Image storage API

**[Still in testing]**

URL: https://filehost.fusionsid.repl.co/

DOCS: https://filehost.fusionsid.repl.co/docs

Upload:

```py
import requests

url = "https://filehost.fusionsid.repl.co/api/upload"

files = {'file': open('file.png', 'rb')}
r = requests.post(url, files=files)
print(r.json()) 
```

Output:
```
{'code': 'code', 'url': 'url_to_where_its_stored'}
```

Get image:
make a request to the url returned from when you uploaded or do:
```https://filehost.fusionsid.repl.co/api/image?code={The code}```