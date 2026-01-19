import pandas as pd

df = pd.read_csv('ABADECIOCADA - Data.csv', header=1)

org_stats = df.groupby('course_organization').agg({
    'course_students_enrolled': 'sum',
    'course_rating': ['mean', 'median', 'var', 'std']
}).reset_index()

org_stats.columns = ['Organization', 'Enrolled Students', 'Mean Rating',
                     'Median Rating', 'Variance Rating',
                     'Standard Deviation Rating']

top5_orgs = org_stats.sort_values('Enrolled Students', ascending=False).head(5)
top5_orgs.insert(0, 'Ranking', range(1, 6))
top5_orgs = top5_orgs.reset_index(drop=True)

def get_mode(x):
    return x.mode()[0] if not x.mode().empty else x.mean()

org_stats = df.groupby('course_organization').agg({
    'course_students_enrolled': 'sum',
    'course_rating': ['mean', 'median', get_mode, 'var', 'std']
}).reset_index()

org_stats.columns = ['Organization', 'Enrolled Students', 'Mean Rating',
                     'Median Rating', 'Mode Rating', 'Variance Rating',
                     'Standard Deviation Rating']

top5_orgs = org_stats.sort_values('Enrolled Students', ascending=False).head(5)
top5_orgs.insert(0, 'Ranking', range(1, 6))
top5_orgs = top5_orgs.reset_index(drop=True)

print(top5_orgs)