from django import forms

from image.models import FileUpload


class UploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ('photo',
                  )

class ImageResizeForm(forms.Form):
    image_field = forms.ImageField(label='IMAGE')


class ImageDocResizeForm(forms.Form):
    image_doc_field = forms.ImageField(label='KYC DOC')


class MultiPageDocResizeForm(forms.Form):
    multi_page_doc_field = forms.ImageField(label='MULTIPAGE TIFF DOC')


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Username',
        max_length=32
    )
    email = forms.CharField(
        required=True,
        label='User Email',
        max_length=32,
    )
    password = forms.CharField(
        required=True,
        label='Password',
        max_length=32,
        widget=forms.PasswordInput()
    )
