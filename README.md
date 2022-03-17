# File storage API

this is a temporary file hosting, the db does get cleared every so often. I might add a longer file host option but for now probably use this if you want to host a file for like a couple hours/minutes


Supported file types: png, txt, jpeg, gif, mp4, mp3  
Max file size: 15mb

---

Base URL: https://file-host.herokuapp.com/ (redirects to docs)

DOCS: https://file-host.herokuapp.com/docs

---

### Upload:

```py
import requests

url = "https://file-host.herokuapp.com/api/upload?file_type=png" # check file types above

files = {'file': open('file.png', 'rb'),}
r = requests.post(url, files=files)
print(r.json()) 
```

### Example Output:
```
{
  "code": "14kwDlNF",
  "url": "https://file-host.herokuapp.com/api/image?code=14kwDlNF"
}
```

---

### Get File:

You can either use the url tht was returned when you made uploaded the file or if you have the code you do:
```https://file-host.herokuapp.com/api/image?code={The code}```

---

###  Rate limits:

`GET /api/file` This endpoint is limited to 69 get files requests per minute

`POST /api/upload` This endpoint is limited to 42 uploads per minute

--- 

Also if you're using [Why Bot](https://github.com/FusionSid/Why-Bot), You can use the command `?filehost`
