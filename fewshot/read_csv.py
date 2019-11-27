import numpy as np
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--file', required=True)

args = parser.parse_args()

loss = []
accuracy = []
stnloss = []
stnaccuracy = []

with open(args.file, 'r') as f:
    lines = f.read().split('\n')
    lines = [line for line in lines if line!=""]
    for i, line in enumerate(lines):
        if i>0:
            accuracy.append(float(line.split(',')[-1].strip()))
            loss.append(float(line.split(',')[-2].strip()))
epochs = np.arange(len(loss))
accuracy = np.array(accuracy)
loss = np.array(loss)

args.file = args.file.replace('.csv', '_stn.csv')
with open(args.file, 'r') as f:
    lines = f.read().split('\n')
    lines = [line for line in lines if line!=""]
    for i, line in enumerate(lines):
        if i>0:
            stnaccuracy.append(float(line.split(',')[-1].strip()))
            stnloss.append(float(line.split(',')[-2].strip()))

print(loss)
stnloss = np.array(stnloss)
print(stnloss)
stnaccuracy = np.array(stnaccuracy)
stnepochs = np.arange(len(stnloss))

plt.figure()
#fig, ax = plt.subplots(1, 2, sharey=True)
#ax[0].plot(epochs, loss, label="loss")
#ax[1].plot(epochs, accuracy, label="Accuracy")
#ax[0].plot(stnepochs, stnloss, label="stnloss")
#ax[1].plot(stnepochs, stnaccuracy, label="stnAccuracy")
#ax[0].legend()
#ax[1].legend()
plt.plot(loss)
plt.plot(stnloss)

#plt.show()
plt.savefig('loss.png')