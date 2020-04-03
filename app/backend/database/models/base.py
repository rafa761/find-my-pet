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

		if filter:
			if not attribute in filter:
				return False

		return True

	def get_self_attributes(self, attr_filter=None):  # type: (Base, Any) -> List[str]
		""" Custom Method to get attributes from any class
		:param: attr_filter - Optional Iterable with the attributes to filter
		 """
		self_attributes = vars(self).keys()

		return [x for x in self_attributes if self.__predicate_attributes(x, filter=attr_filter)]
