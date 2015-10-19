from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Inventory, Computer

from .forms import AddInventoryForm


# Create your views here.
def index(request):
    """Show the user their inventories and give them buttons to make more"""
    inventories = Inventory.objects.all()
    return render(request, 'inventory/index.html', {'inventories':inventories})

def view_inventory(request, inventory_id):
    """Show the user the contents of an inventory."""
    inventory = Inventory.objects.get(id=inventory_id)
    computers = Computer.objects.filter(inventory_id=inventory_id)
    print("got comptuers", computers)

    return render(request, 'inventory/inventory_view.html',
        {
            'inventory_name' : inventory.name,
            'computers' : computers
        })

def create_inventory(request):
    """Show the user a form to add an inventory"""
    if request.method == "POST":
        inventory_form = AddInventoryForm(request.POST)
        if inventory_form.is_valid():
            # TODO: fail if name is already in database

            # create new inventory object
            new_inventory = Inventory(name=inventory_form.cleaned_data['name'])
            print("Created a new inventory object", new_inventory)
            new_inventory.save()
            print("new inventory id is ", new_inventory.id)
            return redirect(view_inventory, inventory_id=new_inventory.id)
                
    else: # form does not exist yet, create and return it
        inventory_form = AddInventoryForm()

    return render(request, 'inventory/inventory_form.html', {'inventory_form':inventory_form})

def edit_inventory(request, inventory_id):
    """Show the user a form to edit or create an inventory object"""
    pass

def delete_inventory(request, inventory_id):
    """Delete the inventory and computers belonging to it given by the id if it exists"""
    pass

def create_computer(request):
    """Show the user a form to add a computer to an inventory"""
    pass

def edit_computer(request, computer_id):
    """Show the user a form to edit or create an computer object"""
    pass

def delete_computer(request, computer_id):
    """Delete the computer given by the id if it exists"""
    pass