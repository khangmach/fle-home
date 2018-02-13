# Learning Equality site

This is the code for Learning Equality's homepage: [https://learningequality.org](https://learningequality.org) aka [http://leq.ngo](http://leq.ngo).

## Environment setup

1. Clone this repo
2. Make and activate a python virtualenv to install dependencies to
3. Install the dependencies with: `pip install -r requirements.txt`
4. Create a _local_settings.py_ file as a sibling to the _settings.py_ file. Inside, set `DEBUG = True` so that static files will load in dev mode
6. Set up the database: `python manage.py syncdb --migrate`
7. Run the server: `python manage.py runserver`

Notes:

* When you're done, deactivate your python virtualenv
* The map requires certain data files to use, and you will get an error if you try and view it at /map/ because they haven't been included in the repo


## Code review

Ping Carine to review content changes and Khang to review design changes.


## Testing and deployment

1. Run and test changes locally
2. Push to staging
3. Check that everything works as expected
2. Push to production

