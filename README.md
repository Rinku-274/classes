Welcome to the Seismic b-value Analysis Repository! This repository contains tools and tutorials for analyzing seismic events, including fetching data, mapping seismic activity, and estimating the b-value. Below is a brief overview of the contents and how to use them.
Repository Contents
1. seismic_b_value.pdf

    Description: This PDF contains an explanation of the seismic b-value concept, its significance, and details on how it is calculated. An example is included to help understand the calculation process.
    Usage: Read this document to understand the seismic b-value and its importance in seismic studies.

2. seismic_event_extraction.ipynb

    Description: This Jupyter Notebook demonstrates how to fetch seismic event data from the ISC catalog using ObsPy. The data is then saved to a CSV file for further use.
    Usage: Use this notebook to learn how to obtain and save seismic event data for subsequent analysis or research.

3. seismic_event_mapping.ipynb

    Description: This Jupyter Notebook illustrates how to create a map of seismic events using PyGMT. The map features topographic elements and plots each earthquake with markers that vary in size according to magnitude and are color-coded by depth.
    Usage: This notebook is ideal for visualizing the spatial distribution of seismic events and understanding their geographical context.

4. b_value_estimation_and_plotting.ipynb

    Description: This Jupyter Notebook demonstrates the estimation of the seismic b-value using the maximum likelihood method. It also shows how to visualize the b-value and its uncertainties in a Gutenberg-Richter plot.
    Usage: Use this notebook to estimate and plot the b-value of seismic events, which provides insights into the seismicity of a given region.

Python Scripts

    seismic_event_extraction.py: Python script version of seismic_event_extraction.ipynb
    seismic_event_mapping.py: Python script version of seismic_event_mapping.ipynb
    b_value_estimation_and_plotting.py: Python script version of b_value_estimation_and_plotting.ipynb

Getting Started
1. Clone the Repository:
git clone https://github.com/your-username/seismic-analysis-repo.git
2. Install Required Packages: Ensure you install the necessary Python packages. You can install them using pip:
pip install obspy pygmt pandas matplotlib
2. Run the Notebooks/Scripts:
Launch Jupyter Notebook and open the .ipynb files to follow the tutorials interactively.
Run the Python scripts from the command line or your preferred IDE.

Contributions

Feel free to fork the repository, make improvements, and submit pull requests. Contributions to enhance the analysis and visualization tools are welcome!
