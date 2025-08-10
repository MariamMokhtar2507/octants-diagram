import plotly.graph_objects as go

# Define octant points
points = {
    "1st Octant (+,+,+)": (10, 10, 10),
    "2nd Octant (-,+,+)": (-10, 10, 10),
    "3rd Octant (-,-,+)": (-10, -10, 10),
    "4th Octant (+,-,+)": (10, -10, 10),
    "5th Octant (+,+,-)": (10, 10, -10),
    "6th Octant (-,+,-)": (-10, 10, -10),
    "7th Octant (-,-,-)": (-10, -10, -10),
    "8th Octant (+,-,-)": (10, -10, -10)
}

# Extract coordinates
x_vals = [coord[0] for coord in points.values()]
y_vals = [coord[1] for coord in points.values()]
z_vals = [coord[2] for coord in points.values()]
labels = list(points.keys())

# Create 3D scatter plot
fig = go.Figure(data=[
    go.Scatter3d(
        x=x_vals,
        y=y_vals,
        z=z_vals,
        mode='markers+text',
        text=labels,
        textposition='top center',
        marker=dict(size=6, color='orange'),
        hovertemplate="Point: %{text}<br>X: %{x}<br>Y: %{y}<br>Z: %{z}"
    )
])

# Add X, Y, Z axis lines
fig.add_trace(go.Scatter3d(x=[-20, 20], y=[0, 0], z=[0, 0], mode='lines', line=dict(color='red', width=4), name="X-axis"))
fig.add_trace(go.Scatter3d(x=[0, 0], y=[-20, 20], z=[0, 0], mode='lines', line=dict(color='green', width=4), name="Y-axis"))
fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, 0], z=[-20, 20], mode='lines', line=dict(color='blue', width=4), name="Z-axis"))

# Layout settings
fig.update_layout(
    scene=dict(
        xaxis=dict(range=[-20, 20], title='X'),
        yaxis=dict(range=[-20, 20], title='Y'),
        zaxis=dict(range=[-20, 20], title='Z'),
    ),
    title="Interactive 3D Octant Viewer"
)

# Save as HTML
fig.write_html("index.html", include_plotlyjs="cdn")
print("✅ File saved as 'index.html'. Upload it to GitHub for web access.")



