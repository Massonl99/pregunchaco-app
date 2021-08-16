from django.shortcuts import render


def Vista_Home(request): 

	return render(request, 'Home.html')