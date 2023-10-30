from django.urls import path

from shop_app.consumer_views import IndexView,Shop_SingleView,Add,CartView,RejectcartView,PaymentView,Thank,Waitng_View,StatusView,Payment,chpayment,Feedback


urlpatterns = [
    
    path('',IndexView.as_view()),
    path('shop_single',Shop_SingleView.as_view()),
    path('cart',Add.as_view()),
    path('view_cart',CartView.as_view()),
    path('remove',RejectcartView.as_view()),
    path('payment',PaymentView.as_view()),
    path('waiting',Waitng_View.as_view()),
    path('status',StatusView.as_view()),
    path('pay',Payment.as_view()),
    path('chpayment',chpayment.as_view()),
    path('thankyou',Thank.as_view()),
    path('feedback',Feedback.as_view()),
]
def urls():
    return urlpatterns,'consumer', 'consumer'