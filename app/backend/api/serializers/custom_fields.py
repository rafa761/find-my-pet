# coding=utf-8

import re

EMAIL_REGEX = re.compile(r'\S+@\S+\.\S+')

from flask import abort
from flask_restplus import fields


class Email(fields.String):
	""" Custom Email Field """
	__schema_type__ = 'string'
	__schema_format__ = 'email'
	__schema_example__ = 'email@domain.com'

	def validate(self, value):
		if not value:
			return False if self.required else True
		return bool(EMAIL_REGEX.match(value))
