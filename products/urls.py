from django.urls import path
from .views import hx_add_view_cart_btn,hx_update_review,hx_alert_success


urlpatterns=[
    path('hx_add_view_cart_btn/<int:product_id>', hx_add_view_cart_btn, name='hx_add_view_cart_btn'),
    path('hx_update_review/<int:product_id>', hx_update_review, name='hx_update_review'),
    path('hx_alert_success/', hx_alert_success, name='hx_alert_success'),

]
