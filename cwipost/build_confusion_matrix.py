import os
import json

from glob import glob

import pandas as pd
import numpy as np


def get_assessment(root: str) -> list[str]:
    return glob(f"{root}/**/assessment.geojson", recursive=True)


def build_confustion_matrix(datafile: str) -> pd.DataFrame:
    with open(datafile, 'r') as f:
        data = json.load(f)
    
    features = data['features']
    props = [_.get("properties") for _ in features]
    data = {k:v for _ in props for k,v in _.items()}
    
    cfm = pd.DataFrame(
        data=data.get('cfm'),
        columns=data.get('labels'),
        index=data.get('labels')
    )
    
    cfm = cfm.reindex(columns=cfm.columns.tolist() + ['Producers'])
    pro = list(map(lambda x: round(x * 100, 2), data.get('pro')))
    cfm["Producers"] = pro
    
    new_index = pd.Index(cfm.index.tolist() + ['Consumers'])
    cfm = cfm.reindex(new_index).fillna(value=np.nan)
    cfm.iloc[-1, 0:-1] = list(map(lambda x: (x * 100), data.get('con')))
    
    cfm = cfm.reindex(cfm.index.tolist() + ['Overall Accuracy']).fillna(value=np.nan)
    cfm.iloc[-1, 0] = round(data.get('acc') * 100, 2)
    
    return cfm
    
    