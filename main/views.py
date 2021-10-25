from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from .models import Doc

class MainView(TemplateView):
    template_name = 'main/main.html'
def file_upload_view(request):
   # print(request.FILES)      <MultiValueDict: {'file': [<InMemoryUploadedFile: test1.png (image/png)>]}>
    if request.method == 'POST':
        my_file = request.FILES.get('file')
        Doc.objects.create(upload=my_file)
        return HttpResponse('')
    return JsonResponse({'post': 'false'})
