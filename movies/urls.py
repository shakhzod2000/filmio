from django.urls import path
from . import views # . is curr dir

# URLs starting with 'movies/'

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    # <> is to pass a parameter
    path('<int:movie_id>', views.detail, name='detail')
]
