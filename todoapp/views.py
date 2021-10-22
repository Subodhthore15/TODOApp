from django.shortcuts import redirect, render
from todoapp.models import Mytodo
# Create your views here.
from todoapp.forms import TodoForm

def alltodos(request):
    tasks=Mytodo.objects.all()
    form = TodoForm()
    if request.method=="POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request,'alltodo.html',{"tasks":tasks,"form":form})


def deleteItem(request,pk):
    
    task = Mytodo.objects.get(id= pk)
    task.delete()
    return redirect('alltodos')

def updateItem(request,pk):
    
    todo = Mytodo.objects.get(id= pk)
    
    updateForm = TodoForm(instance=todo)
    

    if request.method=="POST":

        updateForm = TodoForm(request.POST,instance=todo)

        if updateForm.is_valid():
            updateForm.save()
            return redirect('alltodos')

    return render(request,'updatetodo.html',{'todo':todo,"updateForm":updateForm})
