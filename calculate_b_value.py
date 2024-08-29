import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

# Function to estimate b-value using maximum likelihood method (Aki, 1965)
def b_est(mag, mbin, mc):
    mag_above_mc = mag[np.where(mag > round(mc, 1) - mbin / 2)[0]]  # Magnitudes for events larger than cut-off magnitude mc
    n = mag_above_mc.shape[0]  # Number of events larger than cut-off magnitude mc
    if n < 2:
        a = np.nan
        b = np.nan
        aki_unc = np.nan
        shibolt_unc = np.nan
    else:
        mbar = np.mean(mag_above_mc)  # Mean magnitude for events larger than cut-off magnitude mc
        b = math.log10(math.exp(1)) / (mbar - (mc - mbin / 2))  # b-value
        a = math.log10(n) + b * mc  # 'a-value'
        aki_unc = b / math.sqrt(n)  # Aki uncertainty estimate
        shibolt_unc = 2.3 * b**2 * math.sqrt(np.sum((mag_above_mc - mbar)**2) / (n * (n - 1)))  # Shi & Bolt uncertainty estimate

    return a, b, aki_unc, shibolt_unc  # Return b-value and estimates of uncertainty

# Load the data
df = pd.read_csv('./seismic_events.csv')

# Extract magnitudes
magnitudes = df['Magnitude'].values

# Define parameters for b-value estimation
cat_mc = 3.0  # Set this to a higher value based on your analysis
mbin = 0.1  # Magnitude bin size

# Calculate b-value
cat_a, cat_b, cat_aki_unc, cat_shibolt_unc = b_est(mag=magnitudes, mbin=mbin, mc=cat_mc)

# Calculate frequency for plotting
# Create magnitude bins for frequency count
bin_edges = np.arange(magnitudes.min(), magnitudes.max() + mbin, mbin)
cat_nbmag, _ = np.histogram(magnitudes, bins=bin_edges)  # Number of events in each bin
cat_cumnbmag = np.cumsum(cat_nbmag[::-1])[::-1]  # Cumulative frequency

# Midpoint of bins for plotting
cat_mi = 0.5 * (bin_edges[1:] + bin_edges[:-1])

# Calculate fitted line values for plotting
fitted_line_values = (10 ** (cat_a - (cat_b * cat_mi)))

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(cat_mi, cat_cumnbmag, 'o', label='Cumulative Frequency', color='red')  # Red dots for cumulative frequency
plt.plot(cat_mi, fitted_line_values, label='Fitted Line', color='blue')  # Fitted line in blue

# Calculate frequency at Mc using the fitted line
frequency_at_mc = 10 ** (cat_a - (cat_b * cat_mc))

# Plot green triangle at Mc value
plt.scatter(cat_mc, frequency_at_mc, color='green', marker='^', s=100, label='Magnitude of Completeness (Mc)')  # Green triangle at Mc

plt.yscale('log')
plt.ylim(1, 10**math.ceil(math.log10(df.shape[0])))
plt.xlabel('Magnitude')
plt.ylabel('Frequency')
plt.title('b-value plot')

# Adjusted text positions
plt.text(x=cat_mc + 0.1, y=2.5e3, s="Mc = " + str(round(cat_mc, 1)))  # Closer position for Mc
plt.text(x=cat_mc + 0.1, y=2e3, s="b-value = " + str(round(cat_b, 3)) + " +/- " + str(round(cat_shibolt_unc, 3)))  # Closer position for b-value

plt.legend()
plt.grid(True)
plt.show()
