import plotly.express as px
import pandas as pd

# Read data
data = pd.read_csv('world_fires_1_day.csv')

# Create the initial plot
fig = px.scatter_geo(data, lon='longitude', lat='latitude',
                     size='brightness', color='brightness',
                     color_continuous_scale='YlOrRd',
                     projection='orthographic',
                     labels={'color': 'Brightness'},
                     hover_name='brightness', size_max=50)

# Define frames for rotation animation
frames = [
    {
        'name': str(i),
        'data': [fig.data[0]],  # Use the same data from the initial plot
        'layout': {
            'geo': {
                'projection': {
                    'type': 'orthographic',
                    'rotation': {'lon': i, 'lat': 0}
                }
            }
        }
    }
    for i in range(0, 360, 6)
]

# Add the frames to the figure
fig.frames = frames

# Update layout and add the play button
fig.update_layout(
    geo=dict(
        showland=True, landcolor='lightgreen',
        showocean=True, oceancolor='lightblue',
        showlakes=True, lakecolor='lightblue',
        showcoastlines=True, coastlinecolor='black',
        showrivers=True, rivercolor='lightblue', riverwidth=1.5,
        bgcolor='#1e1e1e', showframe=True, framecolor='#801515'
    ),
    title=dict(
        text='World Fires Map',
        x=0.5,  # Center the title
        y=0.95,  # Adjust position (higher up)
        font=dict(size=35, color='white', family='Arial Black'),
    ),
    coloraxis_colorbar=dict(
        title="Brightness",
        tickvals=[0, 50, 100, 150, 200],
        ticktext=['0', '50', '100', '150', '200'],
    ),
    paper_bgcolor='#1e1e1e',
    margin=dict(l=20, r=85, t=80, b=20),
    updatemenus=[{
        'buttons': [
            {'label': 'Play', 'method': 'animate', 'args': [None, {'frame': {'duration': 50, 'redraw': True}, 'fromcurrent': True}]}
        ]
    }]
)

fig.update_traces(
    marker=dict(
        colorscale='YlOrRd',
        line=dict(width=0.5, color='black'),
        opacity=1,
    )
)

fig.show()
