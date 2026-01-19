import pandas as pandas
import numpy as numpy

file = pandas.read_csv('ABADECIOCADA - Data.csv')

title = file['course_title']
organization = file['course_organization']
cert_Type = file['courrse_Certificate_type']
ratings = file['course_rating']
difficulty = file['course_difficulty']
students_enrolled = file['course_student_enrolled']

temp_array = []

for i in range(len(title)):

org_ratings = temp_array.append(ratings)
