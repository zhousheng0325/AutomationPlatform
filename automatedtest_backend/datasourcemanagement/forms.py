from django.forms import forms, ModelForm


class FileForm(forms.Form):
    file_name = forms.FileField(label=u"文件名称")
