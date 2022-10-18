from django.urls import path
from products.views import product
from .views import frontpage,shop,signup,myaccount,edit_myaccount
from django.contrib.auth import views




urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),
    path('signup/', signup, name='signup'),
    path('myaccount/', myaccount, name='myaccount'),
    path('myaccount/edit', edit_myaccount, name='edit_myaccount'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
]