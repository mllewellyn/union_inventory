"""
Contains forms build in cripsy forms for the inventory application/
"""

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import FormActions
from .models import Inventory, Computer

class AddInventoryForm(forms.ModelForm):
    helper = FormHelper()
    helper.layout = Layout(
            'name',
            FormActions(Submit('save', 'Add inventory'))
        )
    class Meta:
        model = Inventory
        fields = ['name']

class EditInventoryForm(forms.ModelForm):
    helper = FormHelper()
    helper.layout = Layout(
            'name',
            FormActions(Submit('save', 'Save inventory changes'))
        )
    class Meta:
        model = Inventory
        fields = ['name']

class AddComputerForm(forms.ModelForm):
    helper = FormHelper()
    helper.layout = Layout(
            'manufacturer', 'serial_number', 'comments',
            FormActions(Submit('save', 'Add computer'))
        )
    class Meta:
        model = Computer
        fields = ['manufacturer', 'serial_number', 'comments']

class EditComputerForm(forms.ModelForm):
    helper = FormHelper()
    helper.layout = Layout(
            'manufacturer', 'serial_number', 'comments',
            FormActions(Submit('save', 'Save computer changes'))
        )
    class Meta:
        model = Computer
        fields = ['manufacturer', 'serial_number', 'comments']