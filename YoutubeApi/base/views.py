from .models import ListOfVideos
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.views.generic import ListView    
from django.db.models import Q
class VideoList(ListView):
    model = ListOfVideos
    search_fields = ['Title', 'Description']
    filter_backends = (filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter)
    filterset_fields = ['ChannelId','ChannelName']
    template_name = 'base/index.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'ListOfVideos'  # Default: object_list
    paginate_by = 9
    queryset = ListOfVideos.objects.all().order_by('-UploadDateTime')  # Default: Model.objects.all()

class SearchResultView(ListView):
    model = ListOfVideos
    template_name = 'base/search.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        Videos = ListOfVideos.objects.filter(Q(Title__icontains=query))
        return Videos
    
    
