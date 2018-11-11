from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [

    # ex: hostname/blog
    path('', views.index, name = 'index'),

    # ex: hostname/blog/1
    path('<int:post_id>', views.detail, name = 'detail'),

    # ex: hostname/blog/archive/2018
    path('archive/<int:year>/', views.archiveYear, name = 'archive'),
]
