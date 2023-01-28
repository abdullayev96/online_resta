from django import forms
from foods.models import Recipe, Ingredient, Step, Blog, GetInTouch, Followers


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.TextInput(attrs={'class': 'form-control'}),
            "prep_time": forms.TimeInput(attrs={'class': 'form-control'}),
            "cook_time": forms.TimeInput(attrs={'class': 'form-control'}),
            "stars": forms.NumberInput(attrs={'class': 'form-control'}),
            "posted_at": forms.DateInput(attrs={'class': 'form-control'}),
        }


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "order": forms.NumberInput(attrs={'class': 'form-control'}),
            "recipe": forms.Select(attrs={'class': 'form-control'}),
        }


class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "order": forms.NumberInput(attrs={'class': 'form-control'}),
            "recipe": forms.Select(attrs={'class': 'form-control'}),
        }


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.TextInput(attrs={'class': 'form-control'}),
            "author": forms.TextInput(attrs={'class': 'form-control'}),
            "prep_time": forms.TextInput(attrs={'class': 'form-control'}),
            "cook_time": forms.TextInput(attrs={'class': 'form-control'}),
            "posted_at": forms.DateInput(attrs={'class': 'form-control'}),
            "stars": forms.NumberInput(attrs={'class': 'form-control'}),
        }


class GetInTouchForm(forms.ModelForm):
    class Meta:
        model = GetInTouch
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "subject": forms.TextInput(attrs={'class': 'form-control'}),
            "message": forms.TextInput(attrs={'class': 'form-control'}),
            "sent_at": forms.DateTimeInput(attrs={'class': 'form-control'}),
        }


class FollowersForm(forms.ModelForm):
    class Meta:
        model = Followers
        fields = "__all__"
        widgets = {
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
        }
