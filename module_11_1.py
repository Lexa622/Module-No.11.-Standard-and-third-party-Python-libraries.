import requests
import numpy as np
import pandas as pd
r = requests.get('https://github.com/Lexa622/Module-No.-10.-Multithreading./blob/main/module_10_1.py',
                 auth=('user', 'pass'))
print(f"{r.status_code}\n {r.headers['content-type']}\n {r.encoding}")
s = pd.Series(np.arange(5), index=["Ноль", "Один", "Два", "Три", "Четыре"])
print(s)
s = pd.Series(np.linspace(1, 10, 8))
print(s)
