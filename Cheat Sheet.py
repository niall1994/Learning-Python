/Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8 -m pip install matplotlib

mkdir new_folder && cd new_folder
python3.8 -m venv venv 
python3.8 -m venv /Users/niallsheppard/virtual_environment



(base) niallsheppard@Nialls-Air ~ % source /Users/niallsheppard/virtual_environment/bin/activate
(virtual_environment) (base) niallsheppard@Nialls-Air ~ % which python
/Users/niallsheppard/virtual_environment/bin/python
(virtual_environment) (base) niallsheppard@Nialls-Air ~ % deactivate
(base) niallsheppard@Nialls-Air ~ % 

http://localhost:8050
    
git init
git add .
heroku create new-app
git push heroku master
heroku apps:destroy

mkdir

#django
django-admin startproject mysite
python manage.py startapp polls
python manage.py makemigrations polls
python manage.py migrate
python manage.py sqlmigrate polls 0001
python manage.py shell
python manage.py createsuperuser
