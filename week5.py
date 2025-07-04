# Data Wrangling
"""Introduction to R/RStudio/tidyverse
Working with tidy data, dplyr pipes, groups, summaries, joins, scraping and cleaning
Exploratory data analysis (scatterplots, correlation), categorical data analysis, various graphical plots using ggplot
"""
"""
library(tidyverse) 
mpg
nrow(mpg)
colnames(mpg)

view(mpg)

ggplot(mpg,aes(x=displ, y=hwy, colour=trans)) +
  geom_point() +
  ggtitle("fuel efficiency vs number of cylinders")

url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/unisex-names/unisex_names_table.csv"
kids = read_csv(url)
kids

arrange(kids, male_share)
arrange(kids, desc(total))

filter(kids,name=='Kendall')

filter(kids,total>=100000) 
"""