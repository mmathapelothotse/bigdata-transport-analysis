import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

sns.set_style("whitegrid")

# Visualization 1: Tipping Behavior
def visualize_tipping():
    df = pd.read_csv('bigdata-transport-analysis/data/output/tipping_behavior.txt', sep='\t',\
        names=['payment_type', 'distance_category', 'avg_tip_pct', 'count'])
    df.dropna(inplace=True)
    plt.figure(figsize=(10, 4))
    pivot = df.pivot(index='distance_category', columns='payment_type', values='avg_tip_pct')
    pivot.plot(kind='bar', ax=plt.gca())
    plt.xlabel('Trip Distance Category', fontsize=12)
    plt.ylabel('Average Tip Percentage (%)', fontsize=12)
    plt.title('Tipping Behavior by Payment Type and Distance', fontsize=14, fontweight='bold')
    plt.legend(title='Payment Type')
    plt.tight_layout()
    plt.savefig('bigdata-transport-analysis/results/figures/tipping_behavior.png', dpi=300)
    plt.show()

# Visualization 2: Top Profitable Routes
def visualize_profitable_routes():
    df = pd.read_csv('bigdata-transport-analysis/data/output/route_profitability.txt', sep='\t',
                     names=['route', 'total_revenue', 'trip_count', 'avg_rpm'])
    
    top_20 = df.head(20)

    fig = px.bar(top_20, x='route', y=['total_revenue'],
                 title='Top 20 Most Profitable Routes',
                 labels={'value': 'Revenue ($)', 'variable': 'Metric'},
                 barmode='group',
                 height=600)
    plt.savefig('bigdata-transport-analysis/results/figures/profitable_routes.png')
    fig.show()

if __name__ == "__main__":
    print("Generating visualizations...")
    visualize_tipping()
    visualize_profitable_routes()
    print("Visualizations saved to results/figures/")
