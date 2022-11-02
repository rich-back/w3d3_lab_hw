from models.order import *
from datetime import datetime

now = datetime.now()


order1 = Order("Mar", now, 1, "MARgherita", "Olives", "Deep Pan")
order2 = Order("Colette", now, 2, "Hawaiian", "Cheese", "Romana")
order3 = Order("Keith", now, 5, "Pepperoni", "Sausage", "Stuffed Crust")
orders = [order1, order2, order3]