from django.views import View
from django.shortcuts import render

class StoreView(View):
    template_name = 'store.html'
    
    def get(self, request):
        return render(request, self.template_name,)
class CartView(View):
    template_name = 'cart.html'
    
    def get(self, request):
        return render(request, self.template_name,)
