from . import tasks
from django.http import HttpResponse

# Create your views here.
def home(request):
    tasks.load_image.delay()
    return HttpResponse('<h1>Load Cat</h1>')
