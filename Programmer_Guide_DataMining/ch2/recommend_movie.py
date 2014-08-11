from math import sqrt

## user rate for some movies
users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0} 
}

## manhattan distance
def manhattan(rating1,rating2):
    distance = 0
    for rate in rating1:
        ##same rate
        if rate in rating2:
            distance += abs(rating1[rate] - rating2[rate])
    return distance

## Minkowski Distance Function
def minkowski(rating1, rating2, r):
    distance = 0
    commonRating = False
    for key in rating1:
        if key in rating2:
            distance += pow(abs(rating1[key] - rating2[key]), r)
            commonRating = True
    if commonRating:
        return pow(distance, float(1)/r)
    else:
        return 0 # no ratings in common

#### expect value is 7.5
##print manhattan(users["Hailey"],users["Jordyn"])
##print minkowski(users["Hailey"],users["Jordyn"],2)


## Pearson Algorithm

##Pearson Correlation Coefficient
def pearson(rating1,rating2):
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0
    n = 0
    for key in rating1:
        if key in rating2:
            n += 1
            x = rating1[key]
            y = rating2[key]
            sum_xy += x * y
            sum_x += x
            sum_y += y
            sum_x2 += x**2
            sum_y2 += y**2
    # now compute denominator
    denominator = sqrt(sum_x2 - (sum_x**2) / n) * sqrt(sum_y2 -(sum_y**2) / n)
    if denominator == 0:
        return 0
    else:
        return (sum_xy - (sum_x * sum_y) / n) / denominator

##print pearson(users["Angelica"],users["Jordyn"])


## find cloest person, return sorted tuple
def computeNearestNaighbor(username,users):
    distances = []
    for user in users:
        ## other people, calc distance
        if user != username:
            ##distance = manhattan(users[user], users[username])
            ## r=2 Euler Distance
            distance = minkowski(users[user], users[username], 2)
            distances.append((distance, user))
    distances.sort()
    return distances

##Expect Value
##[(2.0, ''Veronica'), (4.0, 'Chan'),(4.0, 'Sam'), (4.5, 'Dan'), (5.0,
##'Angelica'), (5.5, 'Bill'), (7.5, 'Jordyn')]
##nearest_Hailey = computeNearestNaighbor("Hailey", users)
##print nearest_Hailey

##nearest_Hailey[0][1]
##'Veronica'

## recommand function
def recommand(username, users):
    ## nearest person
    nearest = computeNearestNaighbor(username, users)[0][1]

    recommandations = []
    ## find bands neighbor rated that user didn't
    neighborRating = users[nearest]
    userRating = users[username]
    for artist in neighborRating:
        if artist not in userRating:
            recommandations.append((artist, neighborRating[artist]))
    ## return recommand sorted by rating desc
    return sorted(recommandations,
                  key = lambda x: x[1],
                  reverse = True)

##print recommand("Hailey",users)
