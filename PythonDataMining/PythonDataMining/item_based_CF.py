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

## To Do
## Test Dataset
users = {"David":{"Imagine Dragons": 3, "Daft Punk": 5, "Lorde": 4, "Fall Out Boy": 1},
         "Matt":{"Imagine Dragons": 3, "Daft Punk": 4, "Lorde": 4, "Fall Out Boy": 1},
         "Ben":{"Kacey Musgraves": 4, "Imagine Dragons": 3, "Lorde": 3, "Fall Out Boy": 1},
         "Chris":{"Kacey Musgraves": 4, "Imagine Dragons": 4, "Daft Punk": 4,
                  "Lorde": 3, "Fall Out Boy": 1},
         "Torri":{"Kacey Musgraves": 5, "Imagine Dragons": 4, "Daft Punk": 5, "Fall Out Boy": 3}
}

## Cosine Similiarty
def computeSimiliarty(band1, band2, data):
    averages = {}
    for (key, ratings) in data.items():
        averages[key] = float(sum(ratings.values())) / len(ratings.values())

    num = 0
    dem1 = 0
    dem2 = 0
    for (key, ratings) in data.items():
        if band1 in ratings and band2 in ratings:
            avg = averages[key]
            num += (ratings[band1] - avg) * (ratings[band2] - avg)
            dem1 += (ratings[band1] - avg) ** 2
            dem2 += (ratings[band2] - avg) ** 2
    return num / (sqrt(dem1) * sqrt(dem2))

print computeSimiliarty("Kacey Musgraves","Fall Out Boy", users)
