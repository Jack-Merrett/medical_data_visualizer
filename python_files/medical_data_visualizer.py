import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('../data/medical_examination.csv')

# Add 'overweight' column
df['overweight'] = None

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
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    columns_to_melt = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    melted_df = pd.melt(df, value_vars=columns_to_melt, value_name='value', var_name='attribute')

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    # Assuming your DataFrame is named 'df_cat'
    grouped = melted_df.groupby(['cardio', 'attribute', 'value']).size().reset_index(name='total_count')

    # Pivot the table to have 'attribute' as columns and 'value' as index
    pivot_table = grouped.pivot_table(index=['cardio', 'value'], columns='attribute', values='total_count', fill_value=0)

    # Rename columns for the catplot
    pivot_table.columns = [f'{col}_count' for col in pivot_table.columns]

    # Reset index for the DataFrame
    pivot_table = pivot_table.reset_index()

    # Plotting
    sns.set(style="whitegrid")
    g = sns.catplot(data=pivot_table, x='cardio', y='cholesterol_count', hue='value', kind='bar')
    g.set_axis_labels("Cardiovascular Disease", "Cholesterol Counts")
    plt.show()

    # Get the figure for the output
    fig = g.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
