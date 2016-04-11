from dashing.widgets import NumberWidget

from .models import APIUser
from .models import Meal
from .models import Order


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
