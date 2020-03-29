# coding=utf-8

from flask_dance.consumer.storage.sqla import OAuthConsumerMixin
from flask_security import SQLAlchemyUserDatastore, Security

from app.backend.database import db
from app.backend.database.models.role import Role
from app.backend.database.models.user import User


class OAuth(OAuthConsumerMixin, db.Model):
	provider_user_id = db.Column(db.String(255), unique=True, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
	user = db.relationship(User)


# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(datastore=user_datastore)
