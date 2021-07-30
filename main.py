import numpy as np

def calculate(list):
  if len(list)<9:
   raise ValueError("List must contain nine numbers.")
  else:
    m=np.reshape(list,(3,3))
    calculations = {'mean' : [(np.mean(m,axis=0)).tolist(),(np.mean(m,axis=1)).tolist(),(np.mean(m)).tolist()] }
    calculations ['variance'] = [(np.var(m,axis=0)).tolist(),(np.var(m,axis=1)).tolist(),(np.var(m)).tolist()]
    calculations ['standard deviation'] = [(np.std(m,axis=0)).tolist(),(np.std(m,axis=1)).tolist(),(np.std(m)).tolist()]
    calculations ['max'] = [(np.max(m,axis=0)).tolist(),(np.max(m,axis=1)).tolist(),(np.max(m)).tolist()]
    calculations ['min'] = [(np.min(m,axis=0)).tolist(),(np.min(m,axis=1)).tolist(),(np.min(m)).tolist()]
    calculations ['sum'] = [(np.sum(m,axis=0)).tolist(),(np.sum(m,axis=1)).tolist(),(np.sum(m)).tolist()]
    return calculations