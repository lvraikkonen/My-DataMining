class Classifier(object):
    """My first classifier using data attributes"""
    def __init__(self, filename):
        
        self.medianAndDeviation = []
        self.data = []

        # Read data from file
        f = open(filename)
        lines = f.readlines()
        f.close()

        self.format = lines[0].strip().split('\t')
        for line in lines[1:]:
            fields = line.strip().split('\t')
            ignore = []
            vector = []
            for i in range(len(fields)):
                if self.format[i] == 'num':
                    vector.append(int(fields[i]))
                elif self.format[i] == 'comment':
                    ignore.append(fields[i])
                elif self.format[i] == 'class':
                    classification = fields[i]
            self.data.append((classification, vector, ignore))
        
        #print "Raw data: ",self.data

        # get length of instance vector
        ### data format as below:
        ### [('Gymnastics', [54, 66], ['Asuka Termoto']),
        ###  ('Basketball', [72, 162], ['Brittainey Raven'],...
        self.vlen = len(self.data[0][1]) # [0][1] for num attributes
        # now normalize the data
        for i in range(self.vlen):
            self.normalizeColumn(i)

        #print "Median and ASD are: ",self.medianAndDeviation
        #print "NData: ",self.data
    

    ##################################################
    ###
    ###  CODE TO COMPUTE THE MODIFIED STANDARD SCORE
    def getMedian(self, alist):
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

    def getAbsoluteStandardDeviation(self, alist, median = 0):
        """Get the Absolute Standard Deviation of a list"""
        median = self.getMedian(alist)
        sum = 0
        for item in alist:
            sum += abs(item - median)
        return sum / len(alist)

    def normalizeColumn(self, columnNumber):
        """given a column number, normalize that column in data"""
        
        col = [v[1][columnNumber] for v in self.data]
        #print col
        median = self.getMedian(col)
        asd = self.getAbsoluteStandardDeviation(col, median)

        #print median, asd
    
        # store median and asd
        self.medianAndDeviation.append((median,asd))

        for v in self.data:
            v[1][columnNumber] = (v[1][columnNumber] - median) / asd
        return self.data

    def nornalizeVectorForTestset(self, v):
        """We have stored the median and asd for each column.
        We now use them to normalize vector v"""
        vector = list(v)
        for i in range(len(vector)):
            (median, asd) = self.medianAndDeviation[i]
            vector[i] = (vector[i] - median) / asd
        return vector

    ###
    ### END NORMALIZATION
    ##################################################


    def manhattan(self, vector1, vector2):
        """Computes the Manhattan distance."""
        distance = 0
        for i in range(len(vector1)):
            distance += abs(vector1[i] - vector2[i])
        return distance

    def nearestNeighbor(self, itemVector):
        """return nearest neighbor to itemVector
            sample iteVector like [70,170]"""
        return min([ (self.manhattan(itemVector, item[1]), item) for item in self.data]) 
    
    def classify(self, itemVector):
        """Return class we think item Vector is in"""
        return self.nearestNeighbor(self.nornalizeVectorForTestset(itemVector))[1][0]


def unitTest():
    classifier = Classifier('athletesTrainingSet.txt')



#unitTest()
def test(training_filename, test_filename):
    """Test the classifier on a test set of data"""
    classifier = Classifier(training_filename)
    f = open(test_filename)
    lines = f.readlines()
    f.close()
    numCorrect = 0.0
    for line in lines:
        data = line.strip().split('\t')
        vector = []
        classInColumn = -1
        for i in range(len(classifier.format)):
              if classifier.format[i] == 'num':
                  vector.append(float(data[i]))
              elif classifier.format[i] == 'class':
                  classInColumn = i
        theClass= classifier.classify(vector)
        #print "Guess class is :",theClass
        prefix = '-'
        if theClass == data[classInColumn]:
            # it is correct
            numCorrect += 1
            prefix = '+'
        print("%s  %12s  %s" % (prefix, theClass, line))
    print("%4.2f%% correct" % (numCorrect * 100/ len(lines)))


test('athletesTrainingSet.txt', 'athletesTestSet.txt')