# Visualizing Shotcharts from the Toronto Raptors 2019-20 and 2020-21 Seasons

[TOC]

## Introduction

The 2020-21 NBA Regular Season has finished for a while now, and we are already somewhat deep in the 2021 playoffs. And for the first time in eight seasons, the Toronto Raptors are out of the postseason (at least we get to watch other teams suffer without suffering ourselves... right?). And there may be plenty of reasons: moving to Tampa, health-and-safety protocols, injuries, losing Serge Ibaka and Marc Gasol in the offseason... we can go on for a long time. But, in this article (?), I tried to make some visualizations to find some other reasons (particularly in the offensive end) why a team that had a 53-19 record in the 2019-20 season fell to 27-45 in the 2020-21 season.

There are hundreds of articles that are written by people who understand way more than me... and it is probable that these visualizations will not provide much insight on the situation, given that there was an infinity of outside-basketball reasons that are not accounted for in these graphs... however, this is a nice exercise (well, at least for me). 

## The data

The first thing I did was to gather some data about the 2019-20 and 2020-21 seasons. I used the [nba_api]() to fetch this data. Then I had to decide what data to use (which players, etc, etc). I ended up deciding to analyze the full roster data for both seasons, and also the data of what I called the *core four*. The *core four* are Kyle Lowry, Fred VanVleet, Pascal Siakam, and OG Anunoby. I did not choose Norman Powell because, well, he is not in the Raptors anymore (unfortunately). And Chris Boucher was left out because he wasn't in the rotation so much as he was this year (well, if I do this again next year, he might earn a spot given his growth throughout this season). Another important thing is that, in the roster data from the 2020-21 seasons, I did not use data from the rookies: Malachi Flynn, Jalen Harris, and Freddie Gillespie. Unfortunately, the API did not find the data for them. I don't think that it would make that much impact on the results (I might be wrong), but we might as well take this into account when analyzing the data.

