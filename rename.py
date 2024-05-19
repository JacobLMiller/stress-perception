import os 

train_dir = "all_drawings/training_drawings/"
for fname in os.listdir(train_dir):
    os.rename(train_dir + fname, train_dir + fname.replace("g1", "g6"))