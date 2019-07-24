# how it work
- LOGIN SLACK
- COLLECTED ALL THE CHANNEL MESSAGE  
begin from the latest ones      
this is a loop (from first one)
    1. get the created time. save it into array
    2. get the text string, save it into array
    5. store that url link into string. save it into array
- build and overite the xml to the `slack_devops_channel_rss.xml`
# deploy
```
pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org Django
python3 server/manage.py runserver
```
# API
- GET(rss/) ? url="the slack channel url"
    - example - `http://127.0.0.1:8000/rss/?url=https://app.slack.com/client/TBKNBP9UJ/CLHLX1G3S/`  