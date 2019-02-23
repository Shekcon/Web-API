from django.urls import path, re_path
from .views import result, watching, index

urlpatterns = [
    path('', index, name='results'),
    path('results/', result, name='results'),
    path('watch/<slug:id>', watching, name='watch')
]
