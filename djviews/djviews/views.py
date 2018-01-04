from django.http import HttpResponse

def home(request):
	# print(dir(request))
	print(request.get_full_path())
	print(request.method)
	return HttpResponse("<!DOCTYPE html><html><head><title>Blog</title><style>h1{color:green}</style></head><body><h1>Hello World</h1></body></html>")