from django.urls import path
from . import views
from django.urls import path
from .views import ProductDayCreateView, ProductDayUpdateView, ProductDayDeleteView

urlpatterns = [
    path('create/', ProductDayCreateView.as_view(), name='product_day_create'),
    path('<int:pk>/update/', ProductDayUpdateView.as_view(), name='product_day_update'),
    path('<int:pk>/delete/', ProductDayDeleteView.as_view(), name='product_day_delete'),
]
