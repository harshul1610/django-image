from django.shortcuts import render,HttpResponse
from .models import filemodel
from .forms import fileform
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from azure.storage.blob import BlockBlobService
from azure.storage.blob import PublicAccess
from azure.storage.blob import ContentSettings

myaccount='tofim'
mykey='5jb1QMcmwb0BYFPeJwfXpw6afn27MXw6MH37BWHSxRYUfWwwaVQK7DzGEN1ygCkxFti20sDGjWUg2pFH3HVHCQ=='

def index(request):
    context = RequestContext(request)
    if request.method == 'POST':
        formobj = fileform(request.POST,request.FILES)
        if formobj.is_valid():
            modelobj = formobj.save(commit=False)
            modelobj.image=request.FILES['image']
            modelobj.save()

            mp3= request.FILES['image']

            block_blob_service = BlockBlobService(account_name=myaccount, account_key=mykey)
            block_blob_service.create_container('harshultest2', public_access=PublicAccess.Container)
            block_blob_service.set_container_acl('harshultest2', public_access=PublicAccess.Container)

            with open('t.png','wb+') as formfile:
                for chunk in mp3.chunks():
                    formfile.write(chunk)

            block_blob_service.create_blob_from_path(
                'harshultest2',
                str(request.FILES['image']),
                't.png',

            content_settings=ContentSettings(content_type='image')
                )

            return HttpResponseRedirect(reverse('list'))
    else:
        formobj = fileform()
        return render_to_response('app/myform.html', {'formobj': formobj},context)


def listdisp(request):
    context = RequestContext(request)
    modelobjs = filemodel.objects.all()
    return render_to_response('app/list.html', {'modelobjs': modelobjs},context)
