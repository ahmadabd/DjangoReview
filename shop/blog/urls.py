from django.urls import path
from . import views

urlpatterns = [

    # ex: hostname/blog
    path('', views.index, name = 'index'),

    # ex: hostname/blog/4
    path('<int:post_id>', views.detail, name = 'detail')
]
