import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

sns.set_style("whitegrid")

# Visualization 1: Peak Hour Heatmap
def visualize_peak_hours():
    df = pd.read_csv('data/output/peak_hours.txt', sep='\t', 
                     names=['hour', 'location', 'count'])
    
    # Aggregate by hour
    hourly_demand = df.groupby('hour')['count'].sum().reset_index()
    
    plt.figure(figsize=(12, 6))
    plt.bar(hourly_demand['hour'], hourly_demand['count'], color='skyblue', edgecolor='black')
    plt.xlabel('Hour of Day', fontsize=12)
    plt.ylabel('Number of Pickups', fontsize=12)
    plt.title('NYC Taxi Demand by Hour of Day', fontsize=14, fontweight='bold')
    plt.xticks(range(0, 24))
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('results/figures/peak_hours.png', dpi=300)
    plt.show()

# Visualization 2: Tipping Behavior
def visualize_tipping():
    df = pd.read_csv('data/output/tipping_behavior.txt', sep='\t',
                     names=['payment_type', 'distance_category', 'avg_tip_pct', 'count'])
    
    plt.figure(figsize=(10, 6))
    pivot = df.pivot(index='distance_category', columns='payment_type', values='avg_tip_pct')
    pivot.plot(kind='bar', ax=plt.gca())
    plt.xlabel('Trip Distance Category', fontsize=12)
    plt.ylabel('Average Tip Percentage (%)', fontsize=12)
    plt.title('Tipping Behavior by Payment Type and Distance', fontsize=14, fontweight='bold')
    plt.legend(title='Payment Type')
    plt.tight_layout()
    plt.savefig('results/figures/tipping_behavior.png', dpi=300)
    plt.show()

# Visualization 3: Top Profitable Routes
def visualize_profitable_routes():
    df = pd.read_csv('data/output/route_profitability.txt', sep='\t',
                     names=['route', 'total_revenue', 'trip_count', 'avg_rpm'])
    
    top_20 = df.head(20)
    
    fig = go.Figure(data=[
        go.Bar(name='Total Revenue', x=top_20['route'], y=top_20['total_revenue']),
        go.Line(name='Avg Revenue/Mile', x=top_20['route'], y=top_20['avg_rpm']*100)
    ])
    
    fig.update_layout(
        title='Top 20 Most Profitable Routes',
        xaxis_title='Route (Pickup-Dropoff)',
        yaxis_title='Revenue ($)',
        barmode='group',
        height=600
    )
    
    fig.write_html('results/figures/profitable_routes.html')
    fig.show()

if __name__ == "__main__":
    print("Generating visualizations...")
    visualize_peak_hours()
    visualize_tipping()
    visualize_profitable_routes()
    print("Visualizations saved to results/figures/")
