from wtforms.validators import ValidationError

class Unique(object):
    def __init__(self, model, field, message=u'This element already exists.'):
        self.model = model
        self.field = field
        self.message = message

    def __call__(self, form, field):
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)

class IsPasswordMatch(object):
    def __init__(self, password1, password2, message=u'These values do not match'):
        self.password1 = password1
        self.password2 = password2
        self.message = message

    def __call__(self, password1,password2):
        if self.password1 != self.password2:
            raise ValidationError(self.message)
