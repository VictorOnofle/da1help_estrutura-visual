from django.shortcuts import render

def pagina_inicial(request):
    return render(request, 'website/homepage.html')

def contato(request):
    return render(request, 'website/contatopage.html')

def login(request):
    return render(request, 'website/loginpage.html')

def registro(request):
    return render(request, 'website/registerpage.html')

def esqueci_senha(request):
    return render(request, 'website/esquecipassword.html')

def busca(request):
    return render(request, 'website/searchpage.html')

def sobre(request):
    return render(request, 'website/sobrepage.html')