# --------------------------------------------- lib install, import
install.packages("readxl")
library("readxl")
# --------------------------------------------- data import
getwd()
setwd("C://Users//weijc//Github//Crawler//stockIndex")
price <- read_excel("prices.xlsx", sheet = "price_2003_delete")
str(price)
summary(price)
head(price)
tail(price)
# --------------------------------------------- data stats
volumnM <- mean(price$volumn)
volumnV <- sd(price$volumn)
changeM <- mean(price$change)
changeV <- sd(price$change)
changePercM <- mean(price$changePercent)
changePercV <- sd(price$changePercent)
