IT
========

A web app which allows the user to login/signup and then book an appointment.

It also gives the functionality to chat at the time of the appointment.

Uses the Django auth system to provide user accounts; users are only able to
use the chat once logged in, and this provides their username details for the
chat.

Installation
------------

Manual installation
~~~~~~~~~~~~~~~~~~~~~~

Run::

	pip install -r requirements.txt
	
The MySQL settings are currently configured to a test database to change that 
change the database settings in Sample/Settings.py to your own database also change
the settings for database in server3.py.To run the web app on a network add your ip
to ALLOWED HOSTS in Settings.py and also change the ip address in server3.py and 
IT/Templates/chat2.html

Finally, run::

    python manage.py migrate
    python manage.py runserver
	python server3.py
# Counselling-Site
