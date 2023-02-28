from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied


def auth_seller(func):
    def wrapper(request, *args, **kwargs):
        if 'seller' in request.session: 

            return func(request, *args, **kwargs)
        else:
            return redirect('common:seller')
    return wrapper
