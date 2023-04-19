from django import forms
d=[('Female','female'),('Male','male')]
d1=[('JAVA','java'),('PYTHON','python'),('SQL','sql'),('MERN','mern')]
class Student(forms.Form):
    Name=forms.CharField(max_length=100)
    Number=forms.IntegerField()
    Email=forms.EmailField()
    Url=forms.URLField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    Address=forms.CharField(max_length=100,widget=forms.Textarea(attrs={'cols':5,'row':5}))
    dropdownlist=forms.ChoiceField(choices=d)
    dropdownlistmultiple=forms.MultipleChoiceField(choices=d1)
    radio=forms.ChoiceField(choices=d,widget=forms.RadioSelect)
    checkbox=forms.MultipleChoiceField(choices=d1,widget=forms.CheckboxSelectMultiple)