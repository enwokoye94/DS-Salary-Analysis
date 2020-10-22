import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html

def choropleth_map(df, agg, locations, color_scale):
	fig = go.Figure(data=go.Choropleth(locations=df[locations],
		z = df[agg].astype(float),
		locationmode= 'USA-states',
		colorscale = color_scale,
		autocolorscale=False,
    # text = df[agg],
    	marker_line_color = 'white'

                                      ))
	fig.update_layout(
    	title_text='Avg. {} Per State'.format(agg),
        geo = dict(
        	scope='usa',
            projection=go.layout.geo.Projection(type = 'albers usa'),
            showlakes=True, # lakes
            lakecolor='rgb(255, 255, 255)'),
    )

	app = dash.Dash()
	app.layout = html.Div([
    dcc.Graph(figure=fig)
])

	app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter

	fig.show()

choropleth_map(df_state, 'avg_salary', 'state', 'blues' )
