from django.views import View
from django.shortcuts import render

class HomeView(View):
    template_name = 'index.html'
    
    def get(self, request):
        return render(request, self.template_name,)
class AboutUsView(View):
    template_name = 'aboutus.html'
    
    def get(self, request):
        return render(request, self.template_name,)
class ContactView(View):
    template_name = 'contact.html'
    
    def get(self, request):
        return render(request, self.template_name,)
class ProductsView(View):
    template_name = 'products.html'
    
    def get(self, request):
        return render(request, self.template_name,)
