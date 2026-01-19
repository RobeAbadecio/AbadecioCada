import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('ABADECIOCADA - Data.csv', header=1)

df['course_students_enrolled'] = df['course_students_enrolled'].astype(str).str.replace(',', '').astype(float)
df['course_rating'] = pd.to_numeric(df['course_rating'], errors='coerce')

df = df.dropna(subset=['course_organization', 'course_rating', 'course_students_enrolled'])

def get_mode(x):
    mode_result = x.mode()
    return mode_result[0] if len(mode_result) > 0 else np.nan

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

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
print("\n" + "="*100)
print("TOP 5 ORGANIZATIONS:")
print("="*100)
print(top5_orgs)

top5_org_names = top5_orgs['Organization'].tolist()

top5_df = df[df['course_organization'].isin(top5_org_names)]

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for i, org in enumerate(top5_org_names):
    org_data = top5_df[top5_df['course_organization'] == org]['course_rating']

    mean_val = org_data.mean()
    median_val = org_data.median()
    mode_val = org_data.mode()[0] if len(org_data.mode()) > 0 else np.nan

    axes[i].hist(org_data, bins=20, color='skyblue', edgecolor='black', alpha=0.7)

    axes[i].axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_val:.2f}')
    axes[i].axvline(median_val, color='green', linestyle='--', linewidth=2, label=f'Median: {median_val:.2f}')
    axes[i].axvline(mode_val, color='orange', linestyle='--', linewidth=2, label=f'Mode: {mode_val:.2f}')

    axes[i].set_title(f'{org}\n(Rank #{i + 1})', fontsize=10, fontweight='bold')
    axes[i].set_xlabel('Course Rating')
    axes[i].set_ylabel('Frequency')
    axes[i].legend(fontsize=8)
    axes[i].grid(axis='y', alpha=0.3)

fig.delaxes(axes[5])

plt.tight_layout()
plt.savefig('top5_organizations_histogram.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nHistogram saved as 'top5_organizations_histogram.png'")