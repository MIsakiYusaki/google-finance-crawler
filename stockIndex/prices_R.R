# --------------------------------------------- lib install, import
library("readxl")
library("ggplot2")
# --------------------------------------------- data import
getwd()
setwd("C:\\Users\\weijc\\Github\\Crawler\\stockIndex")
price <- read_excel("prices.xlsx", sheet = "price_2003_delete")
price_test <- read_excel("prices.xlsx", sheet = "price_2015")
# --------------------------------------------- price_test (2015~201601)
# total 242 trade days in 2015
price_test2015firsthalf <- tail(price_test, 121)
firsthalf2015mean <- mean(price_test2015uphalf$changePercent)
firsthalf2015std <- sd(price_test2015uphalf$changePercent)
# --------------------------------------------- all data (2013~2017)
allPercMean <- mean(price$changePercent)
allPercSd <- sd(price$changePercent)
max(price$changePercent)
?geom_histogram
ggplot(data = price, aes(price$changePercent * 100))+
  geom_histogram(bins = 100,
                 col = "black",
                 fill = "skyblue",
                 alpha = 0.8)+
  labs(title = "Histogram for price change (all data)")+
  labs(x = "price change %", y = "Count")
# --------------------------------------------- last year data
price365 <- tail(price, 365)
head(price365)
tail(price365)
lastyearPercMean <- mean(price365$changePercent)
lastyearPercSd <- sd(price365$changePercent)

ggplot(data = price365, aes(price365$changePercent * 100))+
  geom_histogram(bins = 60,
                 col = "black",
                 fill = "skyblue",
                 alpha = 0.8)+
  labs(title = "Histogram for price change (last year data)")+
  labs(x = "price change %", y = "Count")
# --------------------------------------------- last month data
price30 <- tail(price, 30)
head(price30)
tail(price30)
lastmonthPercMean <- mean(price30$changePercent)
lastmonthPercSd <- sd(price30$changePercent)

ggplot(data = price30, aes(price30$changePercent * 100))+
  geom_histogram(bin = 5,
                 col = "black",
                 fill = "skyblue",
                 alpha = 0.8)+
  labs(title = "Histogram for price change (last year data)")+
  labs(x = "price change %", y = "Count")
# --------------------------------------------- data stats

changePercMean <- mean(price$changePercent)
changePercSd <- sd(price$changePercent)
