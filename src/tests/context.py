import os
import sys

# Insert parentdir of this file to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pycryptoaddress import AddressExtractor, Tokenizer