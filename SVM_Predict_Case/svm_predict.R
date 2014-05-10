library(e1071)

#load source data
dataset <- read.csv('wdbc.data',head = FALSE)

#prepare subset: trainset and testset
index <- 1:nrow(dataset)
testindex <- sample(index, trunc(length(index)*30/100))

testset <- dataset[testindex,]
trainset <- dataset[-testindex,]

#tune the parameter for svm function
tuned <- tune.svm(V2~., data = trainset, #V2 is the type column
                    gamma = 10^(-6:-1), cost = 10^(-1:1))

#train the model
model <- svm(formula = V2~., data = trainset, kernel = "radial",
             gamma = 0.01, cost = 1)

summary(model)

#testing the model
prediction <- predict(model, testset[,-2])

#confusion matrix
tab <- table(pred = prediction, true = testset[,2])
tab
#       true
# pred   B   M
#  B    103  5
#  M     0  62

#classAgreement
classAgreement(tab)

# This means that there are 103 benign instances in test set
# and all of them were predicted as benign instances.
# On the other hand, there are 67 malign instances in test set
# , 61 were predicted rightly and 5 as benign instances.