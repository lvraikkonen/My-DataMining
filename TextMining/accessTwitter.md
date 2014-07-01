连接Twitter账户简单分析Tweet
========================================================

## 相关包


```r
###install the necessary packages
## install.packages("ROAuth")
## install.packages("twitteR")
## install.packages("wordcloud")
## install.packages("tm")
 
library("ROAuth")
library("twitteR")
library("wordcloud")
library("tm")
```

## Connect via OAuth
ON windows, we need to dowload the certificate for OAUTH

```r
#Download SSL certification
download.file(url="http://curl.haxx.se/ca/cacert.pem", destfile="cacert.pem")

# Set SSL certs globally
options(RCurlOptions = list(cainfo = system.file("CurlSSL", "cacert.pem", package = "RCurl")))

#Set constant request URL
requestURL<-"https://api.twitter.com/oauth/request_token"
#Set constant accessURL
accessURL<-"https://api.twitter.com/oauth/access_token"
#set constant authURL
authURL<-"https://api.twitter.com/oauth/authorize"
consumerKey<-"an3hwBQXNU7xwZmz3ISTHHryI"
consumerSecret<-"I5pMQT5Hlh7G3zHhIBmmTC2f0AKCrJKBem69eTygwpfRu9hNBj"

twitCred <- OAuthFactory$new(consumerKey=consumerKey,
                             consumerSecret=consumerSecret,
                             requestURL=requestURL,
                             accessURL=accessURL,
                             authURL=authURL)


#asking for access
twitCred
```

```
## Reference class object of class "OAuth"
## Field "consumerKey":
## [1] "an3hwBQXNU7xwZmz3ISTHHryI"
## Field "consumerSecret":
## [1] "I5pMQT5Hlh7G3zHhIBmmTC2f0AKCrJKBem69eTygwpfRu9hNBj"
## Field "oauthKey":
## character(0)
## Field "oauthSecret":
## character(0)
## Field "needsVerifier":
## [1] TRUE
## Field "handshakeComplete":
## [1] FALSE
## Field "verifier":
## character(0)
## Field "requestURL":
## [1] "https://api.twitter.com/oauth/request_token"
## Field "authURL":
## [1] "https://api.twitter.com/oauth/authorize"
## Field "accessURL":
## [1] "https://api.twitter.com/oauth/access_token"
## Field "signMethod":
## character(0)
```

```r
twitCred$handshake(cainfo = system.file("CurlSSL", "cacert.pem",package = "RCurl"))

## To check and see if the handshake worked 
registerTwitterOAuth(twitCred)
```

```
## [1] TRUE
```

```r
##  save the handshake
save(list="twitCred", file="twitteR_credentials")
```


Get content and make word cloud

```r
worldCup <- searchTwitter("#WorldCup2014", n=100, cainfo="cacert.pem")
```

```
## Warning: 100 tweets were requested but the API can only return 99
```

```r
worldCup_text <- sapply(worldCup, function(x) x$getText())
worldCup_corpus<-Corpus(VectorSource(worldCup_text))
worldCup_corpus<-tm_map(worldCup_corpus, tolower, mc.cores=1)
worldCup_corpus<-tm_map(worldCup_corpus, removePunctuation, mc.cores=1)
worldCup_corpus<-tm_map(worldCup_corpus, function(x) removeWords(x,stopwords()))
wordcloud(worldCup_corpus)
```

```
## Warning: font width unknown for character 0x90
## Warning: font width unknown for character 0x90
## Warning: font metrics unknown for character 0x90
## Warning: font width unknown for character 0x8f
## Warning: font width unknown for character 0x8f
## Warning: font metrics unknown for character 0x8f
## Warning: font width unknown for character 0x9d
## Warning: font width unknown for character 0x9d
## Warning: font metrics unknown for character 0x9d
```

![plot of chunk unnamed-chunk-2](figure/unnamed-chunk-2.png) 

