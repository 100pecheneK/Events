def change_widget_attrs_class_to_invalid(self, field, placeholder):
    self.fields[field].widget.attrs.update({
        'placeholder': placeholder,
        'class': 'form-control is-invalid',
        'autocomplete': 'off'
    })


def change_widget_attrs_class_to_valid(self, field, placeholder):
    self.fields[field].widget.attrs.update({
        'placeholder': placeholder,
        'class': 'form-control is-valid',
        'autocomplete': 'off'
    })