import json

from flask import Flask
from gevent.pywsgi import WSGIServer

from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import json_item
from bokeh.sampledata.autompg import autompg

from numpy import cos, linspace
from flask_cors import CORS

app = Flask(__name__)
# CORS enabled so react frontend can pull data from python backend
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/plot1')
def plot1():
    # copy/pasted from Bokeh Getting Started Guide - used as an example
    x = linspace(-6, 6, 100)
    y = cos(x)
    p = figure(width=500, height=500, toolbar_location="below", title="Plot 1")
    p.circle(x, y, size=7, color="firebrick", alpha=0.5)
    return json.dumps(json_item(p, "myplot"))


@app.route('/plot2')
def plot2():
    # copy/pasted from Bokeh Getting Started Guide - used as an example
    grouped = autompg.groupby("yr")
    mpg = grouped.mpg
    avg, std = mpg.mean(), mpg.std()
    years = list(grouped.groups)
    american = autompg[autompg["origin"]==1]
    japanese = autompg[autompg["origin"]==3]

    p = figure(title="MPG by Year (Japan and US)")

    p.vbar(x=years, bottom=avg-std, top=avg+std, width=0.8, 
        fill_alpha=0.2, line_color=None, legend="MPG 1 stddev")

    p.circle(x=japanese["yr"], y=japanese["mpg"], size=10, alpha=0.5,
            color="red", legend="Japanese")

    p.triangle(x=american["yr"], y=american["mpg"], size=10, alpha=0.3,
            color="blue", legend="American")

    p.legend.location = "top_left"
    return json.dumps(json_item(p, "myplot"))


# Using WSGI server to allow self contained server
http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()