from django import forms


class ResourceForm(forms.Form):
    method = forms.ChoiceField(
        choices=(
            ('GET', 'GET'),
            ('POST', 'POST')
        ),
        widget=forms.RadioSelect(
            attrs={
                'class': 'custom-control-input',
            } 
        ),
        label='Тип запроса'
    )
    resource_type = forms.ChoiceField(
        choices=(
            ('poet', 'Poet'),
            ('poem', 'Poem')
        ),
        widget=forms.RadioSelect(
            attrs={
                'class': 'custom-control-input',
            } 
        ),
        label='Поэт или стихотворения'
    )
    data = forms.JSONField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 8,
                'placeholder': '{"input": "your json data"}'
            }
        ),
        required=False,
    )
