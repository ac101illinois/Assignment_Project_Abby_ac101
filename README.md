Project description:

An application that shows a map of different coffee shops on the UIUC campus that students can study at. They will have tags that define each spot, including size, volume, price range, etc.

Features:
- Menu
- Map
- Rating/Review System
- Search/filter

ER Diagram:
The ER diagram was added to its own separate directory in the docs folder.
![](C:\Users\acirc\OneDrive\Desktop\INFO 390\Assignment Project ER Diagram.png)

Entities & Their Attributes

Student
- student_id
- first_name
- last_name
- campus_address
- major

CoffeeShop
- shop
- name
- location
- capacity

Visit
- student - if student is deleted, their visits will be as well
- shop - if a shop is deleted, its visits will be as will
- visit_date
- study_duration

Review
- visit - if a visit gets deleted, its reviews will be as well
- rating
- comment

Unique constraint - A student can only have one visit to one coffee shop per day

Ordering - The visit dates are automatically ordered in ascending order

Assignment 4:

In assignment four, I practiced making the views we learned in week 4. I made three
views in total: a HttpResponse for a student list, render for a coffeeshop list, and 
a List View for a list of all the visits.

After creating the views, I made html files for each one. I made a base.html file, and
extended it for each view file. For the student, coffeeshop, and visit files, a loop through
the list of objects and list them one by one. If no data is present, the webpage output says
there is no data yet.

After that, I made the url patterns for each view and tested opening each page. Each time
I was successful.

Future goals include loading data for each view, as well as creating a Detail View for the
List View, so I can click on each visit and get indepth information for each one.

Assignment #5:
In this assignment, I did something very similar to last week's assignment. First,
I created three class-based views. I made a base View for students, a generic ListView
for the reviews in the app, and finally a DetailView for each of the students.

After creating these views, I refactored their urls, and created their templates as
extensions of the preexisting base template. After loading sample data, I tested each of
these views out and was successful in opening each one.

Future goals I have is to make the webpages prettier with CSS and make it so each Student
in the list leads to their individual DetailView.

Assignment #6:
In this assignment, I added a search/filter function to my Visit ListView in views.py.
This makes it possible to search for the first name of a student and be able to pull up
all their visits. This filters by first name. I make the visit_list template show the 
complete list of visits, the search bar along with a clear button.

I also created aggregations to make summaries to count visits per student and visits per
each coffee shop and had these show up in the template at the bottom as well.

The only aspect of this assignment I was not able to complete was to successfully count 
how many queries show up when you search. It automatically shows "none found" no matter
what happens. I will seek help to fix this next week.

Assignment #7:
In this assignment, I played around with CSS files, created graphs for an analytics page
and summarized data as well using aggregation.

For my style.css, I added light brown and off-white colors for the background and header,
as well as added a logo for the website. I also played around with fonts and plan to
recolor my fonts.

I also added a graph to a new analytics page to showcase how many visits per each student.
For an added touch, I colored the graph the same teal that is in the logo. The summary
shows the same information at the bottom of the page. To make my chart, I used
matplotlib.

Assignment #8:
1. GET() is used to search and retrieve information, while POST() is used to update or
add information. For example, I use get when searching for coffeeshop visits, and use
post when adding a coffee shop review to the site.
2. Function based views are functions that manually handle the view method (post or get),
however the user must write more code when they want to create multiple views.
3. Class based views are extensions of generic django views, which means the user does
not have to write a lot of code, however it does not work well if a user is trying to
create a more complex view.

Assignment #9:
1. My first api endpoint is function based, and it returns a list of each coffee shop
visit along with a count of how many visits it had in total
2. My second api endpoint is class based, and it returns a list of aggregated data,
showing the total visits made at each coffee shop

Assignment #10:
For this assignment, I used an API names Nominatim to allow the user to search 
for different coffee shops in the Champaign area. I also built a JSON view, as well as
an HTML template view for the page.

Assignment #11 Part 1:
- For this assignment, I created views which would allow the user to download specific 
information from my website and export them into both csv and json files. The url paths I
used for them are:
path('export/visits/csv/', export_visits_csv, name='export_visits_csv'),
path('export/visits/json/', export_visits_json, name='export_visits_json')
- My reports page shows summaries of each visit per coffee shop and the amount of 
minutes spent studying at each coffeeshop, and it displays the total number of visits 
made throughout all the coffee shops

Assignment #11 Part 2:
1. The routes for each of my function and class-based views are protected, meaning they
cannot be accessed by an external user without an account. This is to keep people from
seeing certain information and being able to download user-specific data without their
permission
2. There are no specific public endpoints. The only pages non-authenticated users are 
able to access is the signin/login pages.
3. The post-login page is the map page, which I thought makes the most sense from a user
standpoint, because the first "step" to using the website is to search for coffee shops
to visit. The post log-out page brings the user to the login page once more
4. I added the credentials (mohitg2/graingerlibrary) as an account, so they should work
5. If a user wants to sign up for my website, it functions very similarly to how the 
instructor's does. It will ask for a username and an email. It also asks for a password
that matches specific requirements, (cannot be too similar to your personal information,
cannot be common, must contain 8 characters, etc.) The user then puts in the password
again to confirm it, and then you click the "create account" button to finish the
signup process. Afterward, you are automatically logged in and taken to the map page.

Assignment #12:
- For this assignment, I learned how to structure my settings folder and work between my
local device and PythonAnywhere to deploy my live app.
- I created a settings folder and made production.py, development.py and base.py to 
manage and organize my settings and prepare for deployment
- Then, I went to PythonAnywhere and worked with the bash console to link my local
app to the website using my github repository, cloning my project and uploading my
requirments.txt file
- I also connected my settings, made migrations, and set up my wsgi file
- Afterward, I tried deploying my live app but was unsuccessful. I wam planning to try
and resolve this, as I figured that my production.py settings is not connecting to my
bash file correctly, and I am unsure how to solve this.
