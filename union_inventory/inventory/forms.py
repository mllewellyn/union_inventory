"""
Contains forms build in cripsy forms for the inventory application/
"""

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import FormActions


class AddInventoryForm(forms.Form):
    """Form for adding or editing a inventory"""
    def __init__(self, *args, **kwargs):
        super(AddInventoryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            FormActions(Submit('save', 'Add inventory'))
        )
    name = forms.CharField(label="Name", required=True, help_text='Eg: My First Inventory')