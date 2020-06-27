import numpy as np
from keras.layers import Dense
from keras.models import Sequential

model = Sequential()
model.add(Dense(32, input_dim=100, activation="relu"))
model.add(Dense(10, activation="softmax"))
model.compile(loss="categorical_crossentropy", optimizer="adam")

X = np.random.uniform(low=0.1, high=1, size=(8, 100))
y = np.random.random_integers(low=0, high=1, size=(8, 10))

model.fit(X, y, epochs=100)
