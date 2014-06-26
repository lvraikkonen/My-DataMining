利用apriori算法进行关联分析
==========================


## 载入相关R扩展包
`arules`

```r
library(arules)
library(rattle)## data
```

## Sample Data
ID: 购物篮编号
Item: 物品

```r
#从rattle包中读入数据
dvdtrans <- read.csv(system.file("csv", "dvdtrans.csv",package="rattle"))
head(dvdtrans)
```

```
##   ID          Item
## 1  1   Sixth Sense
## 2  1         LOTR1
## 3  1 Harry Potter1
## 4  1    Green Mile
## 5  1         LOTR2
## 6  2     Gladiator
```

## 利用`Apriori`算法进行关联分析

```r
#将数据转化为合适的格式
data <- as(split(dvdtrans$Item, dvdtrans$ID),"transactions")

#用 apriori命令生成频繁项集，设其支持度为0.5，置信度为0.8
rules <- apriori(data, parameter=list(support=0.5,confidence=0.8))
```

```
## 
## parameter specification:
##  confidence minval smax arem  aval originalSupport support minlen maxlen
##         0.8    0.1    1 none FALSE            TRUE     0.5      1     10
##  target   ext
##   rules FALSE
## 
## algorithmic control:
##  filter tree heap memopt load sort verbose
##     0.1 TRUE TRUE  FALSE TRUE    2    TRUE
## 
## apriori - find association rules with the apriori algorithm
## version 4.21 (2004.05.09)        (c) 1996-2004   Christian Borgelt
## set item appearances ...[0 item(s)] done [0.00s].
## set transactions ...[10 item(s), 10 transaction(s)] done [0.00s].
## sorting and recoding items ... [3 item(s)] done [0.00s].
## creating transaction tree ... done [0.00s].
## checking subsets of size 1 2 done [0.00s].
## writing ... [3 rule(s)] done [0.00s].
## creating S4 object  ... done [0.00s].
```

```r
#用inspect命令提取规则
inspect(rules)
```

```
##   lhs              rhs         support confidence  lift
## 1 {Patriot}     => {Gladiator}     0.6     1.0000 1.429
## 2 {Gladiator}   => {Patriot}       0.6     0.8571 1.429
## 3 {Sixth Sense} => {Gladiator}     0.5     0.8333 1.190
```

## 结论
这说明购买爱国者电影(`Patriot`)的顾客同时也会购买角斗士(`Gladiator`)
