import matplotlib.pyplot as plt

def visualize_dacade_sunshine(decade_averages):
    """
    Visualizes the average sun hours for each decade using a bar chart.
    """
    if not decade_averages:
        print("No data available for visualization.")
        return
    
    labels, averages = zip(*decade_averages)
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, averages, color='skyblue')
    plt.xlabel('Decade')
    plt.ylabel('Average Sun Hours per Day (Jan & Dec)')
    plt.title('Average Sun Hours in January and December by Decade')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    # Add value labels on top of the bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')
    plt.tight_layout()
    plt.show()