import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.io
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
df = pd.read_csv('nodespans.csv')
tsnodes = df['T-node-span']
added = df['SE-added-span'].values
addedwrong = df['SE-added-wrong'].values
stsnodes = df['S-node-span']
etsnodes = df['SE-node-span']
# Format and order data
a = added[added!=0]
w = addedwrong[added!=0]
order = np.argsort(tsnodes)
t = tsnodes[order]
s = stsnodes[order]
e = etsnodes[order]

# Figure 5
fig = make_subplots(rows=2, cols=2,
                    subplot_titles=("A)","B)","C)", "D)"),
                   horizontal_spacing=0.13, vertical_spacing=0.14)
# Subplots A and B
fig.add_trace(go.Histogram(x=added, marker=dict(color=colors['red']), nbinsx=20), row=1, col=1)
fig.add_trace(go.Scatter(x=added+1, y=addedwrong+1, marker=dict(color=colors['red'], size=3, opacity=0.2), mode='markers'), row=1,col=2)
fig.add_trace(go.Scatter(x=np.linspace(0,1e8,num=1000), y = np.linspace(0,1e8,num=1000), mode='lines', marker=dict(color=colors['blue'])), row=1,col=2)
fig.add_trace(go.Histogram(x=(w/a), marker=dict(color=colors['red']), nbinsx=20), row=1, col=2)

# Subplots C and D
for (data,color,col) in [(e, colors['red'],2), (s, colors['lgreen'],1),(t, colors['blue'],1),(t, colors['blue'],2)]:
    fig.add_trace(go.Scatter(x=np.arange(data.shape[0]), y=data, mode='markers', marker=dict(color=color, opacity=0.3, size=3)), row=2, col=col)

# Subplot layout formatting
fig.update_xaxes(title= 'Edge Span Added', exponentformat='e', row=1,col=1, title_standoff=3)
fig.update_xaxes(title= 'Added Span', type='log', exponentformat='e', row=1, col=2, title_standoff=3,
                tickmode='array', tickvals = np.array([1,100,1e4,1e6,1e8]),ticktext=['0', '100', '1e+4', '1e+6', '1e+8'])
fig.update_yaxes(title= 'Count', type='log', row=1, col=1)
fig.update_yaxes(title="Incorrectly Added Span", type='log', exponentformat='e', row=1, col=2, title_standoff =3,
                tickmode='array', tickvals = np.array([1,100,1e4,1e6,1e8]), ticktext=['0', '100', '1e+4', '1e+6', '1e+8'])
fig.update_yaxes(title='Node Span', type='log', exponentformat='e', row=2, col=1)
fig.update_yaxes(title='Node Span', type='log', exponentformat='e', row=2, col=2, title_standoff=3)
fig.update_xaxes(title='Rank', row=2,col=1)
fig.update_xaxes(title='Rank', row=2,col=2)
fig.layout.annotations[0].update(x=0.025)
fig.layout.annotations[2].update(x=0.025)
fig.layout.annotations[1].update(x=0.575)
fig.layout.annotations[3].update(x=0.575)
fig.update_layout(showlegend=False)

# matplotlib layout
# choose the figure font
font_dict=dict(family='Arial',
               color='black'
               )
# general figure formatting
fig.update_layout(font=font_dict,  # font formatting
                  plot_bgcolor='white',  # background color
                  margin=dict(r=20,t=20,b=10)  # remove white space 
                  )

# x and y-axis formatting
fig.update_yaxes(
                 showline=True,  # add line at x=0
                 linecolor='black',  # line color
                 linewidth=1, # line size
                 ticks='outside',  # ticks outside axis
                 tickfont=font_dict, # tick label font
                 mirror=True,  # add ticks to top/right axes
                 tickwidth=1,  # tick width
                 tickcolor='black',  # tick color
                 )
fig.update_xaxes(
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
fig.update_layout(width=118.11*6.5, height=118.11*4.5)
# save figure
# fig.show()
plotly.io.write_image(fig,'figure5-plt.pdf', format='pdf')

# Supplement
f = go.Figure()
f.add_trace(go.Histogram(x=(w/a), marker=dict(color=colors['red']), nbinsx=20))
# Plot formatting
f.update_yaxes(type='log', title='Count')
f.update_xaxes(title='Percent Incorrectly Added Span')

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
f.update_layout(width=6.5*118.11, height=3.5*118.11)
# Saving
# f.show()
plotly.io.write_image(f,'figureS4-plt.pdf', format='pdf')