from math import sqrt

## user rate for some movies
users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0,
                      "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0,
                 "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0,
                  "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, 
                 "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0,
                    "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, 
                     "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0,
                 "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, 
                      "Slightly Stoopid": 2.5, "The Strokes": 3.0} 
}

## Test Dataset
users = {"David":{"Imagine Dragons": 3, "Daft Punk": 5, "Lorde": 4, "Fall Out Boy": 1},
         "Matt":{"Imagine Dragons": 3, "Daft Punk": 4, "Lorde": 4, "Fall Out Boy": 1},
         "Ben":{"Kacey Musgraves": 4, "Imagine Dragons": 3, "Lorde": 3, "Fall Out Boy": 1},
         "Chris":{"Kacey Musgraves": 4, "Imagine Dragons": 4, "Daft Punk": 4,
                  "Lorde": 3, "Fall Out Boy": 1},
         "Torri":{"Kacey Musgraves": 5, "Imagine Dragons": 4, "Daft Punk": 5, "Fall Out Boy": 3}
}

users2 = {"Amy": {"Taylor Swift": 4, "PSY": 3, "Whitney Houston": 4},
          "Ben": {"Taylor Swift": 5, "PSY": 2},
          "Clara": {"PSY": 3.5, "Whitney Houston": 4},
          "Daisy": {"Taylor Swift": 5, "Whitney Houston": 3}}


### Cosine Similiarty
#def computeSimiliarty(band1, band2, data):
#    averages = {}
#    for (key, ratings) in data.items():
#        averages[key] = float(sum(ratings.values())) / len(ratings.values())
#    #print "averages is: ", averages

#    num = 0
#    dem1 = 0
#    dem2 = 0
#    for (key, ratings) in data.items():
#        if band1 in ratings and band2 in ratings:
#            avg = averages[key]
#            num += (ratings[band1] - avg) * (ratings[band2] - avg)
#            dem1 += (ratings[band1] - avg) ** 2
#            dem2 += (ratings[band2] - avg) ** 2
#    return num / (sqrt(dem1) * sqrt(dem2))

#print computeSimiliarty("Kacey Musgraves","Lorde", users)
#print computeSimiliarty("Imagine Dragons","Lorde", users)
#print computeSimiliarty("Daft Punk","Lorde", users)


## Weighted Slope One Algroithm
## 1. Compute deviations
def computeDevation(data):
    count = {}
    dev = {}

    ## each user ratings
    for ratings in data.values(): # each user ratings
        for (item, rating) in ratings.items(): # baseline rating (to be compared)
            #count = 0
            #dev = 0
            count.setdefault(item, {})
            dev.setdefault(item, {})
            for (item2, rating2) in ratings.items(): # compare

                if item2 != item: ## different band
                    count[item].setdefault(item2,0)
                    dev[item].setdefault(item2, 0.0)
                    count[item][item2] += 1
                    dev[item][item2] += rating - rating2
                else: #same band
                    count[item][item2] = 0
                    dev[item][item2] = 0.0

    for (item, ratings) in dev.items():
        for item2 in ratings:
            if count[item][item2] != 0:
                ratings[item2] /= count[item][item2]
            else:
                ratings[item2] = 0
    #print "count: ",count
    #print "dev is: ",dev
    return dev,count
    
## print computeDevation(users2)

## 2. Predict
def slopeOneRecommendations(data, deviations, count, user, band):
    if data[user].get(band) <> None:
        return data[user][band]
    itemPrediction = 0
    totalFrequency = 0
    for key in data[user]:
        if key != band:
            itemPrediction += (data[user][key] + deviations[band][key]) * count[band][key]
            totalFrequency += count[band][key]
        itemPrediction /= totalFrequency
    return itemPrediction  

d,c = computeDevation(users2)
print "Devation: ",d
print "Count: ",c
predict_HOU_Ben = slopeOneRecommendations(users2, d,c , "Ben", "Whitney Houston")
print predict_HOU_Ben 