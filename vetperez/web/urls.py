from django.urls import path
from web.views.home import HomeView,AboutUsView, ContactView,ProductsView
from web.views.store import StoreView,CartView
urlpatterns = [
    path('',HomeView.as_view()),
    path('quienes-somos',AboutUsView.as_view()),
    path('contactanos',ContactView.as_view()),
    path('productos',ProductsView.as_view()),
    path('tienda',StoreView.as_view()),
    path('carrito',CartView.as_view()),
]