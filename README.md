# JIRA Disable-User
***
### Synopsis
---
This project was developed to address the lack of REST API to disable JIRA Users

### Installation
---
In order to run this application you will need the following installed:

python3 (tested with 3.5.1) and libraries:

> Selenium (3.8.1)

Google Chrome Driver

> ChromeDriver (3.8.1)

Google Browser

> Chrome Browser (63)

### Steps to install Selenium:
```sh
$ pip install selenium
```

### Steps to install ChromeDriver

[Installation Steps found here](https://sites.google.com/a/chromium.org/chromedriver/downloads)

### Steps to install Chrome Browser
```sh
$ vi /etc/yum.repos.d/google-chrome.repo
```
Place the text below in the opened file:
```
[google-chrome]
name=google-chrome
baseurl=http://dl.google.com/linux/chrome/rpm/stable/$basearch
enabled=1
gpgcheck=1
gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub
```

As root install Chrome Browser:
```sh
$ yum install google-chrome-stable -y
```

### Running disable_jira_user script
```python
$ python3 disable_jira_user.py --user myname
```

### Notes
```
JIRA_SERVER = URL for your jira instance e.g. https://jira.corp.com
WEB_DRIVER_HOME = Location for extracted ChromeDriver
USER = JIRA Admin User
PASS = JIRA Admin Password

This Application can be run in either headless or non-headless mode. Default mode is headless
```