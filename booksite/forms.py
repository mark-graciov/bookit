from django import forms


class TaleForm(forms.Form):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', [])
        super(TaleForm, self).__init__(*args, **kwargs)

        for key, label, help_text in fields:
            self.fields[key] = forms.CharField(label=label, help_text=help_text)

    def collect(self):
        values = []
        for key in self.fields:
            value = self.cleaned_data[key]
            values.append((key, value))

        return values
