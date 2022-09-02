# surfs_up
Advanced Data Storage and Retrieval with `Jupyter Notebook`, `SQLite` and `SQLAlchemy`

## CHALLENGE OVERVIEW
---
This project explores the power of Advanced Data Storage and Retrieval to efficently produce an analyis of temperature trends in Oahu, Hawaii. Specifically, summary statistics of temperature data were requested for the months of June and December, in order to determine if a prospective surf and ice cream shop business can sustainably operate year-round as opposed to a seasonal business. 

## FEATURES AND DATA SOURCES
- Data Source: `hawaii.sqlite`
- Programming Files: `SurfsUp_Challenge.ipynb`, `climate_analysis.ipynb`
-  Data Tools: `Python SQL toolkit (SQLAlchemy)`, `Object Relational Mapper`, `pandas`, `numpy`
-  Software: SQLlite, Python 3.9.2, Flask, Jupyter Notebook

## Challenge Deliverables
Deliverable 1: Determine the Summary Statistics for June
Deliverable 2: Determine the Summary Statistics for December
Deliverable 3: A written report for the statistical analysis (README.md)

## Results
---
- _Summary Statistics DataFrame: June vs December Temperatures_

<img width="509" alt="summary_stats_df" src="https://user-images.githubusercontent.com/77628698/121727758-52fd6c80-caba-11eb-8e12-33676aa48ae8.png">

- _June Recorded Temps Visualization (Temperature and Frequency)_

<img width="503" alt="june_plot" src="https://user-images.githubusercontent.com/77628698/121729372-63aee200-cabc-11eb-81ad-075fa0e35b82.png">

- _December Recorded Temps Visualization (Temperature and Frequency)_

<img width="495" alt="dec_plot" src="https://user-images.githubusercontent.com/77628698/121729393-69a4c300-cabc-11eb-853a-667622c4c960.png">


__Key Differences in Weather: Oahu, Hawaii__
- The average recorded temperature in June is about 75 degrees F, 4 degrees higher than the average temp in December.
  - This represents a -5% change in average temperature from June to December
- The frequency of temperatures recorded in June tends to have a much more normal, tight bell curve distribution, cooroborated by the smaller std measure of June temps vs December temps
- The December temperatures seem to be more variable than those in June given its larger range in recorded temperatures (comparing the max vs min temp of each month)
   - However, when looking at the plotted distribution of Dec Temps, we can see that the median temperature in Dec is more inline with the average, and there are not many outliers skuing the average temperature higher or lower than the actual recorded frequency.
   
## Summary of Findings
I would summize that even though temperatures recorded in December seem to vary more than those of June, December would still provide appropriate weather conditions for both surfing and demand in ice cream. The average temperatures in June and December only differ by 4 degrees, and looking at the December histogram, I feel more confident in this decision--December's median temperature, with the highest frequency recorded across a span of years, is about 72 degrees, at least double the frequency of the next highest recorded temperatures, 75 and 67 respectively. It would be ill advised to not open the surf and ice cream shop based on at first clance temperature minimums.

Before making a final deicision though, I would want to perform some additional queries to get more color on weather conditions in these two months.

1. For specificity, I would like to delve into the summary statistics of temperatures recorded by station for each month. This can help determine geopgraphically where in Oahu to build the prospective shop. By comparing the variances in temperatures and the frequencies recorded, we can narrow in on an optimal location. 

- _Stations vs Temps for June and December Starting Point_

<img width="656" alt="station_temps" src="https://user-images.githubusercontent.com/77628698/121732019-af16bf80-cabf-11eb-90b5-a7918402c3b7.png">

2. Secondly, I would like to review other important variables that are correlated with optimal beach and surfing weather. Sunch varibles include precipitation, wave swells and wind condition. Though there may be some contrasting optimal conditions based on surfing vs sunbathing, it is important to identify those conditions and see how they correlate to foot traffic to the beach (depending on the time of year). It would be foolish to only value temperatures as the key indicator for opening a business. 
