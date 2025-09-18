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
