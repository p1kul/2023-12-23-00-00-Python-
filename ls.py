import requests
import numpy as np
payload = {'key1':'value1','key2':'value2'}
r = requests.get('https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request/get',params=payload)
print(r.url)
d = requests.get('https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request/get',data=payload)
print(d.text)
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)