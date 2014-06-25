install.packages("arules")
library(arules)

data("Groceries")
inspect (Groceries[1:10])

## Apriori Algrithum
rules0 <- apriori(data = Groceries,
                  parameter = list(support = 0.001,
                                   confidence = 0.5))
rules0

## Change params
rules1 <- apriori(data = Groceries,
                  parameter = list(support = 0.005,
                                   confidence = 0.5))
rules1

rules2 <- apriori(data = Groceries,
                  parameter = list(support = 0.005,
                                   confidence = 0.6))
rules2

rules3 <- apriori(data = Groceries,
                  parameter = list(support = 0.005,
                                   confidence = 0.64))
rules3

## change params by one
rules.sorted_sup <- sort(rules0, by = "support")


##
rules4 <- apriori(data = Groceries,
                  parameter = list(maxlen=2,supp=0.001,conf=0.1),
                  appearance = list(rhs="mustard",default="lhs"))
rules4

