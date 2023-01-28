from django.db import models


class Recipe(models.Model):
    TYPE = [(1, 'One star'), (2, 'Two stars'),
            (3, 'Three stars'), (4, 'Four stars'), (5, 'Five stars')]

    title=models.CharField(max_length=150, blank=False, null=False)
    description=models.CharField(max_length=150, blank=False, null=False)
    image=models.ImageField(upload_to='images/', blank=False, null=False)
    prep_time=models.CharField(max_length=150, blank=False, null=False)
    cook_time=models.CharField(max_length=150, blank=False, null=False)
    posted_at=models.DateField(auto_now_add=True, blank=False, null=False)
    stars=models.SmallIntegerField(
        blank=False, null=False, default=1,
        choices=TYPE
    )

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    order = models.IntegerField(blank=False, null=False)
    recipe = models.ForeignKey(Recipe, max_length=150, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

class Step(models.Model):
    title = models.CharField(max_length=500, blank=False, null=False)
    order = models.IntegerField(blank=False, null=False)
    recipe = models.ForeignKey(Recipe, max_length=150, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

class Blog(models.Model):
    TYPE1 = [
            (1, 'One star'), (2, 'Two stars'), (3, 'Three stars'), (4, 'four_stars'), (5, 'five stars')
        ]
    title=models.CharField(max_length=150, blank=False, null=False)
    description=models.CharField(max_length=1000, blank=False, null=False)
    author=models.CharField(max_length=150, blank=False, null=False)
    image=models.ImageField(upload_to='images/', blank=False, null=False)
    prep_time = models.IntegerField(blank=False, null=False)
    cook_time = models.IntegerField(blank=False, null=False)
    posted_at=models.DateField(blank=False, null=False)
    stars = models.SmallIntegerField(
        blank=False, null=False, default=1,
        choices=TYPE1
    )

    def __str__(self):
        return self.title

class GetInTouch(models.Model):
    name=models.CharField(max_length=150, blank=False, null=False)
    email=models.CharField(max_length=150, blank=False, null=False)
    subject=models.CharField(max_length=150, blank=False, null=False)
    message=models.TextField(max_length=150, blank=False, null=False)
    sent_at=models.DateTimeField(blank=False, null=True)

    def __str__(self):
        return self.name

class Followers(models.Model):
    email = models.EmailField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.email