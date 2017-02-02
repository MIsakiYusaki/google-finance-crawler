# ------------------------- initail settings
setwd("C:\\Users\\ohyee\\Documents\\GitHub\\Python\\crawler\\twse")
getwd()
twse <- read.csv("prices.csv")
colnames(twse) <- c("ID", "Date", "Price", "Change", "Volumn")
head(twse)
tail(twse)
str(twse)
summary(twse)
library(ggplot2)

p <- ggplot(data=twse, aes(x=-ID, y=Price))
p + geom_point(aes(color=Volumn))

