# how it work
- LOGIN SLACK
- COLLECTED PART OF THE LATEST CHANNEL MESSAGE  
- build and overite the xml to the `slack_devops_channel_rss.xml`
- HOST A SERVER TO PROVIDE THIS RSS FEED
# deploy
- install Selenium and Django
```
pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org Selenium
pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org Django
python3 manage.py runserver
```
# API
- GET(rss/) ? url="the slack channel url"
    - example - `http://127.0.0.1:8000/rss/?url=https://app.slack.com/client/TBKNBP9UJ/CLHLX1G3S/`  