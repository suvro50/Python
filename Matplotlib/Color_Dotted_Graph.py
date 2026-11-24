import matplotlib.pyplot as plt
import numpy as np

# Matplotlib's fmt (Format String) has this syntax: marker | line | color
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, "o:r", ms="10",mfc="b") # o->Circle marker,  :->Dotted line,  r->Red color
plt.show()

# For Lines: 
# ms=marker Size
# mfc= point color
# '-'	Solid line	
# ':'	Dotted line	
# '--'Dashed line	
# '-.'Dashed/dotted line

# For Color:
# 'r'	Red	
# 'g'	Green	
# 'b'	Blue	
# 'c'	Cyan	
# 'm'	Magenta	
# 'y'	Yellow	
# 'k'	Black	
# 'w'	White
