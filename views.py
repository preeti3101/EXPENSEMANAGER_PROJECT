from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from .forms import  DeveloperRegistrationForm
from django.contrib.auth.views import LoginView
from django.views.generic import FormView, TemplateView,ListView


# Create your views here.

class DeveloperRegisterView(CreateView):
    template_name = 'user/developer-register.html'
    model = User
    form_class = DeveloperRegistrationForm
    success_url = '/user/login/'   



class UserLoginView(LoginView): 
    template_name = 'user/login.html'
    model = User
    
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_manager:
                return '/user/developer-dashboard/'
            else:
                return '/user/manager-dashboard/'



class ManagerDashboardView(ListView):
    
    def get(self, request, *args, **kwargs):
        #logic to get all the projects
        print("ManagerDashboardView")
        # projects = Project.objects.all() #select * from project
        # print(".............................................",projects)
        
        return render(request, 'user/manager-dashboard.html')
    
    
    template_name = 'user/manager-dashboard.html'