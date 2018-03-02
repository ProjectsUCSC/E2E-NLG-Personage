import pandas as pd
import numpy as np
import sys

file_name = sys.argv[1]
data = pd.read_csv(file_name)

cols = list(data)

mr_cols = cols[0]
text_cols = cols[1]
voice = cols[2]
param_cols = cols[3:]

da_and_text = data[[mr_cols] + [text_cols] + [voice]]
context = data[param_cols]

da_and_text.to_csv(file_name.split('.')[0] + "_voices_trainset_mtv.csv", index=False)
#context.to_csv(file_name.split('.')[0] + "_voices_context_mtv.txt", index=False)#, sep=' ')#, header=False)
context.to_csv(file_name.split('.')[0] + "_voices_context_personality.txt", index=False, sep=' ', header=False)
