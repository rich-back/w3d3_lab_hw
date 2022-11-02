class Order():

    # import datetime

    # date = datetime.datetime(2022, 11, 2)

    def __init__(self, customer_name, date, quantity, pizza_name, extra_topping, base_type):
        self.customer_name = customer_name
        self.date = date
        self.quantity = quantity
        self.pizza_name = pizza_name
        self.extra_topping = extra_topping
        self.base_type = base_type
        

        