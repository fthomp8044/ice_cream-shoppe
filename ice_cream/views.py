from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import IceCream
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404

# Create your views here.
# instead of having the usual return HttpResponse(). we use the render() method and add 3 args: request, 'the index.html template', and context=""
# def index(request):
#     return HttpResponse('hello world!')

# def dailyFlavor(request):
#     return render(request, 'ice_cream/daily_Flavors.html')



class DailyFlavor(generic.ListView):
    template_name = 'ice_cream/daily_flavors.html'
    context_object_name = 'ice_cream_list'

    def get_queryset(self):
        return IceCream.objects.filter(available='DAILY')


# def weeklyFlavor(request):
#     return render(request, 'ice_cream/weekly_Flavors.html')

class WeeklyFlavor(generic.ListView):

    template_name = 'ice_cream/weekly_flavors.html'
    context_object_name = 'ice_cream_list'

    def get_queryset(self):
        #this returns the icecream flavor objects and instead of .all()we use .filter() to grab your available variable inside your module
        return IceCream.objects.filter(available='WEEKLY')

# def seasonalFlavor(request):
#     return render(request, 'ice_cream/seasonal_Flavors.html')

class SeasonalFlavor(generic.ListView):
    template_name = 'ice_cream/seasonal_flavors.html'
    context_object_name = 'ice_cream_list'

    def get_queryset(self):
    #this returns the icecream flavor objects and instead of .all()we use .filter() to grab your available variable inside your module
        return IceCream.objects.filter(available='SEASONAL')


# def featuredFlavor(request):
#     return render(request, 'ice_cream/featured_Flavors.html')

class FeaturedFlavor(generic.ListView):
    template_name = 'ice_cream/featured_Flavors.html'
    context_object_name = 'ice_cream_list'

    def get_queryset(self):
        return IceCream.objects.all()

class CreateView(generic.CreateView):
    model = IceCream
    template_name = 'ice_cream/ice_cream_new.html'
    fields= '__all__'

def delete_view(request, pk):
#place the icecream you want to delete
    ice_cream = get_object_or_404(IceCream, pk=pk)
#functio to delete the icecream
    ice_cream.delete()
    return HttpResponseRedirect(reverse_lazy('ice_cream:index'))


def increment_votes(request, flavor_id):
    ice_cream = get_object_or_404(IceCream, pk=pk)
    ice_cream.votes +=1
    ice_cream.save()

    return HttpResponseRedirect(reverse('ice_cream:index'))
