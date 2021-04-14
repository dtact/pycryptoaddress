import re
import base58
import hashlib
import binascii

from .tokenizer import Tokenizer

bitcoin = re.compile(r"^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$")
ethereum = re.compile(r"^0x[a-fA-F0-9]{40}$")
litecoin = re.compile(r"^[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}$")
monero = re.compile(r"^[48][0-9AB][123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{93}$")
bitcoin_cash = re.compile(r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}|^bitcoincash:?[q|p][a-z0-9]{41}|^BITCOINCASH:?[Q|P][A-Z0-9]{41}$")
zcash = re.compile(r"^t1[a-zA-Z0-9]{33}$")
dash = re.compile(r"^X[1-9A-HJ-NP-Za-km-z]{33}$")

def validate_litecoin(x):
	if not litecoin.match(x):
		return False

	try:
		base58Decoder = base58.b58decode(x).hex()
	except ValueError as exc:
		return False

	return True

def validate_bitcoin(x):
	if not bitcoin.match(x):
		return False

	try:
		base58Decoder = base58.b58decode(x).hex()
	except ValueError as exc:
		return False

	prefixAndHash = base58Decoder[:len(base58Decoder)-8]
	checksum = base58Decoder[len(base58Decoder)-8:]

	hash = prefixAndHash
	for x in range(1,3):
		hash = hashlib.sha256(binascii.unhexlify(hash)).hexdigest()

	return (checksum == hash[:8])

validators = (
	("bitcoin", validate_bitcoin),
	("ethereum", lambda x: ethereum.match(x)),
	# ("litecoin", validate_litecoin),
	("monero", lambda x: monero.match(x)),
	# ("bitcoin_cash", lambda x: bitcoin_cash.match(x)),
	("zcash", lambda x: zcash.match(x)),
	("dash", lambda x: dash.match(x)),
)

class AddressExtractor:
	def __init__(self):
		pass

	"""
	def findall(self, txt):
	results = []
	for elke regex in mapping:
		results += re.findall(regex, tx)
	return results
	"""

	def finditer(self, txt):
		for (token, start, end) in Tokenizer(txt):
			for (name, validator) in validators:
				result = validator(token)
				if result:
					yield (name, token, start, end)

	def match(text):
		pass
