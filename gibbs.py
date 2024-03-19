from scipy import stats

X_given_Y1 = stats.bernoulli(3/4)
X_given_Y0 = stats.bernoulli(1/3)
Y_given_X1 = stats.bernoulli(3/5)
Y_given_X0 = stats.bernoulli(1/5)

X_given_Y = [X_given_Y0,X_given_Y1]
Y_given_X = [X_given_Y0,X_given_Y1]

X = 0
Y = 0
samples = []
for i in range(10000):
    X = X_given_Y[Y].rvs(1)[0]
    if i > 100:
        samples.append((X,Y))
    Y = Y_given_X[X].rvs(1)[0]
    if i > 100:
        samples.append((X,Y))

X1Y1_count = samples.count((1,1))
X1Y0_count = samples.count((1,0))
X0Y1_count = samples.count((0,1))
X0Y0_count = samples.count((0,0))

N = len(samples)

print("Distribution is: (1,1) = {}, (1,0) = {}, (0,1) = {}, (0,0) = {}".format(X1Y1_count/N,X1Y0_count/N,X0Y1_count/N,X0Y0_count/N))
