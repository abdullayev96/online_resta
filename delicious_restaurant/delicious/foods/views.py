from django.shortcuts import render
from dashboard.views import login_required_decorator
from .models import Followers, Ingredient, GetInTouch, Blog, Step, Recipe



def home_page(request):
    stars = [1, 2, 3, 4, 5]

    if request.POST:
        model = Followers()
        model.email = request.POST.get('email', '')
        if model.email:
            model.save()

    ctx = {
        'foods': Recipe.objects.all()[1:],
        'taomlar': Recipe.objects.all()[:3],
        'cooks': Blog.objects.all(),
        'stars': stars
    }

    return render(request, 'food/index.html', ctx)


@login_required_decorator
def contact_page(request):
    if request.POST:
        model = GetInTouch()
        model.name = request.POST.get('name', '')
        model.email = request.POST.get('email', '')
        model.subject = request.POST.get('subject', '')
        model.message = request.POST.get('message', '')
        model.save()

        model = Followers()
        model.email = request.POST.get('email', '')
        if model.email:
            model.save()
    return render(request, 'food/contact.html')


@login_required_decorator
def receipes_page(request):
    stars = [1, 2, 3, 4, 5]

    cooks = Recipe.objects.all()
    ctx = {
        'cooks': cooks,
        'stars': stars
    }
    return render(request, 'food/receipes.html', ctx)


@login_required_decorator
def blog_page(request, blog_id=1):
    blog = Blog.objects.get(pk=blog_id)
    stars = [1, 2, 3, 4, 5]
    ctx = {
        'cooks': Blog.objects.all(),
        'bloglar': Blog.objects.all(),
        'stars': stars,
        'cooking': blog
    }
    return render(request, 'food/blog-post.html', ctx)


@login_required_decorator
def receipe_post_page(request, receipe_id):
    if request.POST:
        model = GetInTouch()
        model.name = request.POST.get('name', '')
        model.email = request.POST.get('email', '')
        model.subject = request.POST.get('subject', '')
        model.message = request.POST.get('message', '')
        model.save()

    recipe = Recipe.objects.get(pk=receipe_id)
    steps = Step.objects.filter(recipe_id=receipe_id)
    ingredients = Ingredient.objects.filter(recipe_id=receipe_id)
    stars = [1, 2, 3, 4, 5]
    ctx = {
        'cooks': recipe,
        'steps': steps,
        'ingres': ingredients,
        'stars': stars,
    }
    return render(request, 'food/receipe-post.html', ctx)
