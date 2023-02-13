from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ProductForm
from .models import Product
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import auth
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
# Create your views here.
def home(request):
	return render(request, 'login.html')

def logoutView(request):
	logout(request)
	return redirect('home')


def loginView(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			return redirect('apost')
		else:
		    messages.info(request, "Invalid Username or Password")
		    return redirect('login_form')

class AdminCreatePost(LoginRequiredMixin,CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'dashboard/Product.html'
    success_url = reverse_lazy('alistalltise')


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)

class ListAllTise(LoginRequiredMixin,ListView):
    model = Product
    template_name = 'dashboard/product_list.html'
    context_object_name = 'tises'
    paginated_by = 10


    def get_queryset(self):
        return Product.objects.order_by('-id')

class ADeletePost(LoginRequiredMixin,SuccessMessageMixin, DeleteView):
    model = Product
    template_name = 'dashboard/confirm_delete.html'
    success_url = reverse_lazy('alistalltise')
    success_message = "Announcement Was Deleted Successfully"


