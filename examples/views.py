from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import generic

from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalUpdateView,
    BSModalDeleteView
)

from .forms import VehicleModelForm
from .models import Book,Vehicle_Details


class Index(generic.ListView):
    model = Vehicle_Details
    context_object_name = 'vehicle'
    template_name = 'index.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if 'type' in self.request.GET:
            qs = qs.filter(book_type=int(self.request.GET['type']))
        return qs


class AddDetailsView(BSModalCreateView):
    template_name = 'examples/add_details.html'
    form_class = VehicleModelForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('index')


class UpdateDetailsView(BSModalUpdateView):
    model = Vehicle_Details
    template_name = 'examples/update_details.html'
    form_class = VehicleModelForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('index')



class DeleteDetailsView(BSModalDeleteView):
    model = Vehicle_Details 
    template_name = 'examples/delete_details.html'
    success_message = 'Success: Book was deleted.'
    success_url = reverse_lazy('index')



# def vehicle(request):
#     if request.method=='GET':
#         vehicle = Vehicle_Details.objects.all()
#         return render(request,'_vehicle_table.html',{'vehicle':vehicle})

def vehicle(request):
    data = dict()
    if request.method == 'GET':
        vehicle = Vehicle_Details.objects.all()
        data['table'] = render_to_string(
            '_vehicle_table.html',
            {'vehicle': vehicle},
            request=request
        )
        return JsonResponse(data)
