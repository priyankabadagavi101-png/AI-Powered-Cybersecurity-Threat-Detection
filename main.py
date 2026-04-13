from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.model import train_model
from src.visualizer import plot_attack_distribution

# load dataset
df = load_data("data/network_traffic.csv")

# visualize attack distribution
plot_attack_distribution(df)

# preprocess data
X, y = preprocess_data(df)

# train model
model = train_model(X, y)