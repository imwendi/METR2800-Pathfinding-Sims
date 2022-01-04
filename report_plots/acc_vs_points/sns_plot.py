import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sim import setup_tex

sns.set_theme(style="darkgrid")
sns.set_palette('dark')
data = np.load('data604.npy')

#setup_tex()
fig, ax = plt.subplots(figsize=(10, 3))
sns.lineplot(x=data[0], y=data[1]*100, ax=ax)
ax.set_title('Axes Search Algorithm Accuracy')
ax.set_xlabel('# Sampled Points')
ax.set_ylabel('% Accuracy')
fig.show()
fig.savefig("acc_vs_points.png", dpi=300)