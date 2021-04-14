def is_seperator(v):
	return not (v.isalpha() or v.isdigit())

class Tokenizer:
	def __init__(self, value, is_seperator = is_seperator):
		self.value = value
		self.index = 0
		self.is_seperator = is_seperator
		pass

	def __iter__(self):
		index = self.index

		while index < len(self.value):
			if self.is_seperator(self.value[index]):
				yield (self.value[self.index:index], self.index, index)

				while index < len(self.value) and self.is_seperator(self.value[index]):
					index = index + 1

				self.index = index

			index = index + 1

		if self.index < index:
			yield (self.value[self.index:index], self.index, index)
