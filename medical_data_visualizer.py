import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Load dataset
df = pd.read_csv('medical_examination.csv')

# 2. Add overweight column
df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = (df['BMI'] > 25).astype(int)
df.drop(columns='BMI', inplace=True)

# 3. Normalize cholesterol and glucose
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Draw Categorical Plot
def draw_cat_plot():
    # 5. Melt DataFrame
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )

    # 6. Group and count
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']) \
                   .size().reset_index(name='total')

    # 7. Draw plot
    catplot = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        kind='bar',
        col='cardio'
    )

    # 8. Get fig
    fig = catplot.fig

    # 9. Return fig
    return fig

# 10. Draw Heatmap
def draw_heat_map():
    # 11. Clean data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12. Correlation matrix
    corr = df_heat.corr()

    # 13. Create mask
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14. Setup figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # 15. Draw heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5}
    )

    # 16. Return fig
    return fig
