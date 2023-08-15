import numpy as np
import matplotlib.pyplot as plt

# Initialise random number generator with a set seed for reproducibility
rng = np.random.default_rng(seed=42)

# Define function to fit against & a way to add noise
def curve(x):
    return np.cos(x) * np.arctan(np.abs(x))

def noise(x):
    return 0.1 + (x + 5) / 30

def add_noise(x, y):
    return y + rng.normal(scale=noise(x), size=len(x))

# Generate our data & plot
x_data = rng.uniform(low=-5, high=10.5, size=250)
y_data = add_noise(x_data, curve(x_data))
plt.scatter(x_data, y_data, label="data")

# Also plot the actual curve
x_curve = np.linspace(-8, 13, num=200)
y_curve = curve(x_curve)
y_noise = noise(x_curve)
plt.plot(x_curve, y_curve, 'k-', zorder=1000, lw=3, alpha=0.5, label="curve")
plt.plot(x_curve, y_curve + 2*y_noise, 'k-', zorder=1000, lw=1, alpha=0.5, label="+- 2 std dev")
plt.plot(x_curve, y_curve - 2*y_noise, 'k-', zorder=1000, lw=1, alpha=0.5)
plt.legend(edgecolor="k")

# Save a figure & the data itself
plt.savefig("curve.png", dpi=300)
plt.close("all")
np.save("data.npy", np.asarray([x_data, y_data]))
