# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-14 17:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instameals', '0006_auto_20160411_2327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'permissions': (('view_address', 'Can view address'),)},
        ),
        migrations.AlterModelOptions(
            name='allergen',
            options={'permissions': (('view_allergen', 'Can view allergen'),)},
        ),
        migrations.AlterModelOptions(
            name='apiuser',
            options={'permissions': (('view_api_user', 'Can view api user'),)},
        ),
        migrations.AlterModelOptions(
            name='favoriteseller',
            options={'permissions': (('view_favorite_seller', 'Can view favorite seller'),)},
        ),
        migrations.AlterModelOptions(
            name='meal',
            options={'permissions': (('view_meal', 'Can view meal'),)},
        ),
        migrations.AlterModelOptions(
            name='mealreview',
            options={'permissions': (('view_meal_review', 'Can view meal review'),)},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'permissions': (('view_order', 'Can view order'),)},
        ),
        migrations.AlterModelOptions(
            name='orderreview',
            options={'permissions': (('view_order_review', 'Can view order review'),)},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'permissions': (('view_rating', 'Can view review'),)},
        ),
        migrations.AlterModelOptions(
            name='sellerreview',
            options={'permissions': (('view_seller_review', 'Can view seller review'),)},
        ),
    ]
