# SimpleHTTPFileServer
Simple HTTP Server With POST and PUT Upload.
This module builds on BaseHTTPServer by implementing the standard GET and HEAD requests in a fairly straightforward manner.



## Install

```
sudo python setup.py install
```



## Usage

```
➜  ~ SimpleHTTPFileServer
put example:
    curl -T xxx.txt 127.0.0.1:8000
    wget --method PUT -q -O - --body-file xxx.txt 127.0.0.1:8000/xxx.txt
Serving HTTP on 0.0.0.0:8000
```



## Upload

Upload file with one line command

```
curl -T xxx.txt 127.0.0.1:8000
```

```
wget --method PUT -q -O - --body-file xxx.txt 127.0.0.1:8000/xxx.txt
```



