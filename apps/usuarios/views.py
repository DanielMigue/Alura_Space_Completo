from django.shortcuts import render, redirect

from apps.usuarios.forms import LoginForms, CadastroForms # pega as atribuições do login e cadastro do forms

from django.contrib.auth.models import User #pega a tabela do banco de dados

from django.contrib import auth # para autenticações

from django.contrib import messages #para alertas de mensagens

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome=form['nome_login'].value()
            senha=form['senha'].value()

            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )
            if usuario is not None:
                #logou
                auth.login(request, usuario)
                messages.success(request, f"{nome} logado com sucesso!")
                return redirect('index')
            else: 
                messages.error(request, "Erro ao efetuar login")
                return redirect('login')


    return render(request, "usuarios/login.html",{"form":form})#criando o caminho para o template com dicionario com o objeto do formulario

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)#pega todas as informações do formulário e coloca dentro um formulario novo
        
        if form.is_valid():
            #método para redirecionar novamente
            
            nome = form["nome_cadastro"].value()
            email = form["email"].value()
            senha = form["senha_1"].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, "Usuário já existente")                
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, "Cadastro efetuado com sucesso!")
            return redirect('login')

    return render(request, "usuarios/cadastro.html",{"form":form})#criando o caminho para o template

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect('login')

