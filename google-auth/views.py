from django.shortcuts import render_to_response
from django.template.context import RequestContext
from social.exceptions import AuthForbidden

def home(request):
   context = RequestContext(request,
                           {'user': request.user,
                             'request': request})
   return render_to_response('google-auth/home.html',
                             context_instance=context)


def email_allowed(backend, details, response, *args, **kwargs):
    print 'auth allowed called'
    print response
    #import pdb; pdb.set_trace()
    email = response['emails'][0]['value']
    at_position = email.find('@')
    if not email[at_position+1:] == 'iith.ac.in':
	    raise AuthForbidden(backend)
