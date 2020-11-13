# all creation process  

```
pip install django
django-admin startproject sysimibio .
cd sysimibio
manage startapp core
```

1. add app on INSTALLED_APPS
1. Create uls rout on urls.py (not forget to import from project.app.view)
1. Create view 
```
def home(request):
    return render(request, 'index.html')
```
1. Create index.html
1. best practices:
    1. SECRET_KEY, DEBUG, DATABASES and ALLOWED_HOSTS config on setting and .env
    1. Create .env
    1. Change wisg.py using Cling
    1. create Procv
1. Heroku:
    1. login and create app
    1. `cat .env` all this will be set on heroku  
    1. deploy
```
heroku apps:create sysimibio

cat .env

heroku config:set SECRET_KEY=!a3rçkds...sdsd?'
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=.herokuapp.com

git push heroku master -- force
```
