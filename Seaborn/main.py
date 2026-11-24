# Seaborn: Advanced statistical visualization and data analysis.
# Install Seaborn: pip install seaborn
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot([0, 1, 2, 3, 4, 5])



sns.displot([0, 1, 2, 3, 4, 5], kind="kde")

plt.show()