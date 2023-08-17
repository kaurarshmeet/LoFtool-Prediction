"""
correlation matrices
Resources I learned from;
[1] https://datatofish.com/correlation-matrix-pandas/
[2] https://www.freecodecamp.org/news/matplotlib-figure-size-change-plot-size-in-python/#:~:text=Here's%20what%20the%20syntax%20looks%20like%3A&text=We've%20added%20one%20new,and%20height%20of%20the%20plot.
"""
#making histograms for all varaibles
import pandas as pd

df_loftool = pd.read_csv('df_loftool.csv')

import seaborn as sn
import matplotlib.pyplot as plt

corr_loftool_untransformed = df_loftool.corr(method = 'pearson')
print("Untransformed, mean encoded and imputed caddphred dataset:", corr_loftool_untransformed)
sn.heatmap(corr_loftool_untransformed, annot = True)
plt.figure(figsize=(11,9))
plt.savefig('corr.png', dpi=800, bbox_inches = 'tight')
plt.show()
plt.close()

