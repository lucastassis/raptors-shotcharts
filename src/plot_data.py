'''
Functions used to plot the player's data
'''
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc
from matplotlib.offsetbox import  OffsetImage

from scipy.stats import kde
import numpy as np
from PIL import Image
import process_data as process_data

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
    return ax

'''
Function for plotting some player's shotchart based on the league averages
'''
def plot_scatter_zone(player_data, league_data, player_name='Kyle Lowry', player_img='./team_imgs/kylelowry.png', out_path='scatter.png', season='2019-20',savefig=True, show_plot=False):
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
    
    # plotting players
    plot_im = OffsetImage(load_img, zoom=0.15)
    plot_im.set_offset((2780, 3200))

    # plotting logo
    # plot_im = OffsetImage(load_img, zoom=0.25)
    # plot_im.set_offset((2950, 3200)) # for logo

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
def plot_density(player_data, title='Toronto Raptors', player_img='./team_imgs/logo.png', out_path='density.png', season='2019-20', savefig=True, show_plot=False):
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
    plt.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='auto', rasterized=False, cmap='coolwarm')

    # plot colorbar
    position= fig.add_axes([0.7,0.92,0.2,0.03])
    cbar = plt.colorbar(cax=position, orientation="horizontal", ticks=[])
    cbar.ax.tick_params(size=0)
    plt.title('Shots Attempted', fontdict={'weight':'bold'})

    # player pic
    load_img = plt.imread(player_img)
    plot_im = OffsetImage(load_img, zoom=0.25)
    plot_im.set_offset((2950, 3200))
    ax.add_artist(plot_im) 

    # plot title
    ax.set_title(f'{title}\n{season} Regular Season', fontdict={'fontsize':40, 'weight':'bold'}, loc='left')

    if savefig:
        plt.savefig(out_path, dpi=300, bbox_inches='tight')
    if show_plot:
        plt.show()
    plt.close('all')

'''
Function for plotting fg per feet
'''
def plot_fg_per_feet(player_data, player_name='Kyle Lowry', player_img='./team_imgs/kylelowry.png', out_path='fg_per_feet.png', season='2019-20', save_fig=True, show_plot=False):
    mpl.rc('text', usetex=True)
    mpl.rcParams['font.family'] = 'STIXGeneral'
    mpl.rcParams['font.size'] = 14
    plt.style.use('dark_background') 

    # processing the data
    data = process_data.fg_per_feet(player_data)
    shot_feet = data['SHOT_DISTANCE'].to_numpy()
    idx = list(np.where(shot_feet < 35)) # get only shots with distance < 35ft
    shot_feet = shot_feet[tuple(idx)] # array containing shot distances
    percentage_per_feet = data['SHOT_MADE_FLAG']['mean'].to_numpy()[tuple(idx)] * 100 # fg percentage per feet
    shots_per_feet = data['SHOT_MADE_FLAG']['count'].to_numpy()[tuple(idx)] # frequency of shots per feet
    fgp = process_data.get_fgp(player_data) # fg percentage

    # create plot
    fig, ax = plt.subplots(figsize=(15, 5))
    plt.xlim([-0.4, 35])
    plt.ylim([0, 100])    
    plt.plot(np.arange(0, 35, 1), 35 * [fgp], color='white', linestyle='dashed', zorder=1) # plot players fg percentage
    plt.plot(100 * [22], np.arange(0, 100, 1), color='white', alpha=0.5, zorder=1) # plot 3pt line
    plt.plot(100 * [24], np.arange(0, 100, 1), color='white', alpha=0.5, zorder=1) # plot 3pt line
    plt.scatter(shot_feet, percentage_per_feet, s=shots_per_feet * 5, color='#bd1b21', marker='o', zorder=2) # plot shots
    
    # texts + title
    plt.text(30, fgp + 3, f'FG(\%) = {fgp}\%') # fg% text
    plt.text(9, 80,'2 points', fontdict={'fontsize':12})
    plt.text(23, 80, '2 points\n+\ncorner 3', fontdict={'fontsize':12}, ha='center', va='center')
    plt.text(29, 80, '3 points', fontdict={'fontsize':12})
    ax.set_title(f'{player_name}\n{season} Regular Season', fontdict={'fontsize':25}, loc='left')
    ax.set_ylabel('FG(\%)')
    ax.set_xlabel('ft')

    # load img
    load_img = plt.imread(player_img)

    # plot player
    plot_im = OffsetImage(load_img, zoom=0.1)
    plot_im.set_offset((3250, 1340))
   
    # # plotting logo
    # plot_im = OffsetImage(load_img, zoom=0.18)
    # plot_im.set_offset((3400, 1330))
    
    # add img
    ax.add_artist(plot_im) 

    if save_fig:
        plt.savefig(out_path, dpi=300, bbox_inches='tight')
    if show_plot:
        plt.show()

