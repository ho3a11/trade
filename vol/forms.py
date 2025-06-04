from django import forms

class UploadFileForm(forms.Form):
    file1 = forms.FileField(label="فایل اول (.xlsx)")
    file2 = forms.FileField(label="فایل دوم (.xlsx)")

    def clean(self):
        cleaned_data = super().clean()
        for field in ['file1', 'file2']:
            file = cleaned_data.get(field)
            if file:
                if not file.name.lower().endswith('.xlsx'):
                    self.add_error(field, "فقط فایل اکسل با پسوند .xlsx مجاز است.")
        return cleaned_data

    