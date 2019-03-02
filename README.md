# PyRTK

PyRTK allows you to create and decode refresh tokens for JSON Web Token authentication systems.


## Installing
You can install the package using pip or pipenv.

```
$ pip install pyrtk

$ pipenv install pyrtk
```

## Usage

```python
import pyrtk

>>> refresh_token = pyrtk.create_token({'identity': 'tester'}, 'secretKey')
'gAAAAABcetXLTFVJO_BjCHVF5xKKwCj1goqiU9uR4osHwxqNJ6Mnl1YWvQn-m6EjPs3wyIjsoB3-R70rj7XFl2GuU5u6Q-3Z7tSa1VeDVDiEHPL50hxa0SEMunwqT5lyc8XkyT-A8zdt'

>>> decoded_token = pyrtk.decode_token(refresh_token, 'secretKey')
{'identity': 'tester'}

```


Please note that the secret key must be urlsafe base64 encoded. You can use the function `generate_key()` to generate a random key.

```python
>>> key = pyrtk.generate_key()
b'hSwQxJETF2ISuk4fgUNmP1k8r1JkcSz2Ijrq8_wa_ws='
```
