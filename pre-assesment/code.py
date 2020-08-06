#import tensorflow as tf;
#from tensorflow import keras;
#from tensorflow.keras.preprocessing.text import Tokenizer;

import pandas as pd;
import numpy as np;
import matplotlib as mp;
import json;
import os;
import argparse;
from pandas.io.json import json_normalize;

with open ('data.json') as f:
    d = load.json(f)


dataframe = json_normalize(d['covid19_map'])
dataframe.head()