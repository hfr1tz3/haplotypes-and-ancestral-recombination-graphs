import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

colors = {'blue': 'rgb(46,37,133)',
          'red': 'rgb(194,106,119)',
          'lgreen': 'rgb(93,168,153)',
          'gold': 'rgb(220,205,125)',
          'green': 'rgb(51, 117,56)',
          
          'lblue': 'rgb(148,203,236)',
          'magenta': 'rgb(159,74,150)',
          'wine': 'rgb(126,041,084)', 
         }
samplelist = [10, 50, 100, 500, 1000]
lengthlist = [1e6, 5e6, 1e7, 3e7, 5e7]
names = ['1e6', '5e6', '1e7', '3e7', '5e7']
sample_arf = pd.read_csv('figure6-arf-over-sample.csv')
sample_tpr = pd.read_csv('figure6-tpr-over-sample.csv')
length_arf = pd.read_csv('figure6-arf-over-length.csv')
length_tpr = pd.read_csv('figure6-tpr-over-length.csv')

f = make_subplots(rows = 2, cols =2,
                  vertical_spacing=0.11,
                  subplot_titles=['A)','B)','C)','D)'])
for (i, name, group, color, dash, boo) in zip(sample_dis.index, 
                                         ['S','SE','I','IE','IS', 'ISE'],
                                         ['S', 'S', 'I', 'I', 'I', 'I'],
                                         ['blue', 'blue', 'lgreen', 'lgreen','lgreen', 'wine'],
                                         ['dash', None, 'dot', 'dash', None, None],
                                         [True, False, False, False, False, False]):
    f.add_trace(go.Scatter(
        x=lengthlist, y = length_dis.iloc[i].values[1:],
        mode='lines+markers', line=dict(color=colors[color],dash=dash),
        legendgroup=group, name=name, showlegend=True), row=1, col=1)
    f.add_trace(go.Scatter(
        x=lengthlist, y = length_tp.iloc[i].values[1:],
        mode='lines+markers',line=dict(color=colors[color],dash=dash),
        legendgroup=group, name=name, showlegend=False), row=2, col=1)
    f.add_trace(go.Scatter(
        x=samplelist, y=sample_dis.iloc[i].values[1:],
        mode='lines+markers', line=dict(color=colors[color],dash=dash),
        legendgroup=group, name=name, showlegend=False), row=1, col=2)
    f.add_trace(go.Scatter(
        x=samplelist, y=sample_tp.iloc[i].values[1:],
        mode='lines+markers', line=dict(color=colors[color], dash=dash),
        legendgroup=group, name=name, showlegend=False), row=2, col=2)

# Subplot formatting
f.update_xaxes(title='Sample Size', row=2, col=2)
f.update_yaxes(title='ARF', row=1, col=1)
f.update_yaxes(title='TPR', row=2,col=1)
f.update_xaxes(title='Length', row=2,col=1, exponentformat='e')
f.update_xaxes(row=1, col=1, exponentformat='e')
f.layout.annotations[0].update(x=0.025)
f.layout.annotations[2].update(x=0.025)
f.layout.annotations[1].update(x=0.575)
f.layout.annotations[3].update(x=0.575)

# matplotlib layout
# choose the figure font
font_dict=dict(family='Arial',
               color='black'
               )
# general figure formatting
f.update_layout(font=font_dict,  # font formatting
                  plot_bgcolor='white',  # background color
                  margin=dict(r=20,t=20,b=10)  # remove white space 
                  )

# x and y-axis formatting
f.update_yaxes(
                 showline=True,  # add line at x=0
                 linecolor='black',  # line color
                 linewidth=1, # line size
                 ticks='outside',  # ticks outside axis
                 tickfont=font_dict, # tick label font
                 mirror=True,  # add ticks to top/right axes
                 tickwidth=1,  # tick width
                 tickcolor='black',  # tick color
                 )
f.update_xaxes(
                 showline=True,
                 showticklabels=True,
                 linecolor='black',
                 linewidth=1,
                 ticks='outside',
                 tickfont=font_dict,
                 mirror=True,
                 tickwidth=1,
                 tickcolor='black',
                 )
# Sizing
f.update_layout(width=118.11*6.5, height=118.11*5)
f.show()
# Save figure
f.write_image('figure6-plt.pdf', format='pdf', width=118.11*6.5, height=4.5*118.11)