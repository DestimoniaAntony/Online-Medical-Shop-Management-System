from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate

from shop_app.models import Consumer, Medicine, UserType
# Create your views here.
def demo(request):
    return render(request,'index.html')
class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)        
        med = Medicine.objects.all()
        context['medicine'] = med
        return context
class SignInView(TemplateView):
    template_name = 'signin.html'

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "consumer":
                    return redirect('/consumer')
                elif UserType.objects.get(user_id=user.id).type == "pharmacy":
                    return redirect('/pharmacy')
            else:
                return render(request, 'signin.html', {'message': " User Account Not Authenticated"})


        else:
            return render(request, 'signin.html', {'message': "Invalid Username or Password"})
class SignUpView(TemplateView):
    template_name = 'signup.html'
    def post(self, request, *args, **kwargs):
        name = request.POST['con_name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        password = request.POST['password']

        if User.objects.filter(email=email):
            print('pass')
            return render(request, 'signup.html', {'message': "already added the username or email"})

        else:
            user = User.objects.create_user(username=email, password=password, first_name=name, email=email,
                                            is_staff='0', last_name='1')
            user.save()
            reg = Consumer()
            reg.user = user
            reg.con_name = name
            reg.email = email
            reg.address = address
            reg.phone = phone
            reg.password = password    
            
            reg.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "consumer"
            usertype.save()

            return render(request, 'index.html', {'message': "Consumer added successfully"})
        