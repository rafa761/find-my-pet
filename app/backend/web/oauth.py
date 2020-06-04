# coding=utf-8

from flask import flash
from flask_dance.consumer import oauth_authorized, oauth_error
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from flask_dance.contrib.google import make_google_blueprint
from flask_security import current_user, login_user
from sqlalchemy.orm.exc import NoResultFound

from app.backend.database import db
from app.backend.database.models.oauth import OAuth
from app.backend.database.models.user import User

oauth_blueprint = make_google_blueprint(
	scope=['profile', 'email', 'openid'],
	storage=SQLAlchemyStorage(OAuth, db.session, user=current_user)
)


# create/login local user on successful OAuth login
@oauth_authorized.connect_via(oauth_blueprint)
def google_logged_in(oauth_blueprint, token):
	if not token:
		flash('Failed to log in.', category='error')
		return False

	resp = oauth_blueprint.session.get('/oauth2/v1/userinfo')
	if not resp.ok:
		msg = 'Failed to fetch user info.'
		flash(msg, category='error')
		return False

	info = resp.json()
	user_id = info['id']

	# Find this Oauth token in the database, or create it
	query = OAuth.query.filter_by(provider=oauth_blueprint.name, provider_user_id=user_id)
	try:
		oauth = query.one()

	except NoResultFound:
		oauth = OAuth(provider=oauth_blueprint.name, provider_user_id=user_id, token=token)

	if oauth.user:
		login_user(oauth.user)
	else:
		# Create a new local user account for this user
		# TODO: Check how to define a default to the required fields
		user = User(
			username=info.get('given_name', '').lower(),
			first_name=info.get('given_name'),
			last_name=info.get('family_name'),
			email=info['email'],
			is_active=True
		)

		# Associate the new local user account with the OAuth token
		oauth.user = user

		# Save and commit
		db.session.add_all([user, oauth])
		db.session.commit()

		# Log in the new local user account
		login_user(user)
	flash('Successfuly signed in.')

	# Disable Flask-Dance's default behavior for savinf the OAuth token
	return False


# notify on OAuth provider error
@oauth_error.connect_via(oauth_blueprint)
def google_error(oauth_blueprint, message, response):
	msg = f'OAuth error from {oauth_blueprint.name}! message={message} response={response}'
	flash(msg, category='error')
