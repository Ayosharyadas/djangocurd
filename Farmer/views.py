from django.shortcuts import render

# Create your views here.

# Create your views here.
from django.shortcuts import render, redirect
from Farmer.forms import FarmersForm
from Farmer.models import Farmermodel
# Create your views here.
def farm(request):
    if request.method == "POST":
        form = FarmersForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = FarmersForm()
    return render(request,'index.html',{'form':form})
def show(request):
    farms = Farmermodel.objects.all()
    return render(request,"show.html",{'farms':farms})
def edit(request, id):
    Farmer1 = Farmermodel.objects.get(id=id)
    return render(request,'edit.html', {'Farmer1':Farmer1})
def update(request, id):
    Farmer1= Farmermodel.objects.get(id=id)
    form = FarmersForm(request.POST, instance = Farmer1)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'Farmer1': Farmer1})
def destroy(request, id):
    Farmer1 = Farmermodel.objects.get(id=id)
    Farmer1.delete()
    return redirect("/show")
