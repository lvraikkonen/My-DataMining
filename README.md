My-DataMining
=============

Some DataMining Case Study

## Python 实现
###协同过滤推荐
协同过滤推荐（Collaborative Filtering recommendation）是在信息过滤和信息系统中正迅速成为一项很受欢迎的技术。与传统的基于内容过滤直接分析内容进行推荐不同，协同过滤分析用户兴趣，在用户群中找到指定用户的相似（兴趣）用户，综合这些相似用户对某一信息的评价，形成系统对该指定用户对此信息的喜好程度预测。
 与传统文本过滤相比，协同过滤有下列优点:
1 能够过滤难以进行机器自动基于内容分析的信息。如艺术品、音乐；
2 能够基于一些复杂的，难以表达的概念（信息质量、品位)进行过滤；
3 推荐的新颖性。
 尽管协同过滤技术在个性化推荐系统中获得了极大的成功，但随着站点结构、内容的复杂度和用户人数的不断增加，协同过滤技术的一些缺点逐渐暴露出来。
 主要有以下三点:
1 稀疏性(sparsity)：在许多推荐系统中，每个用户涉及的信息量相当有限，在一些大的系统如亚马逊网站中，用户最多不过就评估了上百万本书的1%~2%。造成评估矩阵数据相当稀疏，难以找到相似用户集，导致推荐效果大大降低。
2 扩展性(scalability)：“最近邻居”算法的计算量随着用户和项的增加而大大增加，对于上百万之巨的数目，通常的算法将遭遇到严重的扩展性问题。
3 精确性(accuracy)：通过寻找相近用户来产生推荐集，在数量较大的情况下，推荐的可信度随之降低。

* User-Based
相似性判别方法：
- 距离方法(`Minkowski Metrics`)
- 皮尔逊相关性
- 余弦相似性 

* Item-Based
- 调整余弦相似性(`Adjust Cosine Similiarty`)
- `Slope One`算法

## R

###协同过滤推荐
基于物品的协同过滤推荐
算法： 推荐结果 = 同现矩阵 * 评分矩阵

### Classification with R

* Decision trees: rpart, party
* Random forest: randomForest, party
* SVM: e1071, kernlab
* Neural networks: nnet, neuralnet, RSNNS
* Performance evaluation: ROCR
* Naive Bayes Classifier 朴素贝叶斯分类

### Clustering with R
* k-means: kmeans(), kmeansruns()9
* k-medoids: pam(), pamk()
* Hierarchical clustering: hclust(), agnes(), diana()
* DBSCAN: fpc
* BIRCH: birch

### Association Rule Mining with R
* Association rules: apriori(), eclat() in package arules
* Sequential patterns: arulesSequence
* Visualisation of associations: arulesViz

### Text Mining with R
* Text mining: tm
* Topic modelling: topicmodels, lda
* Word cloud: wordcloud
* Twitter data access: twitteR

##
