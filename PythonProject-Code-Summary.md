For the two week Python Project sprint at the Tech Academy, I worked on a slice of a mature project, which aggregated small data-driven apps built with the django framework into a single hub page. My application was designed as a board game tracker, which would allow users to implement basic CRUD functionality, and display live results scraped from Board Game Quest and GamerPower. Board Game Quest data was scraped using BeautifulSoup, and GamerPower data was scraped using their free API.  Basic front end design was implemented to rapidly prototype the application, and then polished toward the end of the sprint. This project allowed me to work on both front-end and back-end skills in coordination with peers and instructors. I am proud of the work I completed during this sprint, especially considering my part-time schedule. As a student working 20 hours a week on software development, my productivity and completion rate was comparable to the requirements for full time students.

Included below are the stories I completed, including selected code snippets.
Full files for my slice of the project are available under [Python-Live-Project](#Python-Live-Project)


Story #1: Build the basic app
Create a new app for the project, named appropriately for what will be tracked, and get it to display a home page with basic content.

Create new app using manage.py startapp
Register app from within [MainProject]>[MainProject]>settings.py
Create base and home templates in a new templates folder
Add function to views to render the home page
Register urls with MainApp and create urls.py for your app and homepage
Link app's home page to the project's home page (templates/index.html) by adding an image link on the Appbuilder9000 home page.
Add minimal content and some basic styling to your base and home:
Navbar
Background
Title
Footer




Story #2: Create your model
Create a model for the collection item to be tracked, and add the ability to create a new item.

Create a model and add a migration, planning out all the categories to be tracked. Include an objects manager for accessing the database.
Create a model form that will include any inputs the user needs to make.
Add a template to the app folder for creating a new item.
Add a views function that renders the create page and utilizes the model form to save the collection item to the database.
Check the database to make sure items save without errors.
Add whatever styling is appropriate to each template.


Optional Add-Ons completed:


Minimum 4 field types
Minimum 1 widget

### model snippet ###
from django.db import models

# Choices for whether game has been played
PLAYED_CHOICES = {
    ('Yes', 'Yes'),
    ('No', 'No'),
}


# Model for adding board games to tracker
class BoardGames(models.Model):
    Game_Name = models.CharField(max_length=255, default="", null=False)
    Minimum_Players = models.IntegerField(default="", blank=True, null=False)
    Maximum_Players = models.IntegerField(default="", blank=True, null=False)
    Game_Type = models.CharField(max_length=255, default="", null=False)
    Estimated_Play_Time = models.CharField(max_length=255, default="", null=False)
    Have_We_Played = models.CharField(max_length=20, default="", choices=PLAYED_CHOICES)

    objects = models.Manager()

    # Display objects as the Game Name in string format
    def __str__(self):
        return self.Game_Name

### ###


Story #3: Display all items from database
Display information from the database in a page.

Create a new HTML page, link it from the home page
Add in a function that gets all the items from the database and sends them to the template
Display a list of items from the database, with some of the fields for that item displayed with labels/headers.
Add whatever styling is appropriate to the templates.
The functioning page lists the items in the database. 



Story #4: Details page
Create a details page that will show the details of any single item from within the database, as selected by the user. Link this to the index page for each item.

Add a details template to the template folder, register the url pattern
Create a views function that will find a single item from the database and send it to the template
Add in a link for each item on the display all items page that will direct to the details page for that item
Display all the details of the item on the details page.
Add whatever styling is appropriate to the templates.




Story #5: Edit and Delete Functions
Allow for edits and delete functions to be done from the details page or from separate pages. Have confirmation before deleting.

Add an edit page to the templates
Use model forms and instances to display the content of a single item from the database.
Have the views function send the information for the single item and save any changes.
Include the option to delete an item with a confirmation that the user wants to delete.


Optional Add-On completed:
-Use a modal and javascript for the delete confirmation message



API Pt 1: Connect to API
Connect to chosen API and get the JSON response, add in a template for displaying the information.

Create a new API template and render with a function
Go through the API documentation
Connect to the API and write a basic JSON response to the terminal
Add comments of which elements from the JSON response are needed for display
Link the API request page to the app's home page.



API Pt 2: Parse through JSON
Parse through the JSON file returned and display the information you want to display. Make additional queries to the API as necessary. Add a link from the app's home page.

Get elements out of the API JSON response, send just the needed values as relevant dictionary objects to the template

Display all objects in the API template page.

Add appropriate styling.




BeautifulSoup Pt 1: Setup Beautiful Soup
Create a new template for displaying information sourced from another website. Use Beautiful Soup to data scrape the site and find the relevant information.

Create a new template for displaying the content
Use Beautiful Soup to get the html data from selected site as a navigable object
Get the section of data to be scraped
Add comments to note which portions of the data will be extracted
Link the data scraping page to the app's home page.
Print a basic object to the terminal that contains the elements to be extracted



BeautifulSoup Pt 2: Parse through html
Parse through the html returned and display the targeted information. Remove unwanted formatting. 

Get elements out of the Beautiful Soup object, send just the targeted values as relevant dictionary objects to the template.
Display all objects within the data scrape template.

### views.py ### The view functionality for completed stories:

from django.shortcuts import render, get_object_or_404, redirect
from .forms import BoardGameForm
from .models import BoardGames
import requests
from bs4 import BeautifulSoup
import re
import json
from django.http import HttpResponse


# Story 1: build basic app -------------------------------------------------


def bgt_home(request):
    return render(request, "BoardGameTracker/BoardGameTracker_add.html")

# ---------------------------------------------------------------------------


# Story 2: Create Model------------------------------------------------------

def bgt_create(request):
    form = BoardGameForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('bgt_home')
    else:
        print(form.errors)
        form = BoardGameForm()
    context = {
        'form': form,
    }
    return render(request, 'BoardGameTracker/BoardGameTracker_add.html', context)

# --------------------------------------------------------------------------------


# Story 3: Create page to display all boardgames entered into database------------

def bgt_view(request):
    boardgames = BoardGames.objects.all()
    return render(request, 'BoardGameTracker/BoardGameTracker_read.html', {'boardgames': boardgames})

# Story 4: Create page to display details of single selected object--------------------------


def bgt_details(request, pk):
    pk = int(pk)
    boardgame = get_object_or_404(BoardGames, pk=pk)
    context = {'boardgame': boardgame}
    return render(request, 'BoardGameTracker/BoardGameTracker_details.html', context)
# --------------------------------------------------------------------------------------------


# Story 5: Create Edit and Delete functionality for objects in Board Game DB------------------

def bgt_edit(request, pk):
    pk = int(pk)
    boardgame = get_object_or_404(BoardGames, pk=pk)
    form = BoardGameForm(data=request.POST or None, instance=boardgame)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('bgt_view')
    context = {
        'form': form,
        'boardgame': boardgame,
    }
    return render(request, 'BoardGameTracker/BoardGameTracker_edit.html', context)

# Delete object from DB-----------------------------------------------------------


def bgt_delete(request, pk):
    pk = int(pk)
    boardgame = get_object_or_404(BoardGames, pk=pk)
    boardgame.delete()
    return redirect('bgt_view')


# Story 6: Set up BeautifulSoup to scrape html and print navigable objects to console
def bgt_bsoup():
    page = requests.get("https://www.boardgamequest.com/category/game-reviews/")
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify()) #was run to examine the page contents
    # from soup.prettify() I can see that the elements I want contain titles and links to reviews specifically
    # these links and their titles are in <a> tags with no class, no id, and rel='bookmark'

    review_anchor = soup.find_all(href=re.compile('-review'), class_='td-image-wrap', id=False, rel='bookmark') # This line isolates the links to the actual review links I want to scrape
    imageSoup = BeautifulSoup(str(review_anchor), 'html.parser')
    #print(imageSoup.prettify())
    review_image = imageSoup.find_all('img')
    # print("REVIEW IMAGE 0") # this message prints to allow for the print command below to be easily spotted
    # print(review_image[0]) # this message prints to allow for examination of scraped image URL

    reviewList = []
    imageList = []
    n = 0
    while n < 7:

        href = review_anchor[n].get('href')
        title = review_anchor[n].get('title')
        rtext = review_anchor[n].get_text()
        rimage = review_image[n].get('src')
        imageList.append(rimage)
        reviewList.append({'href': href, 'title': title, 'rtext': rtext, 'rimage': rimage})
        n += 1
    #print(list(review_anchor)) # This prints each anchor element containing the review title and link to the console
    # print("IMAGE LIST 0")
    # print(imageList[0])

    content = {"reviewList": reviewList} # right now the list of <a> elements renders on the BeautifulSoup page of my app with no formatting



    return content #render(request, 'BoardGameTracker/BoardGameTracker_bsoup.html', content)

