from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms

from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')

    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)  #o sinal de menos ordena pelo mais antigo

    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html',{"fotografia":fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    #puxa os itens no banco de dados
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    #filtra os itens de acordo com as palavras
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar'] #pegando o tempo que ta dentro de buscar que faz referencia no input
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/index.html", {"cards":fotografias})

def nova_imagem(request):
    #se usuario nao logado
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')

    form = FotografiaForms
    #caso o usuario preencha o formulario as informações terão que ser salvas no banco de dados
    if request.method == 'POST':
        #passou as infromações para dentro
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            #salvando
            form.save()
            messages.success(request, 'Nova fotografia cadastrada!')
            return redirect('index')
    return render(request, 'galeria/nova_imagem.html',{'form':form})

def editar_imagem(request, foto_id):
   fotografia = Fotografia.objects.get(id=foto_id) #coloquei todas as informações daquela fotografia na variavel que esta no banco de dados
   form = FotografiaForms(instance=fotografia)

   if request.method == 'POST':
       form = FotografiaForms(request.POST, request.FILES, instance=fotografia)#cria um novo formulario em que recebe as informações
       if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia editada com sucesso!')
            return redirect('index')
            

   return render(request, 'galeria/editar_imagem.html',{'form':form,'foto_id':foto_id})
    

def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()#removeu
    messages.success(request, 'Deleção feita com sucesso!')
    return redirect('index')

def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True,categoria=categoria)

    return render(request, 'galeria/index.html',{"cards": fotografias})
