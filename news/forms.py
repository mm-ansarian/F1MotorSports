from django import forms


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150)
    content = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title']
        temp_ls = title.split(' ')
        title = []
        for i in temp_ls:
            title.append(i.capitalize())
        title = ' '.join(title)
        return title
