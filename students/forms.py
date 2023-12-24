from django import forms

class StudentForm(forms.Form):
    NatCode=forms.CharField(
        widget=forms.TextInput()
    )
    # BirthDate=forms.DateField(
    #     forms.DateInput()
    # )
    Telephon=forms.CharField(
        widget=forms.TextInput()
    )
    Mobile=forms.CharField(
        widget=forms.TextInput()
    )
    Address=forms.CharField(
        widget=forms.Textarea()
    )


class TeacherForm(forms.Form):
    NatCode=forms.CharField(
        widget=forms.TextInput()
    )
    # BirthDate=forms.DateField(
    #     forms.DateInput()
    # )
    Telephon=forms.CharField(
        widget=forms.TextInput()
    )
    Mobile=forms.CharField(
        widget=forms.TextInput()
    )
    Address=forms.CharField(
        widget=forms.Textarea()
    )