Anyway, the data consists of the location of the players in all their shots taken this season. We also consider 7 (there are 6 that are more important) areas on the court: Restricted Area, Paint, Mid-range, Above the Break 3, Left Corner 3, Right Corner 3... and Backcourt (which isn't that important in the big picture).

With the basic definitions out there, we may as well start this thing.

## The visualizations

### The full team

So, I will start showing the data from the full roster.

| <img src="/home/lucas/Documents/codes/nba/raptors-shotcharts/plots/2019-20/roster_scatter.png" style="zoom:12.5%;" /><img src="/home/lucas/Documents/codes/nba/raptors-shotcharts/plots/2020-21/roster_scatter.png" style="zoom:12.5%;" /> |      |
| ------------------------------------------------------------ | ---- |

Okay, so this first figure presents all the shots made by the Toronto Raptors in both seasons. The color indicates the efficiency (FG%) compared to the league average in the respective year (the redder, the better). Analyzing this first visualization, we observe that the shots distribution seem mostly similar. However, there are some differences in efficiency. In the 2019-20 season, the Raptors had a better FG% above the break 3 pointer. From the corners, they are close to the average in both seasons. Now, we also observe that the Raptors are not a good mid-range team (well, at least for me, this result is expected given the eye-test). They are only OK in the paint and restricted area too. But this Figure alone does not give us much insight (I said before, I am not promising anything). However, It is clear that they shot better from above the break 3 in the season 2019-20, but the number of shots is not that clear in this scatter plot. This is why I made the next Figure.

<img src="/home/lucas/Documents/codes/nba/raptors-shotcharts/plots/2019-20/roster_freq_per_feet.png" style="zoom: 20%;" />

<img src="/home/lucas/Documents/codes/nba/raptors-shotcharts/plots/2020-21/roster_freq_per_feet.png" style="zoom:20%;" />

Okay, now these Figures illustrate the frequency of shots taken by feet. This way, we can better observe the number of shots taken by the team in each area. Now, I guess we have our first "oh-oh" moment. Looking at the three-pointers, they seem mostly the same, but close to the paint... there is a big change. Well, at the beginning of this article(?) I actually said something that may have some influence on this: "losing Serge Ibaka and Marc Gasol in the offseason". Ibaka and Gasol were both pretty solid pieces that helped the team function well both offensively and defensively. They were substituted by Aron Baynes, who did not perform well. And it is nothing personal with Baynes, the team just did not seem to have good chemistry with him on the floor (also, the missed layups and putbacks). So here we may have some clues about some things that went wrong... but again, there is nothing new... everyone on Twitter said this about 2000 times. Well... now it is backed by data (or at least seems to be). But you might be thinking: "Okay... they shot more, but did they make more?". This is answered by this next figure.

<img src="/home/lucas/Documents/codes/nba/raptors-shotcharts/plots/2019-20/roster_fg_per_feet.png" style="zoom:20%;" />

<img src="/home/lucas/Documents/codes/nba/raptors-shotcharts/plots/2020-21/roster_fg_per_feet.png" style="zoom:20%;" />

... and the answer is yes! They also shot better. From 0 ft (layup, dunks, and stuff) they had close to 80% accuracy, which is good when you are taking almost 10% of your shots from there. Yes, after that is pretty similar, I know, but in the 2020-21 season, they had way fewer shots from close range, despite having a similar accuracy. In this way, they exchanged some good shots for far 3s and mid-range shots. By the way, the size of the scatter represents the number of shots per feet, so the bigger, the more shots.

So we already see some differences that may not be one of the main reasons, but it can indicate some things. And I also know people tweeted this many times, but as I said before, now it is backed by data (I guess some people on Twitter might say things backed by data too... but I spent some time on this, so let's imagine it wasn't). Anyway, now we move to the *core four*.

### The core four

The core four consist of the main players of this Raptors team, or at least who I consider the main players. We will follow the data similar to what I did previously. So, first, let's have a look at their shots compared to the league averages.

#### Fred VanVleet

We start by showing Freddy's numbers.

| <img src="/home/lucas/Documents/codes/nba/raptors-shotcharts/plots/2019-20/fredvanvleet.png" style="zoom:12.5%;" /><img src="/home/lucas/Documents/codes/nba/raptors-shotcharts/plots/2020-21/fredvanvleet.png" style="zoom:12.5%;" /> |      |
| ------------------------------------------------------------ | ---- |

One thing that pops up is the mid-range, paint, and restricted area. We already know this: Fred needs to step up in his 2s game in order to hit the next level. In the three-pointers he also took a step back (no pun intended), he shot way better from the corners last season. But Fred had a rough path with COVID... so it is really hard to get something out of this because he did play some games that he wasn't 100%, or as he said: "hitting a wall". Even with his shooting being down this year, he was really solid pre-health-and-safety protocols. I also plotted his frequency per feet.

<img src="/home/lucas/Documents/codes/nba/raptors-shotcharts/plots/2019-20/fredvanvleet_fg_per_feet.png" style="zoom: 20%;" />

<img src="/home/lucas/Documents/codes/nba/raptors-shotcharts/plots/2020-21/fredvanvleet_fg_per_feet.png" style="zoom: 20%;" />

In these figures, it becomes more clear that Fred had an off-year shooting-wise. He also took more threes this year than in the 2019-20 season. But, as said many times, it is really hard to really evaluate Fred given his time after COVID.

#### Kyle Lowry

The next up is no one less than the greatest raptor of all time: Kyle Lowry.  So, let's take a look at Kyle's shotcharts.

| <img src="/home/lucas/Documents/codes/nba/raptors-shotcharts/plots/2019-20/kylelowry.png" style="zoom: 12.5%;" /><img src="/home/lucas/Documents/codes/nba/raptors-shotcharts/plots/2020-21/kylelowry.png" style="zoom: 12.5%;" /> |      |
| ------------------------------------------------------------ | ---- |

Kyle is a veteran of the game and does not seem to be slowing down. His 3 point shooting was better this year, especially from the corners (look at that right corner). His mid-range and paint game seems to be pretty similar. Let's be real Kyle played a really solid season and we will always have the Lakers game. Just to keep it consistent, let's take a look at his FG% per feet.

<img src="/home/lucas/Documents/codes/nba/raptors-shotcharts/plots/2019-20/kylelowry_fg_per_feet.png" style="zoom: 20%;" />

<img src="/home/lucas/Documents/codes/nba/raptors-shotcharts/plots/2020-21/kylelowry_fg_per_feet.png" style="zoom: 20%;" />

Overall he had pretty similar seasons, however, he shot better this season. 

#### Pascal Siakam

Okay, let's move to Spicy P. As you already know, we start with the scatter plots.

| <img src="/home/lucas/Documents/codes/nba/raptors-shotcharts/plots/2019-20/pascalsiakam.png" style="zoom: 12.5%;" /><img src="/home/lucas/Documents/codes/nba/raptors-shotcharts/plots/2020-21/pascalsiakam.png" style="zoom: 12.5%;" /> |      |
| ------------------------------------------------------------ | ---- |

Siakam was strongly criticized throughout this season, particularly because of his missed game-winners. He, like Fred, also went through health-and-safety protocols, so we have that to keep in mind. We did not even need this plot to know this: Siakam was really inconsistent from the three-point line. Well, observing the plot this is clear. But one nice thing is that he actually shot better from the mid-range.

One nice thing from Siakam this season is that his playmaking was much better than last season. But despite that, he needs to get this three-point shot back, at least to an average. By the way, I am not going to bash Pascal because of his lost game-winners, even though I was also mad at them. Pascal had a rough time in the bubble, and being away from Toronto this season probably did not help, so I guess it is fair to wait his next season (if back in Toronto) to properly analyze everything. But, continuing with the visualizations, the next is his FG% per feet.

<img src="/home/lucas/Documents/codes/nba/raptors-shotcharts/plots/2019-20/pascalsiakam_fg_per_feet.png" style="zoom: 20%;" />

<img src="/home/lucas/Documents/codes/nba/raptors-shotcharts/plots/2020-21/pascalsiakam_fg_per_feet.png" style="zoom: 20%;" />

From this image we notice that his 2-point game near the basket seems to be pretty similar, and even had a more solid mid-range game... however, his three-point shot fell hard this season.

#### OG Anunoby

Last but not least: OG. OG had an AMAZING season (yes, I am hyped). He showed great growth, and I am not talking about lifting a 1,91m (yes, I am Brazilian so I use the metric system... but for you who do not it is 6 ft 3) grown man with a single arm, in a way we can only guess made Ibaka proud. By the way, just search "Schroder OG" if you don't know what I am talking about. Anyway, he had an amazing year and we have no reasons not to be hyped about his next season.

| <img src="/home/lucas/Documents/codes/nba/raptors-shotcharts/plots/2019-20/oganunoby.png" style="zoom: 12.5%;" /><img src="/home/lucas/Documents/codes/nba/raptors-shotcharts/plots/2020-21/oganunoby.png" style="zoom: 12.5%;" /> |      |
| ------------------------------------------------------------ | ---- |

Look at this image... he only got better. And I am only talking about his offensive game because everyone knows OG is already an awesome defender. The one thing I have to disagree with the data is that I am SURE that he did not miss any mid-range shot... because every mid-range fadeaway that I remember, he hit. But if the data is showing...

Anyway, I (and the data) have nothing bad to say about OG this season, he was truly awesome. Let's take a look at the next figure.

<img src="/home/lucas/Documents/codes/nba/raptors-shotcharts/plots/2019-20/oganunoby_fg_per_feet.png" style="zoom: 20%;" />



<img src="/home/lucas/Documents/codes/nba/raptors-shotcharts/plots/2020-21/oganunoby_fg_per_feet.png" style="zoom: 20%;" />

Again, pretty much the same shots with the addition of a mid-range. Yes, his FG (%) is a little worse, but he took a lot more shots this year than last year. That is, he had more touches offensively and pretty much kept his efficiency... this is really good by my standards.

### The tables

I also going to leave some tables for the ones that like tables, it can be useful if you want  to further analyze the graphs I showed.

| Toronto Raptors 2019-20 Shooting Splits |            |               |     FG (%) |               |             |
| :-------------------------------------- | ---------: | ------------: | ---------: | ------------: | ----------: |
|                                         | Kyle Lowry | Fred VanVleet | OG Anunoby | Pascal Siakam | Full Roster |
| Mid-Range                               |      37.66 |         31.15 |      33.33 |         31.37 |       35.77 |
| In The Paint (Non-RA)                   |       40.3 |         22.06 |      29.73 |          37.8 |       38.12 |
| Restricted Area                         |      59.07 |         51.48 |      63.29 |         64.19 |       61.11 |
| Above the Break 3                       |      36.12 |         38.39 |      37.74 |         35.48 |       37.35 |
| Left Corner 3                           |      40.74 |         42.42 |      38.71 |         33.33 |       38.75 |
| Right Corner 3                          |       12.5 |         43.33 |      41.67 |         41.46 |       37.76 |
|                                         |            |               |            |               |             |

| Toronto Raptors 2020-21 Shooting Splits |            |               |     FG (%) |               |             |
| :-------------------------------------- | ---------: | ------------: | ---------: | ------------: | ----------: |
|                                         | Kyle Lowry | Fred VanVleet | OG Anunoby | Pascal Siakam | Full Roster |
| Mid-Range                               |      38.55 |         37.27 |      39.39 |         38.58 |       38.97 |
| In The Paint (Non-RA)                   |       37.5 |         31.73 |       32.2 |         42.48 |       38.62 |
| Restricted Area                         |      63.64 |            50 |      68.26 |         62.73 |       62.48 |
| Above the Break 3                       |      38.94 |         38.33 |      38.35 |         29.57 |       36.74 |
| Left Corner 3                           |         50 |         17.86 |      42.37 |         24.14 |       37.54 |
| Right Corner 3                          |      42.86 |            32 |       40.3 |         36.67 |       38.36 |

## Conclusion

I made this project intending to get more experience with visualizations in basketball and also because I truly wanted to see if I found some insights on this chaotic season. From the visualizations, we observed some patterns that may justify part of the problems, such as the lack of a center for most of the season. Also, some players had health-and-safety protocols... and of course, being away from Toronto. And also the COVID aftermath and the "wall" that Freddy said they hit after playing a while. 

**Chaotic** is, maybe, truly the word that better defines this season. And some of the data may not show all of this, but it can show some.

## Extra

So, as I said before, I made this project to learn and also to have some fun exploring the Raptors data. I am by no means a basketball expert and my analysis may be off in some cases. Anyway, if you have any suggestions, comments, etc, etc just send me an email. Hope you liked the article(?). 



Btw, you may find some typos.