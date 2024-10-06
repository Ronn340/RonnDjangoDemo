from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200) #label is optional, max_length is required
    check = forms.BooleanField(required=False)


#YOU CAN CREATE MORE FORM CLASSES--     