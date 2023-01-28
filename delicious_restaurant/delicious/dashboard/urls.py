from django.urls import path
from .views import (dashboard_page, login_page, logout_page, recipe_create, recipe_list, recipe_edit, recipe_delete,
                    ingredient_create, ingredient_list, ingredient_edit, ingredient_delete,
                    step_create, step_list, step_edit, step_delete,
                    blog_create, blog_list, blog_edit, blog_delete,
                    getintouch_create, getintouch_list, getintouch_edit, getintouch_delete,
                    followers_create, followers_list, followers_edit, followers_delete,
                    )

urlpatterns = [
    path('dashboard/', dashboard_page, name='dashboard_page'),
    path("login/", login_page, name='login_page'),
    path("logout/", logout_page, name='logout_page'),

    path('recipe/list', recipe_list, name='recipe_list'),
    path('recipe/create', recipe_create, name='recipe_create'),
    path('recipe/<int:pk>/edit', recipe_edit, name='recipe_edit'),
    path('recipe/<int:pk>/delete', recipe_delete, name='recipe_delete'),

    path('ingredient/list', ingredient_list, name='ingredient_list'),
    path('ingredient/create', ingredient_create, name='ingredient_create'),
    path('ingredient/<int:pk>/edit', ingredient_edit, name='ingredient_edit'),
    path('ingredient/<int:pk>/delete', ingredient_delete, name='ingredient_delete'),

    path('step/list', step_list, name='step_list'),
    path('step/create', step_create, name='step_create'),
    path('step/<int:pk>/edit', step_edit, name='step_edit'),
    path('step/<int:pk>/delete', step_delete, name='step_delete'),

    path('blog/list', blog_list, name='blog_list'),
    path('blog/create', blog_create, name='blog_create'),
    path('blog/<int:pk>/edit', blog_edit, name='blog_edit'),
    path('blog/<int:pk>/delete', blog_delete, name='blog_delete'),

    path('getintouch/list', getintouch_list, name='getintouch_list'),
    path('getintouch/create', getintouch_create, name='getintouch_create'),
    path('getintouch/<int:pk>/edit', getintouch_edit, name='getintouch_edit'),
    path('getintouch/<int:pk>/delete', getintouch_delete, name='getintouch_delete'),

    path('followers/list', followers_list, name='followers_list'),
    path('followers/create', followers_create, name='followers_create'),
    path('followers/<int:pk>/edit', followers_edit, name='followers_edit'),
    path('followers/<int:pk>/delete', followers_delete, name='followers_delete'),

]