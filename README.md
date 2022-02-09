# News Authenticity

News filter Check the authenticity of the same news what we receive & response to someone's request
to confirm authenticity.



# Prerequisites

- Python >= 3.9.10
- Celery >= 5.1
- Redis server must be installed
- Postgres database

# Features

- Fetch news from news api.
- Display news list on Website.
- User can signup in the website
- User will be displayed news based on his preferences.
- User will receive the notification over the email for their preference category.
- User can set upvote and downvote to specific news if he is logged in else he can just see the news.


# Run on local

- Create virtualenv : ```admin@mhp:~$ virtualenv -p python3.9.10 env```
- Activate virtualenv: ```admin@mhp:~$ source env/bin/activate```
- Install all requirements : ```pip install -r requirements.txt```
- Create .env file in same directory where manage.py is placed. Please add all environment variables in it which is listed below.
- Create Database of postgres.
- Run : ```Python manage.py migrate```
- Create superuser and other users to execute the code. Also add the preference of user to get notification.
- Please load the fixtures. You can also add more category from admin panel. : ```python manage.py loaddata fixtures/category.json```
- Runserver : ```Python manage.py runserver```
- Run celery to execute task periodically. - ```celery -A news_authenticity worker --beat -l info```


# Future features

- Filter the news based on the category.
- Allow users to add their custom news.
- Display the votes for the news.
- Add Richtext box to add the news.

# Project Work Flow

- There are 2 celery task.
    - news_api_task : This is periodical task which will execute in every 30 mins. It will fetch latest news from the news API and store into database.  
    - send_notification_email : This will send the email to user once system fetch new news. It will only send the notification to the user if system find new news in their preference.
- When the website is hit then all the news are shown.
- User can see list of news on home page and if the user is logged in then user can up vote and down vote the specific news.

# Environment Variables

| Environment Variable   | Type   |
|------------------------|--------|
| SECRET_KEY             | String |
| EMAIL_HOST             | String |
| EMAIL_PORT             | String |
| EMAIL_BACKEND          | String |
| EMAIL_HOST_USER        | String |
| EMAIL_HOST_PASSWORD    | String |
| DB_ENGINE              | String |
| DB_NAME                | String |
| DB_USER                | String |
| DB_PASSWORD            | String |
| DB_HOST                | String |
| DB_PORT                | String |
| REDIS_URL              | String |
| BROKER_URL             | String |
| SERVER                 | String |
| CELERY_RESULT_BACKEND  | String |
| NEWS_API_ORG_API_KEY  | String |
