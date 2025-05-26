
import numpy as np
import pandas as pd

# Generate data
x = np.linspace(0, 100, 1000)
sine = np.sin(x)
cosine = np.cos(x)
sine_2x = np.sin(2 * x)
noise = np.random.normal(0, 0.1, size=x.shape)

# Create DataFrame
df = pd.DataFrame({
    'sine': sine,
    'cosine': cosine,
    'sine_2x': sine_2x,
    'noise': noise
})

# Save to CSV
df.to_csv('sine_wave_multi.csv', index=False)
print("sine_wave_multi.csv generated.")
