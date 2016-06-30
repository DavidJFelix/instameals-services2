from dashing.widgets import NumberWidget
from django.db.models import Avg

from .models import APIUser
from .models import Meal
from .models import Order
from .models import Price


class MealWidget(NumberWidget):
    title = 'Meals'

    def get_value(self):
        return Meal.objects.filter(is_active=True).count()

    def get_detail(self):
        return 'Number of active meals'


class UserWidget(NumberWidget):
    title = 'Users'

    def get_value(self):
        return APIUser.objects.count()

    def get_detail(self):
        return 'Number of users'


class OrderWidget(NumberWidget):
    title = 'Orders'

    def get_value(self):
        return Order.objects.count()

    def get_detail(self):
        return 'Number of Orders'


class AverageOrderPriceWidget(NumberWidget):
    title = 'Order Price'

    def get_value(self):
        avg_order_price = Order.objects.filter(buyer_price__currency='USD'). \
            aggregate(Avg('buyer_price__value')). \
            get('buyer_price__value__avg', None)
        if avg_order_price is None:
            return "$ 0.00"
        else:
            return "$ {0:.2f}".format(avg_order_price)

    def get_detail(self):
        return 'Avg Price of an Order'


class AverageMealPriceWidget(NumberWidget):
    title = 'Meal Price'

    def get_value(self):
        avg_meal_price = Meal.objects.filter(price__currency='USD'). \
            aggregate(Avg('price__value')). \
            get('price__value__avg', None)
        if avg_meal_price is None:
            return "$ 0.00"
        else:
            return "$ {0:.2f}".format(avg_meal_price)

    def get_detail(self):
        return 'Average Price of a Meal'
