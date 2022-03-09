# Image storage API

**[Still in testing]**


Upload:

```py
import requests

url = "{api_link}/api/upload"

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
```{Link to api}/api/image?code={The code}```