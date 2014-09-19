---
title: "Sentiment analysis with machine learning in R"
author: "Claus Lv"
date: "Friday, September 19, 2014"
output: html_document
---

## Load library

```r
library(RTextTools)
library(e1071)
```

## Train the naive bayes model

```r
pos_tweets <- rbind(
  c('I love this car', 'positive'),
  c('This view is amazing', 'positive'),
  c('I feel great this morning', 'positive'),
  c('I am so excited about the concert', 'positive'),
  c('He is my best friend', 'positive')
)


neg_tweets <- rbind(
  c('I do not like this car', 'negative'),
  c('This view is horrible', 'negative'),
  c('I feel tired this morning', 'negative'),
  c('I am not looking forward to the concert', 'negative'),
  c('He is my enemy', 'negative')
)


test_tweets <- rbind(
  c('feel happy this morning', 'positive'),
  c('larry friend', 'positive'),
  c('not like that man', 'negative'),
  c('house not great', 'negative'),
  c('your song annoying', 'negative')
)

tweets <- rbind(pos_tweets, neg_tweets, test_tweets)
summary(tweets)
```

```
##                                        V1           V2   
##  feel happy this morning                :1   negative:8  
##  He is my best friend                   :1   positive:7  
##  He is my enemy                         :1               
##  house not great                        :1               
##  I am not looking forward to the concert:1               
##  I am so excited about the concert      :1               
##  (Other)                                :9
```

### build document-term matrix

```r
matrix <- create_matrix(tweets[,1], language="english", 
                      removeStopwords=FALSE, 
                      removeNumbers=TRUE,  # we can also removeSparseTerms
                      stemWords=FALSE) 
```

### train the naive Bayes model with the training set
Note that, `e1071` asks the response variable to be numeric or factor. Thus, we convert characters to factors here. This is a little trick.

```r
# train the model
mat <- as.matrix(matrix)
classifier <- naiveBayes(mat[1:10,], as.factor(tweets[1:10,2]) )
## test the accuracy
predicted <- predict(classifier, mat[11:15,])
predicted
```

```
## [1] positive positive negative negative positive
## Levels: negative positive
```

```r
table(tweets[11:15, 2], predicted)
```

```
##           predicted
##            negative positive
##   negative        2        1
##   positive        0        2
```

```r
recall_accuracy(tweets[11:15, 2], predicted)
```

```
## [1] 0.8
```

## Other machine learning methods
use `RTextTools` package

```r
# build the data to specify response variable, training set, testing set.
container <- create_container(matrix, as.numeric(as.factor(tweets[,2])),
                             trainSize=1:10, testSize=11:15,virgin=FALSE)
```

### train the model with multiple machine learning algorithms

```r
models <- train_models(container, algorithms=c("MAXENT" , "SVM", "RF", "BAGGING", "TREE"))
```

### Classify the test set

```r
results = classify_models(container, models)
```
### Accuracy

```r
# accuracy table
table(as.numeric(as.factor(tweets[11:15, 2])), results[,"FORESTS_LABEL"])
```

```
##    
##     1 2
##   1 3 0
##   2 1 1
```

```r
table(as.numeric(as.factor(tweets[11:15, 2])), results[,"MAXENTROPY_LABEL"])
```

```
##    
##     1 2
##   1 1 2
##   2 0 2
```

```r
# recall accuracy
recall_accuracy(as.numeric(as.factor(tweets[11:15, 2])), results[,"FORESTS_LABEL"])
```

```
## [1] 0.8
```

```r
recall_accuracy(as.numeric(as.factor(tweets[11:15, 2])), results[,"MAXENTROPY_LABEL"])
```

```
## [1] 0.6
```

```r
recall_accuracy(as.numeric(as.factor(tweets[11:15, 2])), results[,"TREE_LABEL"])
```

```
## [1] 0.6
```

```r
recall_accuracy(as.numeric(as.factor(tweets[11:15, 2])), results[,"BAGGING_LABEL"])
```

```
## [1] 0.6
```

```r
recall_accuracy(as.numeric(as.factor(tweets[11:15, 2])), results[,"SVM_LABEL"])
```

```
## [1] 0.4
```

