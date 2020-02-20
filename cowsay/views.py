from django.shortcuts import render, reverse, HttpResponseRedirect
import subprocess

from cowsay.forms import TextInput
from cowsay.models import Cowsay

"""
Had help from JT on this part
"""

def cowsay_helper(text):
    cmd = subprocess.Popen(
        ['cowsay', text],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    out, err = cmd.communicate()

    if err:
        raise err
    else:
        return out.decode().split("\n")

def index(request):
    html = 'index.html'

    if request.method == 'POST':
        form = TextInput(request.POST)
        if form.is_valid():
            data = form.cleaned_data['text']
            form.save()

            return render(request, html, {'form': TextInput(), 'text': cowsay_helper(data)})
            
    return render(request, html, {'form': TextInput()})
