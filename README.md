# FamPay_Assignment (YouTube data fetch)
API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.
-----------------------------------------------------------------------------------------------------------------
The server fetches latest videos async after every 10 minutes and saves it to the db.
![Homepage] (Screenshots/Dashboard.png)
 
## Tools and Technoligies used
This whole backend code is Writtten in [Django] (https://www.djangoproject.com/)
For Running the cron job which run every minute I have used [django_crontab] (https://github.com/kraiz/django-crontab) which runs every minute in backend to fetch data and upload it on sqlite database.
![database] (Screenshots/database.png)

The Videos are stored in a paginated response, sorted in descending order of published datetime.
![Pagination] (Screenshots/Pagination.png)

Implement Search Autocomplete For Input Fields in Django
![Search] (Screenshots/search.png)

This project is completely Dockerize

## SETUP GUIDE

- Clone the Project
- Create Virtual env (Optional)
- (optional) Run `docker-compose up`  to run the app in conatinerise enviornment.
- Type `pip install -r requirements.txt` in the terminal to install all dependencies.
- You will need YouTube Data Api key [This] (https://developers.google.com/youtube/v3/getting-started)
- Add key in `settings.py` file
- To set up the Cron Job usin `django_crontab` follow [This] (https://pypi.org/project/django-crontab/) 
- -- (Optional) If You are setting up the jobs or running any command in docker container just add `docker exec` before every command.
- -- For locally to run the server you can use `python mange.py runserver`
