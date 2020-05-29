from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool

# Create your views here.

def products(request):

    male = 1
    female = 0
    
    counts =[]
    items = ["male", "female"]
    prod = Products.objects.values()
    
    for i in prod:
        if "male" in i.values():
            male += 1
        elif ("female" in i.values()):
            female += 1
       

    counts.extend([male, female,])

    plot = figure(x_range=items, plot_height=600, plot_width=600, tilte="Products", toolbar_loactions="right", tools="pan,wheel-zoom,box_zoom,reset, hover, tap, crosshair")

    plot.tilte.text_font_size = '20pt'

    plot.xaxis.major_label_text_font_size = '14pt'
    plot.vbar(items, top=counts,width=.4, color = "firebrick", legend="Product Counts")
    plot.legend.label_text_font_size = '14pt'

    script, div = components(plot)

    return render(request, 'products.html', {'script': script, 'div':div})