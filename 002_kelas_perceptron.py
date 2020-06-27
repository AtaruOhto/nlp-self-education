import numpy as np
from keras.layers import Dense
from keras.models import Sequential

model = Sequential()

model.add(Dense(units=2, activation="relu", input_dim=3))
model.add(Dense(units=1, activation="sigmoid"))
model.compile(loss="binary_crossentropy", optimizer="adam"),

X = np.array([
    [-0.1, -0.2, -0.3],
    [0.3, 0.4, 0.5],
])

y = np.array([0, 1])

model.fit(X, y, batch_size=32, epochs=50)
