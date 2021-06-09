# Source Code used to make the Visualizations

## Description

This directory contains the code used to produce the project visualizations: from getting the data, to processing and plotting the visualizations.

The code is organized as follows:

```fetch_data.py``` : this file contains the class used to get the data from [stats.nba.com](stats.nba.com) using the [```nba_api```](https://github.com/swar/nba_api). The data retrieved was stored into csv files. The files are found in ```src/data/``` 

```process_data.py```: this file contains some functions used to process the data stored in the csv files, making the plotting process easier (and cleaner).

```plot_data.py```: this file contains the functions used to produce the visualizations. All the plots are available in the directory ```plots/```. The plots used images from the players and teams. I got these images from the [stats.nba.com](stats.nba.com) site as well.

```create_plots.py``` and ```create_tables.py```: both files only contains scripts for automating the plotting and table making process. 

## Installation

All the code used Python 3. To install the dependencies you only need to run: ```pip install -r requirements.txt```

## Other stuff

To make this visualizations, I read several articles on plotting shotcharts that may also help you (if you want to make some visualizations of your own).

- JP Hwang has some awesome content about basketball and visualizations, and it really helped me in this process. Links: 

  - [Visualising basketball shots in 2020 - the (big) fundamentals.](https://www.jphwang.com/visualising-basketball-shots-the-basics/)
  -  [NBA shot data analytics & visualization with Python, Pandas and Matplotlib: Part 1 – The basics](https://www.jphwang.com/nba-shot-data-analytics-visualization-with-python-pandas-and-matplotlib-part-1-the-basics/) (this is a three-part series, it is really worth to read it)

- This article is also helpful: [Make a Simple NBA Shot Chart with Python](https://towardsdatascience.com/make-a-simple-nba-shot-chart-with-python-e5d70db45d0d)

- And finally, this article is also really helpful: [How to Create NBA Shot Charts in Python](http://savvastjortjoglou.com/nba-shot-sharts.html). I used his function for drawing the basketball court. 

  
