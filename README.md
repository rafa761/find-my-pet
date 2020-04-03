# find-my-pet
Tool for find, report and rescue lost pets, also useful to register homeless pets.

## Summary

Have you ever taught about how to help homeless or lost pets around the world, now you have the opportunity to help these little fluffy dogs, cats, etc to find a lovely owner.

## Modules, Docs, Sources

### Flask
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Flask Restplus](https://flask-restplus.readthedocs.io/en/stable/)
* [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* [Flask Dance](https://flask-dance.readthedocs.io/en/latest/)
* [Flask Caching](https://flask-caching.readthedocs.io/en/latest/)
* [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/)
* [Flask Security](https://pythonhosted.org/Flask-Security/)

### General
* [Google APIs](https://console.developers.google.com/projectselector2/apis/dashboard?pli=1&supportedpurview=project)

## Info

* The PostgreSQL database name is "**fmp**"

## Environments Variables

* FLASK_APP=pet.py
* FLASK_ENV=development
* FLASK_RUN_PORT=7000

### Google OAuth
* GOOGLE_OAUTH_CLIENT_ID='your client id'
* GOOGLE_OAUTH_CLIENT_SECRET='your client token'

If development environment:
* OAUTHLIB_RELAX_TOKEN_SCOPE=True
* OAUTHLIB_INSECURE_TRANSPORT=True
