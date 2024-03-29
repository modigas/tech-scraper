# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


from scrapy_djangoitem import DjangoItem
from products.models import BaseModel, Category


class ScraperItem(DjangoItem):
    django_model = BaseModel


class ScraperCats(DjangoItem):
    django_cats = Category
