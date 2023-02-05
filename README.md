# FamPay_Assignment (YouTube data fetch)
API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.
-----------------------------------------------------------------------------------------------------------------
The server fetches latest videos async after every 10 minutes and saves it to the db.
![Dashboard](https://user-images.githubusercontent.com/47237661/216819618-2c9308be-09c3-44d8-a57b-4361ff697da5.jpg)

## Tools and Technoligies used
This whole backend code is Writtten in [Django](https://www.djangoproject.com/)
For Running the cron job which run every minute I have used [django_crontab](https://github.com/kraiz/django-crontab) which runs every minute in backend to fetch data and upload it on sqlite database.
![database](https://user-images.githubusercontent.com/47237661/216819654-a9adb3da-4050-4e42-8f7c-92549a317003.jpg)

The Videos are stored in a paginated response, sorted in descending order of published datetime.
![Pagination](https://user-images.githubusercontent.com/47237661/216819661-de500f7b-7401-47ea-a593-dfd6b944b56d.jpg)

Implement Search Autocomplete For Input Fields in Django
![search](https://user-images.githubusercontent.com/47237661/216819643-ae8c44d6-dff1-4edc-af5a-f0ebe6bf780e.PNG)


This project is completely Dockerize

## SETUP GUIDE

- Clone the Project
- Create Virtual env (Optional)
- (optional) Run `docker-compose up`  to run the app in conatinerise enviornment.
- Type `pip install -r requirements.txt` in the terminal to install all dependencies.
- You will need YouTube Data Api key [This](https://developers.google.com/youtube/v3/getting-started)
- Add key in `settings.py` file
- To set up the Cron Job usin `django_crontab` follow [This](https://pypi.org/project/django-crontab/) 
- -- (Optional) If You are setting up the jobs or running any command in docker container just add `docker exec` before every command.
- -- For locally to run the server you can use `python mange.py runserver`.
