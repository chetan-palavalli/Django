from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/')
    items = Item.objects.all()
    returnDict = {'items': items}
    return render(request,'home.html', returnDict)
#    else:
#        new_item_text = ''
#    returnDict = {
#        'new_item_text': new_item_text,
#    }
#    return render(request,'home.html', returnDict)