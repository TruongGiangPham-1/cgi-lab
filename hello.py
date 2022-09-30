#!/usr/bin/env python3

# code from 2021 404 lab 3
import os
import json

#PRINT OUT ALL ENV VARIABLES AS PLAIN TEXT
#print("Content-Type: text/plain") # let browser know to expect plain text
#print()
#print(os.environ)


#print ENV VARIABLES AS JSAON

print("Content-Type: application/json") # let browser know to expect json
print()
print(json.dumps(dict(os.environ), indent=2))  # print with nice formatting

#print only the query string
#print("Content-TYpe: text/html")
#print()
#print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")