# Django Simple Live Chat Using Channels 
![alt text](https://i.imgur.com/YRyhUZt.jpg "image Title")
## Installation Guide:

- 1. python -m venv venv 
- 2. venv\Scripts\activate on windows  or source venv/bin/activate on linux
- 3. pip install -r requirements.txt 
- 4. python manage.py makemigrations 
- 5. python manage.py migrate
- 6. create two users i.e python manage.py createsuperuser  or normal user and login in admin 
- 7. python manage.py runserver 
- 8. go to localhost:8000/chat and type chatroom and using same chatroom on different browser keep chatting 

### It is a sample application , on production we need redis to maintian information of channel layers. 
