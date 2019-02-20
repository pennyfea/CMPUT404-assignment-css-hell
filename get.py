import urllib.request

text_url = {"Frankenstein_Or_The_Modern_Prometheus":"http://www.gutenberg.org/files/84/84-h/84-h.htm", "Autographs": "http://www.gutenberg.org/files/58911/58911-h/58911-h.htm", "The_Adventures_Of_Tom_Sawyer": "http://www.gutenberg.org/files/74/74-h/74-h.htm" }
for key, val in text_url.items():
    request = urllib.request.urlopen(val)

    file = open(f"{key}.html", "w")
    file.write(str(request.read(), encoding = "ISO-8859-1"))
    file.close()




