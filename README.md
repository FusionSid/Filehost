# Image storage API

**[Still in testing]**

URL: https://filehost.fusionsid.repl.co/

DOCS: https://filehost.fusionsid.repl.co/docs

### Upload:

```py
import requests

url = "https://filehost.fusionsid.repl.co/api/upload"

files = {'file': open('file.png', 'rb')}
r = requests.post(url, files=files)
print(r.json()) 
```

### Example Output:
```
{
  "code": "14kwDlNF",
  "url": "https://filehost.fusionsid.repl.co/api/image?code=14kwDlNF"
}
```

### Get image:

You can either use the url tht was returned when you made uploaded the file or if you have the code you do:
```https://filehost.fusionsid.repl.co/api/image?code={The code}```

###  Rate limits:

`GET /api/image` This endpoint is limited to 69 get image requests per minute

`POST /api/upload` This endpoint is limited to 42 uploads per minute