from datetime import datetime
from models.order import *

now = datetime.now()


order1 = Order("Mar", now, 1)

print(order1.date)