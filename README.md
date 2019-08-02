# pre
- add urls and credentials in `server/server/urls.ini`
# deploy
- dependences: Django, Selenium
```
pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org Django Selenium
nohup python3 manage.py runserver 0.0.0.0:8000 &
```
# API
- GET(rss/)"