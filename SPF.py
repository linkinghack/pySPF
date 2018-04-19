# Author: linking
# Department: College of Software Engineering,TaiYuan University of Technology  (TYUT)
# github: github.com/linkinghack
# web: linkinghack.com
# Description: This program implements the SPF algorithm in <<Sampled peculiarity factor and its application in anomaly detection>>

from ConfigReader import Configure
import logging
import logging.handlers
import pickle
import time
from tqdm import tqdm


# setup logging
handler = logging.handlers.RotatingFileHandler('SPF.log',maxBytes=2*1024*1024,backupCount=5) 
fmt = '%(levelname)s - %(asctime)s - %(filename)s:%(lineno)s -  %(message)s' 
formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


# read config
OPTION = Configure.readConfig("config.json")


# Define the model of a record
class Record(object):
    def __init__(self,features,lable):
        self.features = features
        self.lable = lable
        self.PF = 0
    def toString(self):
        return "features: "+str(self.features) + " lable: " + str(self.lable) + " PF: " + str(self.PF)


# Construct the data matrix
matrix = list()
datafile = open(OPTION['datasource'])
for line in datafile:
    line = line.split(OPTION['seprator'])
    data_row = [float(i) for i in line] #switch from string to float number
    matrix.append(Record(data_row[OPTION['col_of_features'][0]:OPTION['col_of_features'][1]+1],
     int(data_row[OPTION['col_of_class_lable']]) ) )

datafile.close()

# select samples
recordsNum = len(matrix)
proportion = OPTION['sample_proportion']
interval = int(recordsNum / (proportion*recordsNum))

sample = list()
for i in range(0,recordsNum,interval):
    # sample.append(matrix[i])
    sample.append(i)
print("sample size: ",len(sample))

# learning threshold of PF
LearnedPFThresHold = None
    # unimplemented


# PF algorithms
ALPHA = OPTION['PFParam']['alpha']
BETA = OPTION['PFParam']['beta']
THRESHOLD = (LearnedPFThresHold if LearnedPFThresHold else (OPTION['PF_threshold']) ) #PF threshold
# THRESHOLD = OPTION['PF_threshold']
outliers = list()
logger.info('-------------------------')
logger.info('Start find outliers with  PF threshold : '+str(THRESHOLD))

t0 = time.clock()  #count compute time

def PF(recordMatrix,sampleIndexs,outliers):
    # PF of record
    countOutlier = 0
    
    for record in tqdm(recordMatrix,desc='Progress',leave=False,mininterval=2,maxinterval=4,miniters=0):
        recordPF = 0
        for i in sampleIndexs:
            featurePF = 0
            featureIndex = 0
            # PF of feature
            for feature in record.features:
                featurePF += (abs((feature - recordMatrix[i].features[featureIndex])) ** ALPHA)
                # print("feature PF : ",featurePF)
                featureIndex += 1
            recordPF += BETA * featurePF
        record.PF = recordPF
        if recordPF > THRESHOLD:
        # if(recordPF > (OPTION['PF_threshold'])):
            countOutlier += 1
            outliers.append(record)
            logger.info('Outlier Found:'+record.toString())
            # print("outlier found: ",record.toString()," PF: ",recordPF)
        else:
            logger.info('Not an outlier:'+record.toString())
            # print('not an outlier',record.toString()," PF: ",recordPF)


PF(matrix,sample,outliers)
t1 = time.clock()
print('Done!  compute time: ',int(t1 - t0), 's')
logger.info('compute time: '+str(t1-t0))
logger.info('-------------------------')
print("size of outliers: ",len(outliers))

# save sorted outliers
outliers.sort(key=lambda record: record.PF)
outliersFile = open('outliers.txt','w')
for rec in outliers:
    outliersFile.write(rec.toString())
    outliersFile.write('\n')
outliersFile.close()

# save sorted matrix
matrix.sort(key=lambda record: record.PF)
matrixFile = open('matrix.txt','w')
for rec in matrix:
    matrixFile.write(rec.toString())
    matrixFile.write('\n')
matrixFile.close()

# serialize the matrix and save to file
matrixBinFile = open('Matrix.BIN','wb')
pickle.dump(matrix,matrixBinFile)
matrixBinFile.close()