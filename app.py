import dash
from dash import html, dcc
from dash.dependencies import Input, Output

# Initialize the Dash app
app = dash.Dash(__name__)

# Create the layout with a button and output text
app.layout = html.Div([
    html.H1("Interactive Dash Website"),
    html.P("Click the button to change the text below."),
    html.Button("Click Me!", id="button"),
    html.Div(id="output-text")
])

# Set up the callback to change the output text when the button is clicked
@app.callback(
    Output("output-text", "children"),
    Input("button", "n_clicks")
)
def update_output(n_clicks):
    if n_clicks is None:
        return "The button hasn't been clicked yet."
    else:
        return f"You clicked the button {n_clicks} times."

if __name__ == '__main__':
    app.run_server(debug=True)