# coding=utf-8

import re
from wtforms.validators import Regexp, ValidationError

from app.utils.constants import NICKNAME_INVALID


class NickName(Regexp):
    def __init__(self, required=True):
        self.required = required
        super(NickName, self).__init__('^[\u4e00-\u9fa5\ue000-\uefff\u2702-\u27B0\U0001F170-\U0001F251'
                                       '\U0001F300-\U0001F64F\U0001F681-\U0001F6C5\w\- ]{2,30}$',
                                       message=NICKNAME_INVALID)

    def __call__(self, form, field, message=None):
        if self.required or field.data:
            super(NickName, self).__call__(form, field, NICKNAME_INVALID)
        if field.data is not None:
            field.data = re.sub('\s+', ' ', field.data.strip())

class EqualTo(object):
    """
    Compares the values of two fields.

    :param fieldname:
        The name of the other field to compare to.
    :param message:
        Error message to raise in case of a validation error. Can be
        interpolated with `%(other_label)s` and `%(other_name)s` to provide a
        more helpful error.
    """
    def __init__(self, fieldname, message=None):
        self.fieldname = fieldname
        self.message = message

    def __call__(self, form, field):
        try:
            other = form[self.fieldname]
        except KeyError:
            raise ValidationError(field.gettext("Invalid field name '%s'.") % self.fieldname)
        if field.data != other.data:
            message = self.message
            if message is None:
                message = field.gettext('Field must be equal to %(other_name)s.')

            raise ValidationError(message)