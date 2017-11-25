# source: https://machinelearningmastery.com/time-series-prediction-with-deep-learning-in-python-with-keras by Dr. Jason Brownlee

# Multilayer Perceptron to Predict International Airline Passengers (t+1, given t)
import numpy
import matplotlib.pyplot as plt
import pandas
import math
from keras.models import Sequential
from keras.layers import Dense

# fix random seed for reproducibility
numpy.random.seed(7)


# convert an array of values into a dataset matrix
def create_dataset(dataset, look_back=1):
    data_x, data_y = [], []
    for i in range(len(dataset) - look_back - 1):
        a = dataset[i:(i + look_back), 0]
        data_x.append(a)
        data_y.append(dataset[i + look_back, 0])
    return numpy.array(data_x), numpy.array(data_y)


def create_model(input, output, look_back=1):
    # create and fit Multilayer Perceptron model
    model = Sequential()
    model.add(Dense(8, input_dim=look_back, activation='relu'))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(input, output, epochs=200, batch_size=2, verbose=2)
    return model


def train_predict(data_set, predict, look_back=1):
    # shift train predictions for plotting
    train_predict_plot = numpy.empty_like(data_set)
    train_predict_plot[:, :] = numpy.nan
    train_predict_plot[look_back:len(predict) + look_back, :] = predict
    return train_predict_plot


def test_predict(data_set, test, train, look_back=1):
    # shift test predictions for plotting
    test_predict_plot = numpy.empty_like(data_set)
    test_predict_plot[:, :] = numpy.nan
    test_predict_plot[len(train) + (look_back * 2) + 1:len(data_set) - 1, :] = test
    return test_predict_plot


def visualization(data_set, train, test):
    # plot baseline and predictions
    plt.plot(data_set)
    plt.plot(train_predict(data_set, train))
    plt.plot(test_predict(data_set, test, train))
    plt.show()


def main():
    # load the data_set
    dataframe = pandas.read_csv('international-airline-passengers.csv', usecols=[1], engine='python', skipfooter=3)
    data_set = dataframe.values.astype('float32')

    # split into train and test sets
    train_size = int(len(data_set) * 0.67)
    test_size = len(data_set) - train_size
    train, test = data_set[0:train_size, :], data_set[train_size:len(data_set), :]
    print(len(train), len(test))

    # reshape into X=t and Y=t+1
    look_back = 1
    train_x, train_y = create_dataset(train, look_back)
    test_x, test_y = create_dataset(test, look_back)

    model = create_model(input=train_x, output=train_y)

    # Estimate model performance
    train_score = model.evaluate(train_x, train_y, verbose=0)
    print('Train Score: {score:.2f} MSE ({rms:.2f} RMSE)'.format(score=train_score, rms=math.sqrt(train_score)))
    test_score = model.evaluate(test_x, test_y, verbose=0)
    print('Test Score: {score:.2f} MSE ({rms:.2f} RMSE)'.format(score=test_score, rms=math.sqrt(test_score)))

    # generate predictions for training
    train_prediction = model.predict(train_x)
    test_prediction = model.predict(test_x)

    visualization(data_set, train=train_prediction, test=test_prediction)

    return 0


if __name__ == '__main__':
    main()
