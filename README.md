# AI-Powered Cybersecurity Threat Detection

Machine learning system that detects network intrusions using the KDD Cup 1999 dataset.

## Features

* Detects malicious network traffic
* Random Forest ML model
* Data preprocessing pipeline
* Attack distribution visualization
* Confusion matrix evaluation

## Tech Stack

* Python
* Scikit-learn
* Pandas
* Matplotlib
* Seaborn

## Dataset

KDD Cup 1999 Intrusion Detection Dataset

Dataset not included due to size.

Download here:
https://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html

## Project Structure

src/
data_loader.py
preprocessing.py
model.py
detect.py
visualizer.py

main.py
predict.py

## Run the Project

Install dependencies:

pip install -r requirements.txt

Train model:

python main.py

Run prediction:

python predict.py

## Results

### Attack Distribution

![Attack Distribution](assets/attack_distribution.png)

### Confusion Matrix

![Confusion Matrix](assets/confusion_matrix.png)

### Example Output

![Example Output](assets/output_example.png)

Detected Traffic Type: land

## Author

Priyanka Badagavi
