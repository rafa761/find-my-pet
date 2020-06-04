# coding=utf-8


class Base:

	def __predicate_attributes(self, attribute, filter):
		""" Check custom rules to ignore some attributes """
		if attribute == 'id':
			return False

		if attribute.startswith('_'):
			return False

		if attribute.startswith('date_'):
			return False

		return attribute in filter

	def get_self_attributes(self, attr_filter):
		""" To turn the updates queries dynamic for any class, this method get the self attributes
		and compares with the received filter
		It excludes some read_only fields and returns the list of attributes that can be changed
		:param: attr_filter - Iterable with the attributes to filter
		 """
		self_attributes = vars(self).keys()
		filter_attributes = [x for x in attr_filter]

		attributes_list = []
		for attr in self_attributes:
			if self.__predicate_attributes(attr, filter=filter_attributes):
				attributes_list.append(attr)

		return attributes_list
