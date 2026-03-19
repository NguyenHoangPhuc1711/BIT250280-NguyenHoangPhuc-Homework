import pandas as pd
import matplotlib.pyplot as plt
cities = pd.read_csv("D:\giả lập pokm\california_cities.csv")
print(cities.columns)
cities['density'] = cities['population_total'] / cities['area_total_km2']
top_density = cities.sort_values(by='density', ascending=False).head(15)
plt.figure(figsize=(10, 6))
plt.barh(top_density['city'], top_density['density'], color="pink")
plt.xlabel('Population Density (people/km2)')
plt.title('Top 15 Most Densely Populated Cities in California')
plt.tight_layout()
plt.gca().invert_yaxis()
plt.show()
plt.show()