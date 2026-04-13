import matplotlib.pyplot as plt

def plot_attack_distribution(df):

    attack_counts = df.iloc[:, -1].value_counts()

    attack_counts.plot(kind="bar")

    plt.title("Attack Type Distribution")

    plt.xlabel("Attack Type")

    plt.ylabel("Count")

    plt.show()