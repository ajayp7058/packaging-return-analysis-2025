from IPython.display import Image, display
import matplotlib.pyplot as plt

# Create figure and axes with black background
fig, ax = plt.subplots(1, 1, figsize=(12, 10), facecolor='black')
ax.set_facecolor('black')  # Set axes background

# Normalize the data to enhance color contrast
col = "Total quantity (kg) of packaging returned in the Deposit-Return System, per capita, January – July 2025"
merged["normalized"] = (merged[col] - merged[col].min()) / (merged[col].max() - merged[col].min())

# Plot the choropleth with high-contrast colormap
merged.plot(
    column="normalized",
    cmap="plasma",  # Works well on dark backgrounds
    linewidth=0.8,
    edgecolor='white',
    legend=True,
    ax=ax
)

# Add labels at the centroid of each county — now in black
for idx, row in merged.iterrows():
    centroid = row["geometry"].centroid
    value = row[col]
    ax.text(centroid.x, centroid.y, f"{value:.1f}", fontsize=8, ha='center', va='center', color='black')

# Style title and remove axes
plt.title("Packaging Returned per Capita by County (Jan–July 2025)", fontsize=15, color='white')
plt.axis('off')

# Save and display
plt.savefig("choropleth_map.png", dpi=300, facecolor='black')
plt.close()
display(Image(filename="choropleth_map.png"))
