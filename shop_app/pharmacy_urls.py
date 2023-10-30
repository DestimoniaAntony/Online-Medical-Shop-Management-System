from django.urls import path
from shop_app import pharmacy_views

from shop_app.pharmacy_views import IndexView,OrdersView,ViewTabletMedicine,ViewinjectionsMedicine,ViewtpclMedicine,ViewdrpsMedicine,ViewinhalersMedicine,Shop_SingleView,ViewReportTable,ViewLqdMedicine

urlpatterns = [
    
    path('',IndexView.as_view()),
    path('orders',OrdersView.as_view()),
    path('viewtabltmed',ViewTabletMedicine.as_view()),
    path('viewlqdtmed',ViewLqdMedicine.as_view()),
    path('viewdrpsmed',ViewdrpsMedicine.as_view()),
    path('viewtpclmed',ViewtpclMedicine.as_view()),
    path('viewinhalersmed',ViewinhalersMedicine.as_view()),
    path('viewinjectionsmed',ViewinjectionsMedicine.as_view()),
    path('shop_single',Shop_SingleView.as_view()),
    path('view_report',ViewReportTable.as_view()),
    path('report12',pharmacy_views.reportview,name="report")
]
def urls():
    return urlpatterns,'pharmacy', 'pharmacy'