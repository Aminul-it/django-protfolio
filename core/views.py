from django.shortcuts import render
from django.views.generic import CreateView
from core.models import Contact
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def home(request):
    return render(request,'core/home.html', context={})

class contact(CreateView):
      model = Contact
      template_name = 'core/contact.html'
      fields = ('your_name','your_email','your_subject','your_message',)
      def form_valid(self,form):

          form.save(commit=True)


          return HttpResponseRedirect(reverse('success'))
def success(request):
    return render(request,'core/success.html',context={})
