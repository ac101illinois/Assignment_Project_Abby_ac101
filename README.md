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
