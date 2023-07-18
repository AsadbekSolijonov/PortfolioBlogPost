from django import forms


class CommentForm(forms.Form):
    author = forms.CharField(max_length=60,
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control mb-3',
                                 'placeholder': 'Your Name',
                             }))
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control mb-3 ',
            'placeholder': 'Leave Comment!',
        }
    ))
