# coding=utf-8


class Base:

	def get_columns(self, filter_list=None):
		""":arg filter_list = List for columns to filter"""

		column_list = []
		for column in self.__table__.columns:
			if filter_list and (column.key not in filter_list):
				continue

			if column.key == 'id':
				continue

			if column.key.startswith('_'):
				continue

			if column.key.startswith('date_'):
				continue

			column_list.append(column.key)

		return column_list
