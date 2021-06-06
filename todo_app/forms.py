from django import forms

class TodoForm(forms.Form):
    title = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'ala-bala',
            }
        )
    )

    description = forms.CharField()

    bot_catcher = forms.CharField(
        widget=forms.HiddenInput,
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            if 'class' in field.widget.attrs:
                value = field.widget.attrs['class'] + ' form-control'
            else:
                value = 'form-control'
            field.widget.attrs['class'] = value


# --------------------------------------------------------------

# class ToDoFormFull(forms.Form):
#     task = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
#         'class': 'form-control'
#     }))
#     text = forms.CharField(widget=forms.Textarea(attrs={
#                                                         'class': 'form-control',
#
#                                                         }), required=True,
#                                                             label='Description',
#                                                                )
#     # password = forms.CharField(widget=forms.PasswordInput(attrs={
#     # 'class':'form-control'
#     # }))
#     age = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
#         'class': 'form-control',
#     }))
#     slider = forms.IntegerField(widget=forms.TextInput(
#         attrs={
#                'type': 'range',
#                'class': 'form-control',
#
#                }
#     ))
