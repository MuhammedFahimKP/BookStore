
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions,status

class BookAlreadyExists(exceptions.APIException):
    
    status_code    = status.HTTP_409_CONFLICT
    default_detail = _('Book Already Exist.')
    default_code   = 'Book Already exist'
    
    
    