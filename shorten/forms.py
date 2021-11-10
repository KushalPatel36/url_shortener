from django import forms


class SubmitUrl(forms.Form):
    url = forms.CharField(label="Submit URL",
                          widget= forms.TextInput(attrs={"placeholder":"Long URL",
                                                         "class":"form-control"}))