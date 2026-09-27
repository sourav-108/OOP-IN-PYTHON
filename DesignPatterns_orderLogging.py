from functools import wraps


def log_action(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Starting order action")
        result = function(*args, **kwargs)
        print("Order action finished")
        return result
    return wrapper


class Order:
    @log_action
    def confirm(self, order_id):
        return f"Order {order_id} confirmed"


print(Order().confirm("B208"))