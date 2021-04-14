# pycryptoaddress


``` python
from pycryptoaddress import AddressExtractor 
extractor = AddressExtractor()

for extract in extractor.finditer("""You need make payment deposit to this coding our address give you instruction
 
Address BTC 1CryptcfFKJJES1Gh5zAoFtmnPYLCRcMmY"""):
    print(extract)

```

