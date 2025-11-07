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

