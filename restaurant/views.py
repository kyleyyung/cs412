from django.shortcuts import render, redirect, HttpResponse
import random
import time

# Create your views here.

#   main page func
def main(request):

    template_name = "restaurant/main.html"

    context = {
        'current_time': time.ctime(),
        'main_image': "https://mlbostoncommon.com/get/files/image/galleries/Raffles-Nov14_ConorDoherty_0378.jpg",
    }

    return render (request, template_name, context)

# order page func
def order(request):

    template_name = "restaurant/order.html"

    context = {
        'current_time': time.ctime(),
        'special': random.choice(["Beef Wellington", "Fish Tacos", "Lobster Rolls",]), # randomly chooses a special daily dish from array
    }

    return render (request, template_name, context)

def confirmation(request):

    template_name = "restaurant/confirmation.html"

     # check if the request is a POST (vs GET)
    if request.POST:

    # read the form data in python variables:
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        special = request.POST.get('special')
        main_course1 = request.POST.get('main_course1')
        main_course2 = request.POST.get('main_course2')
        main_course3 = request.POST.get('main_course3')
        addon1 = request.POST.get('addon1')
        addon2 = request.POST.get('addon2')
        addon3 = request.POST.get('addon3')
        main_course4 = request.POST.get('main_course4')
        comments = request.POST['comments']

        items = []
        cost = 0
        if special: # if special is chosen
            cost += 30
            items.append(special)
        if main_course1:  # if risotto is chosen
            cost += 22
            items.append(main_course1) 
        if main_course2: # if Filet Mignon is chosen
            cost += 20
            items.append(main_course2)  
        if main_course3: # if burger is chosen
            cost += 12
            items.append(main_course3)
        if addon1: # if the extra patty addon is chosen
            cost += 7
            items.append(addon1)
        if addon2: # if the extra cheese addon is chosen
            cost += 3
            items.append(addon2)
        if addon3:
            cost += 5 # if the extra tomatoes addon is chosen
            items.append(addon3)
        if main_course4: # if hot dog is chosen
            cost += 7
            items.append(main_course4)

    #create a dictionary of context variables
    context = {
        'current_time': time.ctime(),
        'name': name,
        'phone': phone,
        'email': email,
        'items': items,
        'comments': comments,
        'cost': cost,
        'readytime': time.ctime(time.time() + random.randint(1800, 3600))
    }

    return render (request, template_name, context)