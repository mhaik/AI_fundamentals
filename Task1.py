import streamlit as st
import numpy as np
from matplotlib import pyplot as plt

st.title("Data visualizer and generator")

def generator(num_modes, num_samples, mean_range, cov_range):
    samples = []

    for mode in range(num_modes):
        
        mean_x, mean_y = np.random.uniform(mean_range[0], mean_range[1], 2)
        sigma_x, sigma_y = np.random.uniform(cov_range[0], cov_range[1], 2)
        x_samples = np.random.normal(mean_x, sigma_x, num_samples)
        y_samples = np.random.normal(mean_y, sigma_y, num_samples)

        mode_samples = np.column_stack((x_samples, y_samples))
        samples.append(mode_samples)
 
    samples = np.vstack(samples)
    return samples

# Sidebar 

st.sidebar.header("Input")
samples = st.sidebar.slider("Number of samples", 100, 1000, 200)
modes = st.sidebar.slider("Number of modes", 2, 9, 2)
mean_range = [-1.0, 1.0]
cov_range = [0.01, 0.1]

# Plot

samples_class_0 = generator(modes, samples, mean_range, cov_range)
samples_class_1 = generator(modes, samples, mean_range, cov_range)
fig, ax = plt.subplots()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.scatter(samples_class_0[:, 0], samples_class_0[:, 1], color='red') # class 0
ax.scatter(samples_class_1[:, 0], samples_class_1[:, 1], color='blue') # class 1
st.pyplot(fig)