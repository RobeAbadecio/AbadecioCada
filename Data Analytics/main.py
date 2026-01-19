import csv
import numpy as np
import matplotlib.pyplot as plt
file_path = "D:/School/3rd_2nd/Data Analytics/ABADECIOCADA - Data.csv"
#unique list
seen=set()
#data storage
course_title=[]
course_organization=[]
course_Certificate_type=[]
course_rating=[]
course_difficulty=[]
course_students_enrolled=[]
unique_organization=[]
unique_rating=[]
unique_course=[]
unique_population=[]
Advanced_rating=[]
#csv to arrays
with open(file_path, "r", encoding="utf-8") as csvfile:
    content = csv.reader(csvfile)
    next(content)
    next(content)
    for line in content:
       course_title.append(line[1])
       course_organization.append(line[2])
       course_Certificate_type.append((line[3]))
       course_rating.append(float(line[4]))
       course_difficulty.append(line[5].strip())
       course_students_enrolled.append(float(line[6].replace(",", "")))

#retrieving unique organization
for item in course_organization:
    if item not in seen:
        unique_rating.append(0)
        unique_population.append(0)
        Advanced_rating.append(0)
        unique_organization.append(item)
        seen.add(item)
#ratings
#while in range count unique_org
#if unique_org[x] = org[y]
#   unique_rating[x]=unique_rating[x]+rating[y]
#   instance+1
# unique_rating[x]=unique_rating[x]/instance
x=0
for item in unique_organization:
    y = 0
    instance = 0
    for items in course_organization:
        if item==items:
            unique_rating[x]=unique_rating[x]+course_rating[y]
            instance=instance+1
        y=y+1
    unique_rating[x] = unique_rating[x] / instance
    x=x+1

#number of unique course
for item in unique_organization:
    unique_course.append(course_organization.count(item))

#unique population per course
x=0
for item in unique_organization:
    y = 0
    instance = 0
    for items in course_organization:
        if item==items:
            unique_population[x]=unique_population[x]+course_students_enrolled[y]
        y=y+1
    unique_population[x] = unique_population[x] / unique_course[x]
    x = x + 1
#Advanced rating
#for each unique organization
#   check each instance of that organization on the data
#   if it matches, check if the difficulty is Advanced
# if so, instance +1 then add that rating to advanced_rating.
# after checking all, divide the advanced rating to the instance to get  the average
# Advanced rating
for x, org_name in enumerate(unique_organization):
    total_rating = 0.0
    instance_count = 0
# based on each unique organization
    for y, course_org in enumerate(course_organization):
# iterate the database to search for its instance and if the difficulty is advanced
        if org_name == course_org and course_difficulty[y].strip() == "Advanced":
            total_rating += course_rating[y]
            instance_count += 1

#error handling
    if instance_count > 0:
        Advanced_rating[x] = total_rating / instance_count
    else:
        Advanced_rating[x] = 0

# conclusion

#top-rated org
#binding
combined = zip(unique_rating, unique_organization)
#sort
sorted_combined = sorted(combined, reverse=True)
#store
sorted_ratings, sorted_orgs_rating = zip(*sorted_combined)

#top population-per-course
combined = zip(unique_population, unique_organization)
sorted_combined = sorted(combined, reverse=True)
sorted_population,sorted_orgs_population = zip(*sorted_combined)

#top offered course number
combined = zip(unique_course, unique_organization)
sorted_combined = sorted(combined, reverse=True)
sorted_course, sorted_orgs_course = zip(*sorted_combined)

#top advanced rating
combined = zip(Advanced_rating, unique_organization)
sorted_combined = sorted(combined, reverse=True)
sorted_advanced, sorted_orgs_advanced = zip(*sorted_combined)

print( "ranking | rating | population per course | no of courses | advanced rating")
x=0
while x < 5:
    print(x+1," ",sorted_orgs_rating[x],"[",sorted_ratings[x],"]"," | ",sorted_orgs_population[x],"[",sorted_population[x],"]"," | ",sorted_orgs_course[x],"[",sorted_course[x],"]"," | ",sorted_orgs_advanced[x],"[",sorted_advanced[x],"]")
    x=x+1
top_n = 5
plt.figure()
plt.bar(sorted_orgs_advanced[:5], sorted_advanced[:5])
plt.xlabel("Organization")
plt.ylabel("Average Advanced Course Rating")
plt.title("Top 5 Organizations by Advanced Course Ratings")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


