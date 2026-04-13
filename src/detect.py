def detect_threat(model, sample):

    prediction = model.predict(sample)

    if prediction[0] == 0:
        print("Normal Traffic")
    else:
        print("⚠ Potential Cyber Attack Detected")