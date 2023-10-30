from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from shop_app.models import Assign, Cart, Consumer, Feedbacks, Medicine, Pharmacy, UserType
class IndexView(TemplateView):
    template_name = 'admin/index.html'
class AddMedicineView(TemplateView):
    template_name = 'admin/add_medicine.html'
    def post(self, request, *args, **kwargs):
        med_name = request.POST['med_name']
        image = request.FILES['image']
        ob = FileSystemStorage()
        obj = ob.save(image.name,image)
        description = request.POST['description']
        price = request.POST['price']
        Tquantity =request.POST['Tquantity']
        directions =request.POST['directions']
        side_effects =request.POST['side_effects']
        warnings =request.POST['warnings']
        consume_type =request.POST['consume_type']
        reg = Medicine()
        reg.image = obj
        reg.med_name = med_name
        reg.description = description
        reg.price = price 
        reg.Tquantity = Tquantity
        reg.directions = directions
        reg.side_effects = side_effects
        reg.warnings = warnings
        reg.consume_type = consume_type
        reg.save()
        return render(request, 'admin/add_medicine.html', {'message': "Medicine added successfully"})
class ViewMedicine(TemplateView):
    template_name = 'admin/view_medicine.html'
    def get_context_data(self, **kwargs):
        context = super(ViewMedicine, self).get_context_data(**kwargs)        
        med = Medicine.objects.all()
        context['medicine'] = med
        return context
class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id2 = request.GET['id']
        Medicine.objects.get(id=id2).delete()
        return redirect(request.META['HTTP_REFERER'], {'message': "Removed"})
class AddPharmacyView(TemplateView):
    template_name = 'admin/add_pharmacy.html'
    def post(self, request, *args, **kwargs):
        phar_names = request.POST['phar_name']
        image = request.FILES['image']
        ob = FileSystemStorage()
        obj = ob.save(image.name,image)
        locations = request.POST['location']
        phone_nu = request.POST['phone']
        email =request.POST['email']
        password =request.POST['phone'] 
        # phone number is used as password 
        if User.objects.filter(email=email):
            print('pass')
            return render(request, 'admin/add_pharmacy.html', {'message': "already added the username or email"})

        else:
            user = User.objects.create_user(username=email, password=password, first_name=phar_names, email=email,
                                            is_staff='0', last_name='1')
            user.save()
            reg = Pharmacy()
            reg.pharmacy = user
            reg.image = obj
            reg.phar_name = phar_names
            reg.location = locations
            reg.phone = phone_nu 
            reg.email = email
            reg.password = password
            reg.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "pharmacy"
            usertype.save()
            return render(request, 'admin/add_pharmacy.html', {'message': "Pharmacy added successfully"}) 
        
class ViewPharmacy(TemplateView):
    template_name = 'admin/view_pharmacy.html'
    def get_context_data(self, **kwargs):
        context = super(ViewPharmacy, self).get_context_data(**kwargs)        
        phar = Pharmacy.objects.all()
        context['pharmacy'] = phar   
        return context  
          
class RejectShopView(View):
    def dispatch(self, request, *args, **kwargs):
        id2 = request.GET['id']
        User.objects.get(id=id2).delete()
        return redirect(request.META['HTTP_REFERER'], {'message': "Removed"})
class AssignPharmacy(TemplateView):
    template_name ='admin/assign_pharmacy.html'
    def get_context_data(self, **kwargs):
        context = super(AssignPharmacy, self).get_context_data(**kwargs)       
        phar = Pharmacy.objects.all()
        cart = Cart.objects.filter(status="Added",payment="NULL")
        context['pharmacy'] = phar 
        context['cart'] = cart   
        return context 
    def post(self, request, *args, **kwargs):
        id = request.POST['id']
        pharmacy = request.POST['pharmacy']
        re = Cart.objects.get(id=id)
        qnt = re.req_qnty
        price = re.price
        ca = Assign()
        ca.pharmacy_id=pharmacy
        ca.consumer_id=re.consumer_id
        ca.medicine_id=re.medicine_id
        re.pharmacy_id=pharmacy
        ca.cart_id = re.id
        ca.req_qnty =qnt
        ca.price = price
        re.status="Assigned"
        ca.status = "Assigned"
        re.save()
        ca.save()
        return render(request, 'admin/index.html', {'message': "Assigned"})
class fbview(TemplateView):
    template_name='admin/feedback_view.html'

    def get_context_data(self, **kwargs):
    
        
        view_fb = Feedbacks.objects.all()
        context = {
            'viewfb':view_fb
        }
        return context

class ViewConsumer(TemplateView):
    template_name = 'admin/view_consumer.html'
    def get_context_data(self, **kwargs):
        context = super(ViewConsumer, self).get_context_data(**kwargs)        
        order = Cart.objects.filter(status="paid",payment="paid")
        context['completed_order'] = order   
        return context 