import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Simulate IoT sensor data (replace this with your actual data source)
def generate_sensor_data(num_samples=100):
    timestamps = pd.date_range(start='2022-01-01', periods=num_samples, freq='H')
    temperature_values = np.random.normal(25, 5, num_samples)
    humidity_values = np.random.normal(50, 10, num_samples)
    sensor_data = pd.DataFrame({'Timestamp': timestamps, 'Temperature (C)': temperature_values, 'Humidity (%)': humidity_values})
    return sensor_data

# Function to plot sensor data
def plot_sensor_data(sensor_data):
    fig, ax1 = plt.subplots(figsize=(10, 6))

    color = 'tab:red'
    ax1.set_xlabel('Timestamp')
    ax1.set_ylabel('Temperature (C)', color=color)
    ax1.plot(sensor_data['Timestamp'], sensor_data['Temperature (C)'], color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Humidity (%)', color=color)
    ax2.plot(sensor_data['Timestamp'], sensor_data['Humidity (%)'], color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    st.pyplot(fig)

# Main Streamlit app
def main():
    st.title('IoT Sensor Data Dashboard')

    # Generate some sample sensor data
    sensor_data = generate_sensor_data(num_samples=1000)

    # Display the sensor data table
    st.subheader('Sensor Data')
    st.write(sensor_data)

    # Display the sensor data plot
    st.subheader('Sensor Data Visualization')
    plot_sensor_data(sensor_data)

    # Additional functionalities (e.g., real-time data, data filtering) can be added here

if __name__ == '__main__':
    main()
