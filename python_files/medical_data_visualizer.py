import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('../data/medical_examination.csv')

# Add 'overweight' column
df['bmi'] = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = df['bmi'].apply(lambda x: 1 if x > 25.0 else 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
def replace_values(value):
    if value > 1:
        return 1
    else:
        return 0
df['gluc'] = df['gluc'].apply(replace_values)
df['cholesterol'] = df['cholesterol'].apply(replace_values)

# Draw Categorical Plot
def draw_cat_plot():
    # Convert the data into long format
    columns_to_melt = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    melted_df = pd.melt(df, id_vars=['cardio'], value_vars=columns_to_melt, var_name='attribute', value_name='value')

    # Plotting
    # Create a cat plot using Seaborn's catplot()
    g = sns.catplot(data=melted_df, x='attribute', hue='value', kind='count', col='cardio', height=4, aspect=1.5, sharey=False)
    g.set_axis_labels('Attribute', 'Count')
    g.set_titles('Cardio: {col_name}')
    g.legend.set_title('Value')
    plt.subplots_adjust(top=0.85)  # Adjust top spacing for the titles
    plt.suptitle('Categorical Features Count by Cardio')
    plt.show()
    
    # Get the figure for the output
    fig = g.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
# Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, fmt=".1f", linewidths=0.5, mask=mask, vmax=0.25, center=0, square=True, cbar_kws={"shrink": 0.75})
    plt.title("Correlation Plot")
    plt.show()

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig