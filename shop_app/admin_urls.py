from django.urls import path

from shop_app.admin_views import IndexView,AddMedicineView,AddMedicineView,ViewMedicine,RejectView,AddPharmacyView,ViewPharmacy,RejectShopView,AssignPharmacy,fbview,ViewConsumer

urlpatterns = [
    
    path('',IndexView.as_view()),
    path('add_medicine',AddMedicineView.as_view()),
    path('view_medicine',ViewMedicine.as_view()),
    path('reject',RejectView.as_view()),
    path('add_pharmacy',AddPharmacyView.as_view()),
    path('view_pharmacy',ViewPharmacy.as_view()),
    path('reject_shop',RejectShopView.as_view()),
    path('assign_pharmacy',AssignPharmacy.as_view()),
    path('feedbackview',fbview.as_view()),
    path('view_ompleted_orders',ViewConsumer.as_view()),
]
def urls():
    return urlpatterns, 'admin', 'admin'