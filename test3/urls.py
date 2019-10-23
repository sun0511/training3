from django.contrib import admin
from django.urls import re_path, path
from graphene_django.views import GraphQLView
from test3.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^graphql$', GraphQLView.as_view(graphiql=True, schema=schema))

]