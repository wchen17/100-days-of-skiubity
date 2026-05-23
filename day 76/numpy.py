# ============================================================
#  DAY 76 — NumPy Array Computation
#  PROJECT: Image manipulation + statistical computation
# ============================================================
#
#  SKILLS TODAY:
#    - import numpy as np
#    - np.array([...])                → create array
#    - np.zeros((r, c)) / np.ones()  → pre-filled arrays
#    - np.arange(start, stop, step)  → range as array
#    - np.linspace(a, b, n)          → n evenly spaced points
#    - array.shape / .ndim / .dtype
#    - Array maths: +, -, *, /       → element-wise, no loops needed
#    - np.mean() / np.max() / np.std()
#    - Boolean indexing: arr[arr > 5]
#    - np.random.rand() / np.random.randint()
#    - Broadcasting: operations on different-shaped arrays
#    - pip install numpy matplotlib
#
# ============================================================

import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------
#  DEMO: Array vs Python list
# --------------------------------------------------
py_list  = [1, 2, 3, 4, 5]
np_array = np.array([1, 2, 3, 4, 5])

# Element-wise multiplication — lists can't do this:
print(np_array * 2)          # [2 4 6 8 10]
print(np_array ** 2)         # [1 4 9 16 25]
print(np_array[np_array > 3])  # [4 5]


# --------------------------------------------------
#  TODO 1: 2D arrays (matrices)
# --------------------------------------------------
# Create a 5×5 identity matrix using np.eye(5)
# Create a 3×3 matrix of random integers 0-9
# Multiply them together using the @ operator (matrix multiply)

# --------------------------------------------------
#  TODO 2: Statistical analysis
# --------------------------------------------------
# Simulate 1000 dice rolls: np.random.randint(1, 7, size=1000)
# Calculate: mean, std, min, max, and the frequency of each face (1-6)
# Plot as a bar chart

rolls = np.random.randint(1, 7, size=1000)
# your analysis here


# --------------------------------------------------
#  TODO 3: Image as a NumPy array
# --------------------------------------------------
# Create a 100×100 greyscale gradient image
# rows = np.linspace(0, 255, 100).astype(np.uint8)
# image = np.tile(rows, (100, 1))
# plt.imshow(image, cmap="gray")
# plt.show()

# Then: flip it, rotate it, add noise, threshold it


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Load a real image: from PIL import Image; np.array(Image.open("photo.jpg"))
#  2. Apply a blur using np.convolve or scipy.ndimage.uniform_filter
#  3. Create a Mandelbrot set visualisation using NumPy broadcasting
# ============================================================
