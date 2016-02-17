from django.shortcuts import render
from .models import filemodel
from .forms import fileform
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from azure.storage.blob import BlobService

def index(request):
    context = RequestContext(request)
    if request.method == 'POST':
        formobj = fileform(request.POST,request.FILES)
        if formobj.is_valid():
            modelobj = formobj.save(commit=False)
            modelobj.image=request.FILES['image']
            modelobj.save()
            
            blob_service = BlobService(account_name='myaccount', account_key='mykey')
            try:
                blob_service.create_container('mycontainer', x_ms_blob_public_access='container')
            except:
                blob_service.set_container_acl('mycontainer', x_ms_blob_public_access='container')
            return HttpResponseRedirect(reverse('list'))
    else:
        formobj = fileform()
        return render_to_response('app/myform.html', {'formobj': formobj},context)


def listdisp(request):
    context = RequestContext(request)
    modelobjs = filemodel.objects.all()
    return render_to_response('app/list.html', {'modelobjs': modelobjs},context)
