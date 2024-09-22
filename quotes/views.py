from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import time
import random
# Create your views here.

# def home(request):
#     '''a function to respond to the /hw url'''

#     response_text = f'''
#     <html>
#     <h1>Hello, World!</h1>
#     <p>
#     This is our first django web page!
#     </p>
#     <hr>
#     This page was generated at {time.ctime()}.
#     '''

#     return HttpResponse(response_text)

# view for main page
def quote(request):
    ''' 
    A function to respond to the /hw url.
    This function will delegate work to an HTML template
    '''

    template_name="quotes/quote.html"

    #create a dictionary of context variables
    #quote is a list of string quotes and image is a list of URLs of images
    context = {
        'current_time': time.ctime(),
        'quote': random.choice(["“If you do the work, you get rewarded. There are no shortcuts in life.”", "“Heart is what separates the good from the great.”", "“I've never been afraid to fail.”", "“If you quit once, it becomes a habit. Never quit!”", "“Never say never, because limits, like fears, are often just an illusion.”","“I can accept failure, everyone fails at something. But I can't accept not trying.”","“You must expect great things of yourself before you can do them.”",]),
        'image': random.choice(["https://media.cnn.com/api/v1/images/stellar/prod/160204101907-nba-slam-dunk-5.jpg?q=w_4725,h_2658,x_0,y_0,c_fill", "https://dynaimage.cdn.cnn.com/cnn/c_fill,g_auto,w_1200,h_675,ar_16:9/https%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F210616193554-01-michael-jordan-athlete-activism.jpg", "https://image.cnbcfm.com/api/v1/image/106498863-1587478459689michaeljordan.jpg?v=1587478546&w=1858&h=1045&vtcrop=y", "https://miro.medium.com/v2/resize:fit:1358/1*MrVNTqVrTC5JFuXRGC7wHA.jpeg", "https://www.si.com/.image/ar_1.91%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cg_faces:center%2Cq_auto:good%2Cw_1200/MTk0MzY4ODA1MTEwMDMxODc3/michael-jordan-45.jpg, https://cdn.calciomercato.com/images/2017-03/michael.jordan.basketball.sport.wallpapers.hd.wallpapers.hd.celebrities.sports.photo.michael.jordan.wallpaper.1440x864.jpg"]),
    }

    return render(request, template_name, context)

#view for about page
def about(request):
    ''' 
    A function to respond to the /hw url.
    This function will delegate work to an HTML template
    '''

    template_name="quotes/about.html"

    #create a dictionary of context variables
    context = {
        'current_time': time.ctime(),
    }

    return render(request, template_name, context)

#view for show all page
def show_all(request):
    ''' 
    A function to respond to the /hw url.
    This function will delegate work to an HTML template
    '''

    template_name="quotes/show_all.html"

    #create a dictionary of context variables
    # attach each quote and iomage to a different context variable
    context = {
        'current_time': time.ctime(),
        'quote1': "“If you do the work, you get rewarded. There are no shortcuts in life.”",
        'quote2': "“Heart is what separates the good from the great.”",
        'quote3': "“I've never been afraid to fail.”",
        'quote4': "“If you quit once, it becomes a habit. Never quit!”",
        'quote5': "“Never say never, because limits, like fears, are often just an illusion.”",
        'quote6': "“I can accept failure, everyone fails at something. But I can't accept not trying.”",
        'quote7': "“You must expect great things of yourself before you can do them.”",
        'image1': "https://media.cnn.com/api/v1/images/stellar/prod/160204101907-nba-slam-dunk-5.jpg?q=w_4725,h_2658,x_0,y_0,c_fill",
        'image2': "https://dynaimage.cdn.cnn.com/cnn/c_fill,g_auto,w_1200,h_675,ar_16:9/https%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F210616193554-01-michael-jordan-athlete-activism.jpg",
        'image3':"https://image.cnbcfm.com/api/v1/image/106498863-1587478459689michaeljordan.jpg?v=1587478546&w=1858&h=1045&vtcrop=y",
        'image4': "https://miro.medium.com/v2/resize:fit:1358/1*MrVNTqVrTC5JFuXRGC7wHA.jpeg",
        'image5': "https://www.si.com/.image/ar_1.91%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cg_faces:center%2Cq_auto:good%2Cw_1200/MTk0MzY4ODA1MTEwMDMxODc3/michael-jordan-45.jpg",
        'image6': "https://cdn.calciomercato.com/images/2017-03/michael.jordan.basketball.sport.wallpapers.hd.wallpapers.hd.celebrities.sports.photo.michael.jordan.wallpaper.1440x864.jpg",
    }

    return render(request, template_name, context)