def bgt_bsoup_render(request):
    reviewList = bgt_bsoup()["reviewList"]
    content = {
        'reviewList': reviewList
    }
    return render(request, 'BoardGameTracker/BoardGameTracker_bsoup.html', content)



def jprint(obj): # This function was used to examine JSON results, but is not required for rendering / display
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)




def bgt_api(request):
    response = requests.get("https://www.gamerpower.com/api/giveaways?sort-by=date") # This API allows easy sorting of deals and giveaways by date
    print(response.status_code)

    # from the returned JSON I intend to render
    #   thumbnail images ("image"), link to the giveaway listing ("gamerpower_url"), and title ("title")
    #   Clicking on the thumbnail or title should redirect viewer to gamerpower URL.
    #   New entries should load and refresh based on what listings are most recent at gamerpower
    api_load = json.loads(response.text)
    #print(api_load)

    gamerpower_url = []
    title = []
    image_url = []

    for item in api_load:
        json_title = item["title"]
        title.append(json_title)

        json_gameurl = item["gamerpower_url"]
        gamerpower_url.append(json_gameurl)

        json_image = item["image"]
        image_url.append(json_image)

    api_list = zip(title, gamerpower_url, image_url)
    content = {"api_list": api_list}


    return render(request, "BoardGameTracker/BoardGameTracker_api.html", content)

    ### ###

Story #8: Front End Improvements
Go through your various templates and add improvements to the UI/UX. 

