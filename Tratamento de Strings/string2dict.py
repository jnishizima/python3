import json
s = "'A':22,'M':3,'d':18,'h':13,'m':7,'s':44"
s = "{" + s + "}"
json_acceptable_string = s.replace("'", "\"")
d = json.loads(json_acceptable_string)
print (d['A'])