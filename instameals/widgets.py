from dashing.widgets import NumberWidget

from .models import APIUser
from .models import Meal
from .models import Order
from .models import Price
from django.db.models import Avg


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
    #we can group by currency, if needed.
    def get_value(self):
        avg_meal_price = Price.objects.all().aggregate(Avg('value'))
        print(avg_meal_price)
        if avg_meal_price['value__avg'] is None:
            return 0
        else:
            return avg_meal_price


    def get_detail(self):
        return 'Avg price of a Meal'
