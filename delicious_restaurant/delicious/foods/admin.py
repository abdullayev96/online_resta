from django.contrib import admin
from .models import Followers, Ingredient, GetInTouch, Blog, Step, Recipe

admin.site.register(Followers)
admin.site.register(Ingredient)
admin.site.register(GetInTouch)
admin.site.register(Blog)
admin.site.register(Step)
admin.site.register(Recipe)