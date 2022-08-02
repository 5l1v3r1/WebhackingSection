import  requests
# Coded By youhacker55

url = input("enter the website to start your recon:")
r = requests.get("http://web.archive.org/cdx/search/cdx?url="+url+"%2F*&output=text&fl=original&collapse=urlkey&filter=statuscode%3A200")
print(r.text)