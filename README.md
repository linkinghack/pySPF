# pySPF
 DataMining - Home work of linking (LiuLei , TYUT - 2015005973)
 
![GitHub release](https://img.shields.io/badge/beta-0.1-blue.svg)  ![PyPI - Python Version](https://img.shields.io/badge/python-3.x-blue.svg)   ![release](https://img.shields.io/badge/build-passing-green.svg)   ![license](https://img.shields.io/badge/license-MIT-blue.svg)


Implementation of SPF algorithm in &lt;&lt;[Sampled peculiarity factor and its application in anomaly detection](http://kns.cnki.net/KCMS/detail/detail.aspx?dbcode=CJFQ&dbname=CJFD2010&filename=SDGY201005011&uid=WEEvREcwSlJHSldRa1FhcTdWajFtZkFIaHF4RFBzTWJRTGJDN1dvRXUzQT0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!&v=MjE3NDg3RGgxVDNxVHJXTTFGckNVUkxLZlllZHNGaUhtV3J2T05pbk1kN0c0SDlITXFvOUVaWVI4ZVgxTHV4WVM=)>> 

There are two example datasets in the project folder that provided by [UCI Machine Learning Repository:Data Sets](https://archive.ics.uci.edu/ml/datasets.html "UCI Machine Learning Repository:Data Sets").

# Requirements
- python 3.x
- tqdm : `pip install tqdm`

# Usage

1. edit the config file *"config.json"*  (see  **Configuration**)


2. Run the code
`python SPF.py`

# Configuration
The *config.json* can specify some unique arguments for the algorithms in JSON format which can be like this: 
```
{
    "datasource":"ism.data",
    "seprator":",",
    "features_num":7,
    "class_lables":[],
    "outlier_class_lables":[],
    "col_of_class_lable":6,
    "col_of_features":[0,6],
    "sample_set_size":1500,
    "PF_threshold":150000,
    "sample_proportion":0.3,
    "PFParam":{"alpha":0.5,"beta":1}
}
```

`datasource`  -  the dataset file to read

`seprator`  - the seprator of features of every line in the datasource

`features_num` - columns of the dataset including features and class lable

`class_lables | sample_set_size  ` - no use currently

`col_of_class_lable` - column of class lable  (**count start from 0**)

`col_of_features` - must be an array containing two **int** items , the 1st specify the start
column of features and the 2nd specify the end of features (**count start from 0**)

`PF_threshold` - the threshold of PF that is used for determine whether one record is anomalous

`sample_proportion` - proportion of sample to compute PF

`PFParam` - object, including `alpha` and `beta`, refer to the paper