'''
Function for plotting shot frequency per feet
'''
def plot_freq_per_feet(player_data, player_name='Toronto Raptors', player_img='./team_imgs/logo.png', out_path='freq_per_feet.png', season='2019-20', save_fig=True, show_plot=False):
    mpl.rc('text', usetex=True)
    mpl.rcParams['font.family'] = 'STIXGeneral'
    mpl.rcParams['font.size'] = 14
    plt.style.use('dark_background')

    # processing the data
    data = process_data.freq_per_feet(player_data)
    shot_distance = data['SHOT_DISTANCE'].to_numpy()
    idx = list(np.where(shot_distance < 35))
    shot_distance = shot_distance[tuple(idx)]
    shot_freq = data['COUNT'].to_numpy()[tuple(idx)]

    # plot
    fig, ax = plt.subplots(figsize=(15, 5))
    plt.xlim([-.6, 35])
    plt.ylim([0, 20])
    plt.bar(shot_distance, shot_freq, color='#bd1b21', zorder=2)
    plt.plot(30 * [21.5], np.arange(0, 30, 1), color='white', alpha=0.5, zorder=1) # plot 3pt line
    plt.plot(30 * [23.5], np.arange(0, 30, 1), color='white', alpha=0.5, zorder=1) # plot 3pt line

    # texts + title
    plt.text(9, 17,'2 points', fontdict={'fontsize':12})
    plt.text(22.5, 17, '2 points\n+\ncorner 3', fontdict={'fontsize':12}, ha='center', va='center')
    plt.text(28, 17, '3 points', fontdict={'fontsize':12})
    ax.set_title(f'{player_name}\n{season} Regular Season', fontdict={'fontsize':25}, loc='left')
    ax.set_ylabel('Frequency (\%)')
    ax.set_xlabel('ft')

    # load img
    load_img = plt.imread(player_img)

    # # plot player
    # plot_im = OffsetImage(load_img, zoom=0.1)
    # plot_im.set_offset((3250, 1340))
   
    # plotting logo
    plot_im = OffsetImage(load_img, zoom=0.18)
    plot_im.set_offset((3400, 1320))
    
    # add img
    ax.add_artist(plot_im) 

    if save_fig:
        plt.savefig(out_path, dpi=300, bbox_inches='tight')
    if show_plot:
        plt.show()


if __name__ == "__main__":
    import pandas as pd 

    # load the data
    player_data = pd.read_csv('./data/2020-21/roster_data.csv')
    league_data = pd.read_csv('./data/2020-21/league_averages.csv')

    # plot the data
    # plot_scatter_zone(player_data, league_data, player_name='Toronto Raptors', player_img='./team_imgs/logo.png', season='2019-20', show_plot=False)
    # plot_density(player_data, out_path='2019-20.png', season='2019-20', show_plot=False)
    # plot_fg_per_feet(player_data, player_name='Kyle Lowry', player_img='./team_imgs/kylelowry.png', season='2019-20')
    plot_freq_per_feet(player_data, player_name='Toronto Raptors', player_img='./team_imgs/logo.png', out_path='roster_freq_per_feet.png', season='2020-21')



