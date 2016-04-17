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


class AvgPriceWidget(NumberWidget):
    title = 'Price'

    # we can group by currency, if needed.
    def get_value(self):
        avg_meal_price = Price.objects.all(). \
            aggregate(Avg('value')). \
            get('value__avg', None)
        if avg_meal_price is None:
            return 0
        else:
            return avg_meal_price

    def get_detail(self):
        return 'Avg price of a Meal'
