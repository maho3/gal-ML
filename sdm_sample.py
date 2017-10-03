
#imports:
import sdm
import numpy as np

#tell sdm what model you want it to run, here's one example:
model = sdm.NuSDR(n_proc = 1, div_func = 'kl')

#sdm wants a list of "right answers" that it's trying to learn (the massList)
#it also wants a list of np arrays of features to learn from (the featuresList)
#let's build those two things in a loop:

featuresList = []
massList = []

#loop through all of the halos
for h in numHalos:
        
        #make a numpy array that will hold, in this case, 3 features for each of the numSubs subhalos.  Be aware that SDM requires at least 2 dimensions, so if you want to use line of sight velocity, you'll have to fill in a dummy value for the 2nd dimension.  I used an array of 1.0's
        subfeat = np.zeros((numSubs, 3), 'f')
        
        #loop through the subhalos/galaxies in this halo:
        for sh in xrange (0, numSubs):
            #and fill in each of the features
            subfeat[sh][0] = feature1
            subfeat[sh][1] = feature2
            subfeat[sh][2] = feature3

        #append the numpy array of features to the featuresList
        featuresList.append(subfeat)
        #and the mass to the massList
        massList.append(mass[h])

#turn this into a features object:
features = sdm.Features(featuresList, mass=massList)

#model.crossvalidate is the workhorse.  It will do the 10-fold crossvalidation to predict answers for all of your data.  It outputs root mean squared error (rmse) and mass predictions:
rmse, predictions = model.crossvalidate(trainData, trainData.mass)
