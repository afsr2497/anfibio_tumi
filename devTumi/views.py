from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return render(request,'devTumi/index.html')

def gamepadButton(request):
    comando = request.GET.get('comando')
    if int(comando[7])<4:
        print(comando)
        #ENviar a la nucleo
        return JsonResponse({
            'mensaje':'recibido',
            'robot':'chatibot'
        })
    else:
        return JsonResponse({
            'mensaje':'Error'
        })

def gamepadFront(request):
    return render(request,'devTumi/gamepadFront.html')

def mainView(request):
    return render(request,'devTumi/mainView.html')