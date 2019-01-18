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
import pyjwt

>>> refresh_token = pyrtk.create_token('userID', 'secretKey')
'gAAAAABcQR8IVD6nGbVItVUvgtzFM-eKnTVz2F00LwVHydXF0X4xv6WTRDPiEJax2Y342LTPxu2sWD6t83CyZFHY0g_-etcC_6g7JzzJ4IeWyL7MCHGvEWkPxEKETRCoYcnpJfM9MsxmfR5LDLArz3IYcnh85PC2sA=='

>>> decoded_token = pyrtk.decode_token(refresh_token, 'secretKey')
'{'user_id': 'userID', 'created': 1547771656.802478}'

```
