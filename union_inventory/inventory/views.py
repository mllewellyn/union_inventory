from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Inventory, Computer

from .forms import AddInventoryForm, EditInventoryForm, AddComputerForm, EditComputerForm


# Create your views here.
def index(request):
    """Show the user their inventories and give them buttons to make more."""
    inventories = Inventory.objects.all()
    return render(request, 'inventory/index.html', {'inventories':inventories})

def view_inventory(request, inventory_id):
    """Show the user the contents of an inventory."""
    inventory = Inventory.objects.get(pk=inventory_id)
    computers = Computer.objects.filter(inventory_id=inventory_id).all()
    print("got comptuers", computers)

    return render(request, 'inventory/inventory_view.html',
        {
            'inventory' : inventory,
            'computers' : computers
        })

def create_inventory(request):
    """Show the user a form to add an inventory."""
    if request.method == "POST":
        form = AddInventoryForm(request.POST)
        if form.is_valid():
            # TODO: fail if name is already in database

            # create new inventory object
            new_inventory = Inventory(name=form.cleaned_data['name'])
            new_inventory.save()
            return redirect(view_inventory, inventory_id=new_inventory.id)
                
    else: # form does not exist yet, create and return it
        form = AddInventoryForm()

    return render(request, 'inventory/inventory_form.html',
        {
            'form_name' : "Add Inventory",
            'form' : form
        })

def edit_inventory(request, inventory_id):
    """Show the user a form to edit or create an inventory object."""
    inventory = Inventory.objects.get(pk=inventory_id)

    if request.method == 'POST':
        form = EditInventoryForm(request.POST)
        if form.is_valid():
            inventory.name = form.cleaned_data['name']
            inventory.save()
            return redirect(view_inventory, inventory_id=inventory.id)
    else:
        form = EditInventoryForm(instance=inventory)


    return render(request, 'inventory/inventory_form.html',
        {
            'form_name' : "Edit Inventory",
            'form' : form
        })


def delete_inventory(request, inventory_id):
    """Delete the inventory and computers belonging to it given by the id if it exists."""
    pass

def create_computer(request, inventory_id):
    """Show the user a form to add a computer to an inventory."""
    if request.method == "POST":
        form = AddComputerForm(request.POST)
        if form.is_valid():
            new_computer = Computer(inventory_id=inventory_id, **form.cleaned_data)
            new_computer.save()
            return redirect(view_inventory, inventory_id=inventory_id)
                
    else: # form does not exist yet, create and return it
        form = AddComputerForm()

    return render(request, 'inventory/computer_form.html',
        {
            'inventory_id' : inventory_id,
            'form_name' : "Add Computer",
            'form' : form
        })


def edit_computer(request, computer_id):
    """Show the user a form to edit or create an computer object."""
    computer = Computer.objects.get(pk=computer_id)

    if request.method == 'POST':
        form = EditComputerForm(request.POST)
        if form.is_valid():
            # make the edits to the computer
            computer.manufacturer = form.cleaned_data['manufacturer']
            computer.serial_number = form.cleaned_data['serial_number']
            computer.comments = form.cleaned_data['comments']
            computer.save()
            return redirect(view_inventory, inventory_id=computer.inventory_id)
    else:
        form = EditComputerForm(instance=computer)


    return render(request, 'inventory/computer_form.html',
        {
            'inventory_id' : computer.inventory_id.id,
            'form_name' : "Add Computer",
            'form' : form
        })

def delete_computer(request, computer_id):
    """Delete the computer given by the id if it exists."""
    pass