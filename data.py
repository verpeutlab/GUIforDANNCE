#basic way to import data in python (i use a mac so it may be slightly different for your device)
import scipy.io
#change pathway for your own device 
mat=scipy.io.loadmat('/Users/ishaan/Downloads/save_data_AVG0.mat')
mat['pred']
