from django.shortcuts import render, redirect
from foods.models import Recipe, Ingredient, Step, Blog, GetInTouch, Followers
from .forms import RecipeForm, IngredientForm, StepForm, BlogForm, GetInTouchForm, FollowersForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def login_required_decorator(func):
    return login_required(func, login_url='login_page')


def login_page(request):
    if request.POST:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('recipe_list')
    return render(request, 'login.html')


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('home')


@login_required_decorator
def dashboard_page(request):
    return render(request, "food/index.html")


@login_required_decorator
def recipe_create(request):
    model = Recipe()
    form = RecipeForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    ctx = {
        'model': model,
        'form': form,
    }
    return render(request, "recipe/form.html", ctx)

@login_required_decorator
def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes": recipes
    }
    return render(request, "recipe/list.html", ctx)

@login_required_decorator
def recipe_edit(request, pk):
    model = Recipe.objects.get(pk=pk)
    form = RecipeForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'recipe/form.html', ctx)

@login_required_decorator
def recipe_delete(request, pk):
    model = Recipe.objects.get(pk=pk)
    model.delete()
    return redirect("recipe_list")


@login_required_decorator
def ingredient_create(request):
    model = Ingredient()
    form = IngredientForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("ingredient_list")
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'ingredient/form.html', ctx)

@login_required_decorator
def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    ctx = {
        'ingredients': ingredients
    }
    return render(request, 'ingredient/list.html', ctx)

@login_required_decorator
def ingredient_edit(request, pk):
    model = Ingredient.objects.get(pk=pk)
    form = IngredientForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("ingredient_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'ingredient/form.html', ctx)

@login_required_decorator
def ingredient_delete(request, pk):
    model = Ingredient.objects.get(pk=pk)
    model.delete()
    return redirect("ingredient_list")


@login_required_decorator
def step_create(request):
    model = Step()
    form = StepForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("step_list")
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'step/form.html', ctx)

@login_required_decorator
def step_list(request):
    steps = Step.objects.all()
    ctx = {
        'steps': steps
    }
    return render(request, 'step/list.html', ctx)

@login_required_decorator
def step_edit(request, pk):
    model = Step.objects.get(pk=pk)
    form = StepForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("step_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'step/form.html', ctx)

@login_required_decorator
def step_delete(request, pk):
    model = Step.objects.get(pk=pk)
    model.delete()
    return redirect("step_list")


@login_required_decorator
def blog_create(request):
    model = Blog()
    form = BlogForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("blog_list")
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'blog/form.html', ctx)

@login_required_decorator
def blog_list(request):
    blogs = Blog.objects.all()
    ctx = {
        'blogs': blogs
    }
    return render(request, 'blog/list.html', ctx)

@login_required_decorator
def blog_edit(request, pk):
    model = Blog.objects.get(pk=pk)
    form = BlogForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("blog_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'blog/form.html', ctx)

@login_required_decorator
def blog_delete(request, pk):
    model = Blog.objects.get(pk=pk)
    model.delete()
    return redirect("blog_list")


@login_required_decorator
def getintouch_create(request):
    model = GetInTouch()
    form = GetInTouchForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("getintouch_list")
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'getintouch/form.html', ctx)

@login_required_decorator
def getintouch_list(request):
    getintouches = GetInTouch.objects.all()
    ctx = {
        'getintouches': getintouches
    }
    return render(request, 'getintouch/list.html', ctx)

@login_required_decorator
def getintouch_edit(request, pk):
    model = GetInTouch.objects.get(pk=pk)
    form = GetInTouchForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("getintouch_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'getintouch/form.html', ctx)

@login_required_decorator
def getintouch_delete(request, pk):
    model = GetInTouch.objects.get(pk=pk)
    model.delete()
    return redirect("getintouch_list")


@login_required_decorator
def followers_create(request):
    model = Followers()
    form = FollowersForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("followers_list")
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'followers/form.html', ctx)

@login_required_decorator
def followers_list(request):
    followers = Followers.objects.all()
    ctx = {
        'followers': followers
    }
    return render(request, 'followers/list.html', ctx)

@login_required_decorator
def followers_edit(request, pk):
    model = Followers.objects.get(pk=pk)
    form = FollowersForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("followers_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'followers/form.html', ctx)

@login_required_decorator
def followers_delete(request, pk):
    model = Followers.objects.get(pk=pk)
    model.delete()
    return redirect("followers_list")