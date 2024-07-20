from dash import Dash, html

app = Dash()

app.layout = [html.Div(children='hello, world')]

if __name__ == '__main__':
    app.run(debug=True)
