# pycryptoaddress

This library will extract crypto addresses from text (eg. tweets, pastebin, webpages, etc).


## Example
Extract the crypto addresses from the ransom note.

``` python
from pycryptoaddress import AddressExtractor 
extractor = AddressExtractor()

for extract in extractor.finditer("""You need make payment deposit to this coding our address give you instruction
 
Address BTC 1CryptcfFKJJES1Gh5zAoFtmnPYLCRcMmY"""):
    print(extract)

```

# Creator

[DTACT](https://dtact.com/)

# Copyright and license

Code and documentation copyright 2011-2021 DTACT.

Code released under the Apache license.
