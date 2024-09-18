from django.http import HttpResponse

# Create your views here.
def vistaPaginaInicio(request):
	return HttpResponse('Hola Raymundo, Edmundo y Segismundo')
