# urls.py
from django.urls import path,include
from .views import PropertyListCreateView, PropertyRetrieveUpdateDestroyView, PropertySearchByCityView

urlpatterns = [
    # path('api-auth/', include('rest_framework.urls')),
    path('properties/', PropertyListCreateView.as_view(), name='property-list-create'),
    path('properties/<int:pk>/', PropertyRetrieveUpdateDestroyView.as_view(), name='property-retrieve-update-destroy'),
    path('properties/search/', PropertySearchByCityView.as_view(), name='property-search-by-city'),
]
