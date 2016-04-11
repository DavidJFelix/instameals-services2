from dashing.widgets import NumberWidget
from .models import Meal
from .models import APIUser


class MealWidget(NumberWidget):
    title = 'Meals'

    def get_value(self):
        return Meal.objects.count()

    def get_detail(self):
        return 'Number of active meals'

    def get_more_info(self):
        return 'more info gets in here'


class UserWidget(NumberWidget):
    title = 'Users'

    def get_value(self):
        return APIUser.objects.count()

    def get_detail(self):
        return 'Number of users'

    def get_more_info(self):
        return 'more info gets in here'
