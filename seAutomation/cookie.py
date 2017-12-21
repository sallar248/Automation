#!/usr/bin/python

# Go to correct domain
driver.get("http://www.example.com")

# Now set the cookie, This one's valid for the entire domain
cookie = { 'name' : 'foo', 'value' : 'bar'}
driver.add_cookie(cookie)

# Add now output all the available cookies for the current URL
driver.get_cookies()


