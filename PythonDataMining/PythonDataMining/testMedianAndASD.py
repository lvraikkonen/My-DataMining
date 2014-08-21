data = [('Gymnastics', [54, 66], ['Asuka Teramoto']),
        ('Basketball', [72, 162], ['Brittainey Raven']),
        ('Basketball', [78, 204], ['Chen Nan']),
        ('Gymnastics', [49, 90], ['Gabby Douglas'])]

medianAndDeviation = []

def getMedian(alist):
    """Get the Median of a list"""
    if alist == []:
        return []
    n = len(alist)
    alist_sorted = sorted(alist)
    if n % 2 == 0: # avg between middle 2
        v1 = alist_sorted[int(n/2) - 1]
        v2 = alist_sorted[int(n/2)]
        return float(v1 + v2) / 2
    else:
        return alist[n/2]

def getAbsoluteStandardDeviation(alist, median = 0):
    """Get the Absolute Standard Deviation of a list"""
    median = getMedian(alist)
    sum = 0
    for item in alist:
        sum += abs(item - median)
    return sum / len(alist)

def normalizeColumn(columnNumber): #normalize the train data
    """given a column number, normalize that column in data"""
    col = [v[1][columnNumber] for v in data]
    median = getMedian(col)
    asd = getAbsoluteStandardDeviation(col, median)

    # print median, asd
    
    # store median and asd
    medianAndDeviation.append((median,asd))

    for v in data:
        v[1][columnNumber] = (v[1][columnNumber] - median) / asd
    return data

vlen = len(data[0][1]) ## number attributes
for i in range(vlen):
    normalizeColumn(i)

##print medianAndDeviation
##print data

def normalizeVector(v): # Calc the Modified Standard Score
    vector = list(v)
    for i in range(len(vector)):
        (median, asd) = medianAndDeviation[i]
        vector[i] = (vector[i] - median) / asd
    return vector

##print normalizeVector([70,170])

def manhattan(vector1, vector2):
    """Computes the Manhattan distance."""
    distance = 0
    for key in vector1:
        if key in vector2:
            distance += abs(vector1[key] - vector2[key])
    return distance

def nearestNeighbor(itemVector):
    """return nearest neighbor to itemVector
        sample iteVector like [70,170]"""
    #return min([ (manhattan(itemVector, item[1]), item) for item in data]) 
    distances = []
    for item in data:
        distance = manhattan(itemVector, item[1])
        distances.append((distance,item))
    distances.sort()
    return min(distances)

#print nearestNeighbor([70,170])
    
def classify(itemVector):
    """Return class we think item Vector is in"""
    return(nearestNeighbor(normalizeVector(itemVector))[1][0]) # return the classifier result

print classify([70,170])