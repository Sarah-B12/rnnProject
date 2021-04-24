from rnn import*


def main():
    X, Y = create_data(data_dir, known_Y)

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, shuffle=True, random_state=0)

    model = Sequential()
    model.add(ConvLSTM2D(filters=64, kernel_size=(3, 3), return_sequences=False, data_format="channels_last",
                         input_shape=(int(seq_len / 2), img_height, img_width, 3)))
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(512, activation="relu"))
    model.add(Dropout(0.3))
    model.add(Dense(512, activation="relu"))
    model.add(Dropout(0.3))
    model.add(Dense(2, activation="sigmoid"))

    model.summary()

    opt = keras.optimizers.SGD(lr=0.001)
    model.compile(loss='binary_crossentropy', optimizer=opt, metrics=["accuracy"])

    earlystop = EarlyStopping(monitor='val_loss', mode='min', patience=7)
    callbacks = [earlystop]

    history = model.fit(x=X_train, y=y_train, epochs=80, batch_size=8, shuffle=True, validation_split=0.2,
                        callbacks=callbacks)

    y_pred = model.predict(X_test)
    y_pred = np.argmax(y_pred, axis=1)
    y_test = np.argmax(y_test, axis=1)

    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))

    model.save('RNN_Project.h5')  # creates a HDF5 file


if __name__ == '__main__':
    main()