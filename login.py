#!/usr/bin/env python3


# code from winter 2021 compute 404 lab 3
import cgi
import cgitb

cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect

import secret
import os
from http.cookies import SimpleCookie

#CREATE SIMPLE LOGIN FORM
#set up cgi form
s= cgi.FieldStorage() # where all the posted data will sta
username = s.getfirst("username")
password = s.getfirst("password")

#check if correct login info provided to cgi form
form_ok = username == secret.username and password == secret.password

# set up cookie
cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None
if cookie.get("username"):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_password = cookie.get("password").value

#check if cookie username/pass == secret username/pass
# make sure cookie info hasnt changed
cookie_ok = cookie_username == secret.username and cookie_password == secret.password

if cookie_ok: # thing in cookie is correct login info
    # once we refresh WE STAY LOGGED IN 
    # so user doesnt have to type in user and pass so we can auto fill it yourseld
    username = cookie_username
    password = cookie_password



# form this point on, everything prints to html
print("Content-Type: text/html")

if form_ok:
    # user entered correct ingi
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")

print()

# laod login page, print user info

if not username and not password:  # if user didnt submitted anythijng in the form
    print(login_page())
elif username == secret.username and password == secret.password:  # if user enter correctly we goto secret pg
    print(secret_page(username, password))
else:  # else print login page and print info the form received
    print(after_login_incorrect())
    
    # use cooki so when user login they dont have to login again as long is cooki is there