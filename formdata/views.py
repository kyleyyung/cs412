from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def show_form(request):
    '''show the HTML form to the client.'''

    # use this template to produce the response
    template_name = 'formdata/form.html'
    return render(request, template_name)

def submit(request):
    ''' 
    Handle submission.
    Read out the data. 
    Generate a response
    '''

    template_name = 'formdata/confirmation.html'

    # check if the request is a POST (vs GET)
    if request.POST:

    # read the form data in python variables:
        name = request.POST['name']
        favorite_color = request.POST['favorite_color']

# package the data up to be used in the response
        context = {
            'name': name,
            'favorite_color': favorite_color,
        }

    # generate a response
    return render(request, template_name, context)

# return HttpResponse("Nope.")

## GET lands down here: no return statements!
    # template_name = 'fomdata/form.html'
    # return render(request, template_name)

# best solution
    return redirect("show_form")