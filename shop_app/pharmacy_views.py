from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from shop_app.models import Assign, Cart, Consumer, Medicine, Pharmacy, UserType
from django.template.loader import get_template
from xhtml2pdf import pisa

class IndexView(TemplateView):
    template_name = 'pharmacy/index.html'
class OrdersView(TemplateView):
    template_name = 'pharmacy/medicine_req.html'
    def get_context_data(self, **kwargs):
        context = super(OrdersView, self).get_context_data(**kwargs) 
        id1=Pharmacy.objects.get(pharmacy_id=self.request.user.id) 
        # ph=Cart.objects.filter(pharmacy_id=id1,status="Assigned")   
        asg = Assign.objects.filter(status="Assigned",pharmacy_id=id1)
        context['asg'] = asg   
        return context 
    def post(self, request, *args, **kwargs):
        id=request.POST['id']
        sta=request.POST['status']
        s=Assign.objects.get(id=id)
        s.status = sta
        s.save()
        c=Cart.objects.get(id=s.cart_id)
        c.status = sta
        c.save()
        return redirect('/pharmacy')
class ViewTabletMedicine(TemplateView):
    template_name='pharmacy/view_medicine.html'
    def get_context_data(self, **kwargs):
        context = super(ViewTabletMedicine, self).get_context_data(**kwargs)        
        med = Medicine.objects.filter(consume_type="Tablet")
        context['medicine'] = med
        return context
class ViewLqdMedicine(TemplateView):
    template_name='pharmacy/view_medicine.html'
    def get_context_data(self, **kwargs):
        context = super(ViewLqdMedicine, self).get_context_data(**kwargs)        
        med = Medicine.objects.filter(consume_type="Liquid")
        context['medicine'] = med
        return context
class ViewtpclMedicine(TemplateView):
    template_name='pharmacy/view_medicine.html'
    def get_context_data(self, **kwargs):
        context = super(ViewtpclMedicine, self).get_context_data(**kwargs)        
        med = Medicine.objects.filter(consume_type="Topical")
        context['medicine'] = med
        return context
class ViewdrpsMedicine(TemplateView):
    template_name='pharmacy/view_medicine.html'
    def get_context_data(self, **kwargs):
        context = super(ViewdrpsMedicine, self).get_context_data(**kwargs)        
        med = Medicine.objects.filter(consume_type="Drops")
        context['medicine'] = med
        return context
class ViewinhalersMedicine(TemplateView):
    template_name='pharmacy/view_medicine.html'
    def get_context_data(self, **kwargs):
        context = super(ViewinhalersMedicine, self).get_context_data(**kwargs)        
        med = Medicine.objects.filter(consume_type="Inhalers")
        context['medicine'] = med
        return context
class ViewinjectionsMedicine(TemplateView):
    template_name='pharmacy/view_medicine.html'
    def get_context_data(self, **kwargs):
        context = super(ViewinjectionsMedicine, self).get_context_data(**kwargs)        
        med = Medicine.objects.filter(consume_type="Injections")
        context['medicine'] = med
        return context
class Shop_SingleView(TemplateView):
    template_name = "pharmacy/shop-single.html"
    
    def get_context_data(self, **kwargs):
        context = super(Shop_SingleView, self).get_context_data(**kwargs)
        id1 = self.request.GET['id']
        shop_single = Medicine.objects.get(id=id1)
        context['shop_single'] = shop_single
        return context
class ViewReportTable(TemplateView):
    template_name = "pharmacy/view_report.html"    
    def get_context_data(self, **kwargs):
        context = super(ViewReportTable, self).get_context_data(**kwargs)        
        med = Medicine.objects.all()
        context['medicine'] = med
        return context
def reportview(request):
    rm=Medicine.objects.all()
    template_path = 'pharmacy/report.html'
    context = {'rm': rm}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;filename="vaccine_appo.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
    html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response