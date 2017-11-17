from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Pin, Location
from .forms import PinForm, LocationForm
# Views for PinScene

def index(request):
    """Homepage for pinscene app"""
    return render(request, 'pinscene/index.html')

def pins(request):
    """Show all pins"""
    pins = Pin.objects.order_by('-date_added') #get list of all pins in db
    context = {'pins': pins}
    return render(request, 'pinscene/pins.html', context) #render list of pins

def pin(request, pin_id):
    """shows single pinball machine and its information"""
    pin = Pin.objects.get(id=pin_id) #get particular pin by id.
    context = {'pin': pin}
    return render(request, 'pinscene/pin.html', context)

@login_required
def new_pin(request):
    """Add a new pinball machine to database"""
    if request.method != 'POST':
        #No data submitted -- create blank form
        form = PinForm()
    else:
        #POST data submitted -- process data.
        form = PinForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pinscene:pins'))

    context = {'form': form}
    return render(request, 'pinscene/new_pin.html', context)

@login_required #prevent non-registered users from editing pins
def edit_pin(request, pin_id):
    """edit an existing pin"""
    pin = Pin.objects.get(id=pin_id)

    if request.method != 'POST':
        form = PinForm(instance=pin)
    else:
        form = PinForm(instance=pin, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pinscene:pin', args=[pin.id]))
    
    context = {'pin':pin, 'form':form}
    return render(request, 'pinscene/edit_pin.html', context)
@login_required
def delete_pin(request, pk):
    pin = get_object_or_404(Pin, pk=pk)  # Get your current cat

    if request.method == 'POST':         # If method is POST,
        pin.delete()                     # delete the cat.
        return redirect('pinscene:pins')             # Finally, redirect to the homepage.

    return render(request, 'pinscene:pins', {'pin': pin})
