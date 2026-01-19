import pandas as pandas
import numpy as numpy

file = pandas.read_csv('ABADECIOCADA - Data.csv')

title = []
organization = []
cert_Type = []
ratings = []
difficulty = []
students_enrolled = []

for index, row in file.iterrows():
    row = pandas.iloc[index]
    if
