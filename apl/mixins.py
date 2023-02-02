from django.forms import forms


class FormControlMixin:
    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                field.widget.attrs['class'] = 'form-control datetimepicker-input'
                field.widget.attrs['onfocus'] = "(this.type='date')"
            elif isinstance(field, forms.DateTimeField):
                field.widget.attrs['class'] = 'form-control datetimepicker-input'
                field.widget.attrs['onfocus'] = "(this.type='datetime-local')"
            elif isinstance(field, forms.FileField):
                field.widget.attrs['class'] = 'custom-file-input'
            elif isinstance(field, forms.ModelMultipleChoiceField):
                field.widget.attrs['class'] = 'form-control selectpicker'
                field.widget.attrs['title'] = field.label
            else:
                field.widget.attrs['class'] = 'form-control'