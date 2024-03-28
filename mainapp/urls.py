from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
    path('store.html',views.store,name="store/"),
	path('cart.html', views.cart, name="cart"),
	path('checkout.html', views.checkout, name="checkout"),
    path('order.html',views.order,name = "order"),

]
