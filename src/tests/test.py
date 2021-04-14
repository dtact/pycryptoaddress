#!/usr/bin/env python3
import unittest

from context import AddressExtractor, Tokenizer

class TestTokenizer(unittest.TestCase):
	def test(self):
		index = 0

		tokens = ['test', 'test', 'test']

		tokenizer = Tokenizer("test test test")
		for token in tokenizer:
			self.assertEqual(tokens[index], token[0])
			index = index + 1

		self.assertEqual(index, len(tokens))


class TestParser(unittest.TestCase):
	cases = [
		("bitcoin", "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh"),
		("ethereum", "0xb794f5ea0ba39494ce839613fffba74279579268"),
		("litecoin", "MGxNPPB7eBoWPUaprtX9v9CXJZoD2465zN"),
		("monero", "4AdUndXHHZ6cfufTMvppY6JwXNouMBzSkbLYfpAV5Usx3skxNgYeYTRj5UzqtReoS44qo9mtmXCqY45DJ852K5Jv2684Rge"),
		# subaddress
		("monero", "888tNkZrPN6JsEgekjMnABU4TBzc2Dt29EPAvkRxbANsAnjyPbb3iQ1YBRk1UXcdRsiKc9dhwMVgN5S9cQUiyoogDavup3H"),
		("zcash", "t1KLGj3izuKveu1eFZUiwp3BEKHQAiYv2Z7"),
		("dash", "XfcLDYdv97tc8YYbQqmR1gxBdLq4xfPNdy"),
	]

	def test(self):
		extractor = AddressExtractor()

		for (type, address) in self.cases:
			found = 0

			for needle in extractor.finditer(f"test {address} {address} test2b"):
				self.assertEqual(needle[0], type)
				self.assertEqual(needle[1], address)
				found = found + 1

			self.assertEqual(found, 2, f"no matches found for {type}")

if __name__ == '__main__':
	unittest.main()
