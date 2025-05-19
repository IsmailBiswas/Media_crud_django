from django.views.generic.edit import  CreateView, DeleteView, UpdateView
from django.views.generic import ListView

from django.urls import reverse_lazy
# from .forms import imageForm
from .models import images

# Create your views here.
#
# class imageView(FormView):
#   template_name="image_curd.html"
#   form_class = imageForm
#   success_url = "/view_uploaded/"


class imageCreateView(CreateView):
  model = images
  fields = "__all__"
  success_url = reverse_lazy("image-view")

class imageUpdateView(UpdateView):
  model = images
  fields = "__all__"
  context_object_name = 'image'
  success_url = reverse_lazy("image-view")

class imageDeleteView(DeleteView):
  model = images
  fields = "__all__"
  context_object_name = 'image'
  success_url = reverse_lazy("image-view")

class imageView(ListView):
  template_name = 'image_curd/image_view.html'
  context_object_name = 'image'

  def get_queryset(self):
    return images.objects.all()
