 source: https://machinelearningmastery.com/time-series-prediction-with-deep-learning-in-python-with-keras by Dr. Jason Brownlee 

# Multilayer Perceptron to Predict International Airline Passengers (t+1, given t)
import numpy
import matplotlib.pyplot as plt
import pandas
import math
from keras.models import Sequential
from keras.layers import Dense

# fix random seed for reproducibility
numpy.random.seed(7)

# load the dataset
dataframe = pandas.read_csv('international-airline-passengers.csv', usecols=[1], engine='python', skipfooter=3)
dataset = dataframe.values
dataset = dataset.astype('float32')

# split into train and test sets
train_size = int(len(dataset) * 0.67)
test_size = len(dataset) - train_size
train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]
print(len(train), len(test))

# convert an array of values into a dataset matrix
def create_dataset(dataset, look_back=1):
	dataX, dataY = [], []
	for i in range(len(dataset)-look_back-1):
		a = dataset[i:(i+look_back), 0]
		dataX.append(a)
		dataY.append(dataset[i + look_back, 0])
	return numpy.array(dataX), numpy.array(dataY)

def create_model(input, output):
	# create and fit Multilayer Perceptron model
	model = Sequential()
	model.add(Dense(8, input_dim=look_back, activation='relu'))
	model.add(Dense(1))
	model.compile(loss='mean_squared_error', optimizer='adam')
	model.fit(input, output, epochs=200, batch_size=2, verbose=2)
	return(model)

def train_predict(dataset,trainPredict):
	# shift train predictions for plotting
	trainPredictPlot = numpy.empty_like(dataset)
	trainPredictPlot[:, :] = numpy.nan
	trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
	return(trainPredictPlot)

def test_predict(dataset,testPredict):
	# shift test predictions for plotting
	testPredictPlot = numpy.empty_like(dataset)
	testPredictPlot[:, :] = numpy.nan
	testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict
	return(testPredictPlot)

def visualization(dataset,trainPredict,testPredict):
	# plot baseline and predictions
	plt.plot(dataset)
	plt.plot(train_predict(dataset, trainPredict))
	plt.plot(test_predict(dataset, testPredict))
	plt.show()

def main():	
	# reshape into X=t and Y=t+1
	look_back = 1
	trainX, trainY = create_dataset(train, look_back)
	testX, testY = create_dataset(test, look_back)

	# Estimate model performance
	trainScore = model.evaluate(trainX, trainY, verbose=0)
	print('Train Score: %.2f MSE (%.2f RMSE)' % (trainScore, math.sqrt(trainScore)))
	testScore = model.evaluate(testX, testY, verbose=0)
	print('Test Score: %.2f MSE (%.2f RMSE)' % (testScore, math.sqrt(testScore)))
	
	# generate predictions for training
	trainPredict = model.predict(trainX)
	testPredict = model.predict(testX)
	
	visualization(dataset,testPredict,testPredict)

	return 0

if __name__ == '__main__':
	main()

