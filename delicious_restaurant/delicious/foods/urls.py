from django.urls import path
from .views import home_page, contact_page, receipes_page, blog_page, receipe_post_page

urlpatterns = [
    path('', home_page, name='home'),
    path('contact/', contact_page, name='contact'),
    path('receipes/', receipes_page, name='receipes'),
    path('blog/', blog_page, name='blog'),
    path('blog/<int:blog_id>', blog_page, name='blog'),
    path('receipe_post/<int:receipe_id>',  receipe_post_page, name='receipe_post'),
]
