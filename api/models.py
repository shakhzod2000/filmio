from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie


class MovieResource(ModelResource):
    class Meta:
        # queryset is query executed later (lazy loading, lazy object)
        queryset = Movie.objects.all()
        resource_name = 'movies' # after .../api/ URL
        excludes = ['date_created']
