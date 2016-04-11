from dashing.widgets import NumberWidget
from .models import Meal


class MealWidget(NumberWidget):
    title = 'Meals'

    def get_value(self):
        return Meal.objects.count()

    def get_detail(self):
        return 'Number of active meals'

    def get_more_info(self):
        return 'more info gets in here'
