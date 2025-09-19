import pandas as pd
import plotly.express as px

# Prepare data
data = pd.DataFrame({
    "County": ["CT", "BV", "TR", "IS", "MS", "CL", "SV", "MH", "ZJ", "TL", "NT", "HB", "DJ", "GR", "YN", "VJ", "SB", "IN", "PH", "CV", "MK", "DB", "AN", "TM", "VL", "BR", "AR", "OT"],
    "Returned (kg)": [16.9, 11.6, 11.0, 9.6, 9.5, 13.2, 7.5, 12.7, 11.7, 10.3, 8.7, 11.0, 13.4, 11.4, 8.4, 9.2, 11.6, 9.1, 11.9, 9.0, 10.5, 11.6, 10.0, 12.8, 10.7, 9.5, 13.4, 12.5]
})

# Create chart
fig_wind = px.bar_polar(
    data,
    r="Returned (kg)",
    theta="County",
    color="Returned (kg)",
    color_continuous_scale="Viridis",
    title="Radial Comparison of Packaging Returned per County"
)

# Style
fig_wind.update_layout(
    template="plotly_dark",
    paper_bgcolor="black",
    polar_bgcolor="black",
    font=dict(color="white"),
    title_font=dict(size=20),
    title_x=0.5
)

# Add explanation
print("This radial chart compares packaging returned per capita across counties from January to July 2025. Each spoke represents a county, with length and color indicating return quantity. It offers a visual contrast to the geographic distribution shown in the choropleth map.")

# Show chart
fig_wind.show()
