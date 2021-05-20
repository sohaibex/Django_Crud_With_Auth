from django.shortcuts import render, redirect
from django.db import connection
from .forms import CdrForms
from .models import Cdr, Client
from pprint import pprint


def cdr(request):
    client = Client.objects.all()
    if request.method == "POST":
        form = CdrForms(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = CdrForms()
    return render(request, 'index.html', {'form': form,"client": client})




def show(request):
    if request.method == "POST":
        search=request.POST.get('search')
        searchresult=connection.cursor()
        searchresult.execute('select cl.id,cl.nomClient,cl.telClient,cdr.date,cdr.duree,cdr.id from cdr_client cl join cdr_cdr cdr on cl.id=cdr.idClient_id where cdr.date="2021-05-20"')
        results = searchresult.fetchall()
        return render(request, "show.html", {'cdr': searchresult})

    else:
         cdr=connection.cursor()
         cdr.execute("select cl.id,cl.nomClient,cl.telClient,cdr.date,cdr.duree,cdr.id from cdr_client cl join cdr_cdr cdr on cl.id=cdr.idClient_id ORDER BY cdr.date desc ")
         results=cdr.fetchall()
         return render(request, "show.html", {'cdr': cdr})



def edit(request, id):
    client = Client.objects.all()
    cdr = Cdr.objects.get(id=id)
    return render(request, 'edit.html', {'cdr': cdr,'client':client})


def update(request, id):
    cdr = Cdr.objects.get(id=id)
    form = CdrForms(request.POST, instance=cdr)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'cdr': cdr})


def destroy(request, id):
    cdr = Cdr.objects.get(id=id)
    cdr.delete()
    return redirect("/show")
