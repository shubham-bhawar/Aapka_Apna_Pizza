from . import views

from django.urls import path



urlpatterns = [
    path('', views.index,name="ShopHome"),
    path('about/', views.about ,name="About"),
    path('contact/', views.contact,name="Contact"),
    path('tracker/', views.tracker,name="Tracker"),
    path('search/', views.search,name="Search"),
    path('product/<int:myid>', views.productview,name="Product"),
    path('checkout/', views.checkout,name="Checkout"),
]
