import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc
from matplotlib.offsetbox import  OffsetImage

from scipy.stats import kde
import numpy as np
from PIL import Image
from . import process_data
'''
Function for drawing the basketball court (Source: http://savvastjortjoglou.com/nba-shot-sharts.html)
'''
def draw_court(ax=None, color='black', lw=2, outer_lines=False):
    # If an axes object isn't provided to plot onto, just get current one
    if ax is None:
        ax = plt.gca()
    # Create the various parts of an NBA basketball court
    # Create the basketball hoop
    # Diameter of a hoop is 18" so it has a radius of 9", which is a value
    # 7.5 in our coordinate system
    hoop = Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False)
    # Create backboard
    backboard = Rectangle((-30, -7.5), 60, -1, linewidth=lw, color=color)
    # The paint
    # Create the outer box 0f the paint, width=16ft, height=19ft
    outer_box = Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color,
                        fill=False)
    # Create the inner box of the paint, widt=12ft, height=19ft
    inner_box = Rectangle((-60, -47.5), 120, 190, linewidth=lw, color=color,
                        fill=False)
    # Create free throw top arc
    top_free_throw = Arc((0, 142.5), 120, 120, theta1=0, theta2=180,
                        linewidth=lw, color=color, fill=False)
    # Create free throw bottom arc
    bottom_free_throw = Arc((0, 142.5), 120, 120, theta1=180, theta2=0,
                            linewidth=lw, color=color, linestyle='dashed')
    # Restricted Zone, it is an arc with 4ft radius from center of the hoop
    restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=lw,
                    color=color)
    # Three point line
    # Create the side 3pt lines, they are 14ft long before they begin to arc
    corner_three_a = Rectangle((-220, -47.5), 0, 140, linewidth=lw,
                            color=color)
    corner_three_b = Rectangle((220, -47.5), 0, 140, linewidth=lw, color=color)
    # 3pt arc - center of arc will be the hoop, arc is 23'9" away from hoop
    # I just played around with the theta values until they lined up with the 
    # threes
    three_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=lw,
                    color=color)
    # Center Court
    center_outer_arc = Arc((0, 422.5), 120, 120, theta1=180, theta2=0,
                        linewidth=lw, color=color)
    center_inner_arc = Arc((0, 422.5), 40, 40, theta1=180, theta2=0,
                        linewidth=lw, color=color)
    # List of the court elements to be plotted onto the axes
    court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw,
                    bottom_free_throw, restricted, corner_three_a,
                    corner_three_b, three_arc, center_outer_arc,
                    center_inner_arc]
    if outer_lines:
        # Draw the half court line, baseline and side out bound lines
        outer_lines = Rectangle((-250, -47.5), 500, 470, linewidth=lw,
                                color=color, fill=False)
        court_elements.append(outer_lines)
    # Add the court elements onto the axes
    for element in court_elements:
        ax.add_patch(element)
    #ax.set_facecolor('brown')
    return ax

'''
Function for plotting some player's shotchart based on the league averages
'''
def plot_scatter_zone(player_data, league_data, player_name='Kyle Lowry', player_img='./players_pics/kylelowry.png', out_path='scatter.png', season='2019-20',savefig=True, show_plot=True):
    plt.style.use('dark_background')

    mpl.rc('text', usetex=True)
    mpl.rcParams['font.family'] = 'STIXGeneral'
    mpl.rcParams['font.size'] = 14
    
    # basic fig definitions
    fig, ax = plt.subplots(figsize=(12, 11))
    plt.xlim(250, -250)
    plt.ylim(-47.5, 422.5)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.set_aspect('equal')
    plt.tight_layout()  
    
    # draw the court
    draw_court(ax, outer_lines=True, color='white')
    
    # data processing
    player_fg_zone = process_data.player_fg_zone(player_data)
    league_fg_zone = process_data.league_fg_zone(league_data)
    
    # scatter plot per zone
    zones = player_fg_zone.index.to_numpy()
    for zone in zones:
        data = process_data.player_loc_zone(player_data, zone)
        fgm = process_data.player_fgm(data)
        player_percentage = player_fg_zone.loc[zone].item()
        league_percentage = league_fg_zone.loc[zone].item()
        fgd = player_percentage - league_percentage
        plt.scatter(fgm['LOC_X'], fgm['LOC_Y'], s=110, c=len(fgm)*[fgd], cmap='coolwarm', alpha=1, norm=mpl.colors.Normalize(vmin=-7.5, vmax=7.5))
    
    # plot colorbar
    position= fig.add_axes([0.7,0.92,0.2,0.03])
    cbar = plt.colorbar(cax=position, orientation="horizontal", ticks=[-7.5, 7.5])
    cbar.ax.set_xticklabels(['Below\nLeague Average ', 'Above\nLeague Average'])
    cbar.ax.tick_params(size=0)
    plt.title('Efficiency by Location', fontdict={'weight':'bold'})
    
    # plot title
    ax.set_title(f'{player_name}\n{season} Regular Season', fontdict={'fontsize':40, 'weight':'bold'}, loc='left')
    load_img = plt.imread(player_img)
    plot_im = OffsetImage(load_img, zoom=0.15)
    plot_im.set_offset((2780, 3200))
    ax.add_artist(plot_im)    
    # save and plot fig
    if savefig:
        plt.savefig(out_path, dpi=300, bbox_inches='tight')   
    if show_plot:
        plt.show()        
    plt.close('all')

'''
Function for plotting the density (or heatmap) visualization of some player's data
'''
def plot_density(player_data, savefig=True, show_plot=True):
    mpl.rc('text', usetex=True)
    mpl.rcParams['font.family'] = 'STIXGeneral'
    mpl.rcParams['font.size'] = 14
    plt.style.use('dark_background')

    
    # basic fig definitions
    fig, ax = plt.subplots(figsize=(12, 11))
    plt.xlim(250, -250)
    plt.ylim(-47.5, 422.5)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.set_aspect('equal')
    plt.tight_layout()  

    # create density plot
    nbins=500
    k = kde.gaussian_kde([player_data['LOC_X'], player_data['LOC_Y']])
    xi, yi = np.mgrid[-250:250:nbins*1j, 422.5:-47.5:nbins*1j]
    zi = k(np.vstack([xi.flatten(), yi.flatten()]))
    draw_court(outer_lines=True)
    plt.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='auto', rasterized=False, cmap='inferno')

    # plot colorbar
    position= fig.add_axes([0.7,0.92,0.2,0.03])
    cbar = plt.colorbar(cax=position, orientation="horizontal", ticks=[0, ])
    #cbar.ax.set_xticklabels(['Below\nLeague Average ', 'Above\nLeague Average'])
    cbar.ax.tick_params(size=0)
    plt.title('Shots Attempted', fontdict={'weight':'bold'})

    # plot title
    ax.set_title('Kyle Lowry\n2019-20 Regular Season', fontdict={'fontsize':40, 'weight':'bold'}, loc='left')

    if savefig:
        plt.savefig('density.png', dpi=300, bbox_inches='tight')
    # if show_plot:
    #     plt.show()
    plt.close('all')


if __name__ == "__main__":
    import pandas as pd 

    # load the data
    player_data = pd.read_csv('../data/2020-21/kylelowry.csv')
    league_data = pd.read_csv('../data/2020-21/league_averages.csv')

    # plot the data
    plot_scatter_zone(player_data, league_data)
    #plot_density(player_data)



