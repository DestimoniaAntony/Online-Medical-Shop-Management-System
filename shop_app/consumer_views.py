from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from shop_app.models import Assign, Cart, Consumer, Medicine,Feedbacks, Pharmacy

class IndexView(TemplateView):
    template_name = 'consumer/index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)        
        med = Medicine.objects.all()
        context['medicine'] = med
        return context
class Shop_SingleView(TemplateView):
    template_name = "consumer/shop-single.html"
    
    def get_context_data(self, **kwargs):
        context = super(Shop_SingleView, self).get_context_data(**kwargs)
        id1 = self.request.GET['id']
        shop_single = Medicine.objects.get(id=id1)
        context['shop_single'] = shop_single
        return context
    
class Add(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.POST['id'] 
        qty=request.POST['req_quantity']
        med=Medicine.objects.get(id=id)
        med_name=med.med_name
        Tquantity=int(med.Tquantity)-int (qty)
        price=med.price
        total=int(qty)*int(price)
        med.Tquantity=int(med.Tquantity)-int (qty)
        med.save()
        re = Consumer.objects.get(user_id=self.request.user.id)
        ca=Cart()
        ca.medicine_id=id 
        ca.consumer_id=re.id
        ca.status = 'Added'
        ca.payment = 'NULL'
        ca.price=total
        ca.req_qnty=qty
        ca.med_name=med_name
        ca.Tquantity=Tquantity
        ca.save()       
        #return redirect(request.META['HTTP_REFERER'],{'message':"Item selected"})
        return redirect('/consumer')
        #return render(request,'consumer/cart.html',{'message':" Item selected"})
        
class CartView(TemplateView):
    template_name="consumer/cart.html"
    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)  
        user = Consumer.objects.get(user_id=self.request.user.id)      
        cart = Cart.objects.filter(status='Added',consumer_id=user.id)
        total = 0   
        for i in cart:
            total = total + int(i.price)
        context['sum'] = total
        context['cart'] = cart
        return context
class RejectcartView(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        id2= request.GET['id2']
        cart=Cart.objects.get(id=id)
        qty=cart.req_qnty
        med=Medicine.objects.get(id=id2)
        med.Tquantity=int(med.Tquantity)+int(qty)
        med.save()
        Cart.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'],{'message':"Removed"})
class PaymentView(TemplateView):
    template_name="consumer/checkout.html"
    def get_context_data(self, **kwargs):
        context = super(PaymentView, self).get_context_data(**kwargs)  
        user = Consumer.objects.get(user_id=self.request.user.id)      
        cart = Cart.objects.filter(status='Added',payment='NULL',consumer_id=user.id)
        total = 0   
        for i in cart:
            total = total + int(i.price)
        context['sum'] = total
        context['cart'] = cart
        context['consumer'] = user
        return context
class Waitng_View(TemplateView):
    template_name="consumer/waiting_conf.html"
class StatusView(TemplateView):
    template_name="consumer/status.html"
    def get_context_data(self, **kwargs):
        context = super(StatusView, self).get_context_data(**kwargs)  
        user = Consumer.objects.get(user_id=self.request.user.id)      
        cart = Cart.objects.filter(status="Accepted",consumer_id=user.id)
        total = 0
        for i in cart:
            total = total + int(i.price)
        context['asz'] = total
        context['cart'] = cart
        return context
class Payment(TemplateView):
    template_name="consumer/Payment.html"
    def get_context_data(self, **kwargs):
        context = super(Payment, self).get_context_data(**kwargs)  
        user = Consumer.objects.get(user_id=self.request.user.id)      
        cart = Cart.objects.filter(status="Accepted",consumer_id=user.id)
        total = 0
        for i in cart:
            total = total + int(i.price)
        context['asz'] = total
        context['cart'] = cart
        return context
class chpayment(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        user = Consumer.objects.get(user_id=self.request.user.id)      
        cart = Cart.objects.filter(status="Accepted",consumer_id=user.id)
        asg = Assign.objects.filter(status="Accepted",consumer_id=user.id)
        print(cart)
        for i in cart:
            i.payment = 'paid'
            i.status = 'paid'
            i.save()
        for i in asg:
            i.status = 'paid'
            i.save()
        return render(request,'consumer/thankyou.html',{'message':" payment Success"})
class Thank(TemplateView):
    template_name="consumer/thankyou.html"
class Feedback(TemplateView):
    template_name="consumer/feedback.html"
    def post(self, request, *args, **kwargs):
        id1=Consumer.objects.get(user_id=self.request.user.id)
        service = request.POST['service']
        messages = request.POST['message']
        reg = Feedbacks()
        reg.message=messages
        reg.service=service
        reg.consumer_id=id1.id
        reg.save()
        return redirect('/consumer', {'message': "Feedback Send"})
        