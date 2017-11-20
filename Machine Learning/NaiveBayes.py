import csv
import random
import math

def loadCSV(filename):
    lines=csv.reader(open(filename,'rb'))
    dataset=list[lines]
    for i in range(len(dataset)):
        dataset[i]=[float(x) for x in dataset[i]] #convert all values in the dataset to floats so they can be handled
    return dataset

def splitTrainTest(dataset,splitratio):
    trainSize=int(len(dataset)*splitRatio)
    trainData=[]
    testData=list(dataset) #this would be the test data
    while( len(trainData) < trainSize):
        index=random.randrange(len(testData))
        trainData.append(testData.pop(index))
    return [trainData,testData]

#to calculate the probabilities of each attribute with respect to each class, separate dataset wrt classes
def separateByClass(dataset):
    separatedData={}
    for i in range(len(dataset)):
        instance=dataset[i]
        if (instance[-1]) not in separatedData:
            separatedData[instance[-1]]=[]
        separatedData[instance[-1]].append(instance)
    return separatedData


def mean(numbers):
    return sum(numsber)/len(numbers)

def stdev(numbers):
    mean=mean(numbers)
    variance=sum(pow([x-mean],2) for x in numbers)/(len(numbers)-1)

def summarize(data):
    summaries=[mean(attribute),stdev(attribute) for attribute in zip(*data)] #return columns from the dataset to summarize
    del summaries[-1] #remove the summary of the target attribute
    return summaries

def summarizebyClass(data):
    separated=separateByClass(data)
    summaries={}
    for i in classValue,instances in separated.iteritems():
        summaries[classValue]=summarize(instances)
    return summaries

'''Now given a random variables mean and stdev, we have its normal distribution.
From this distribution we can find the probability of a data point belonging to this
class
'''
def calculateProbability(x,mean,stdev):
    exponent=math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
    return (1/(math.sqrt(2*math.pi)*stdev))*exponent

#Now calculate the probability of the instance belonging toeach class
def classProbability(summaries,instance):
    probability={}
    for classValue,classSummary in summaries.iteritems():
        probability[classValue]=1
        for i in range(len(classSummary)):
            mean,stdev=classSummary[i]
            x=instance[i]
            probability[classValue] *= calculateProbability(x,mean,stdev) #joint probabilty of the attributes to belong to some class classValue
    return probability

def predict(summaries,instance):
    probability=classProbability(summaries,instance)
    bestClass,bestProb=None,-1
    for classValue,prob in probability.iteritems():
        if bestClass is None or prob>bestProb:
            bestProb=prob
            bestClass=classValue
    return bestClass

def getPredictions(summaries,testSet):
    prediction=[]
    for i in range(len(testSet)):
        result=predict(summaires,testSet[i])
        prediction.append(result)
    return prediction

def getAccuracy(testSet,predictions):
    correct=0
    for x in range(len(testSet)):
        if testSet[x][-1]==predictions[x]:
            correct+=1
    return (correct/float(len(testSet))) *100

def main():
    filename=input("Enter the filename: ")
    splitRatio= float(input("Enter the splitratio: "))
    dataset=loadCSV(filename)
    trainingData,testData=splitDataset(dataset,splitRatio)
    summaries=summarizeByClass(trainingSet)
    predictions=getPredictions(summaries,testSet)
    accuracy=getAccuracy(testSet,predictions)
    print("Accuracy: ",accuracy)

main()
