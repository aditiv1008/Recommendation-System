# User-Based Algorithm

To run the user-based algorithm, follow these steps:

1. Install required Python packages using conda:
    ```bash
    conda install tensorflow matplotlib numpy pandas os
    ```

2. Install Flask:
    ```bash
    conda install flask
    ```

3. Navigate to the 'app2' folder:
    ```bash
    cd app2
    ```

4. Run the application:
    ```bash
    python run app2
    ```

5. Open the application in a web browser and click on different user buttons to generate recommendations.

# Naive Algorithm for Item-Based

To run the item-based algorithm, follow these steps:

1. Install required Python packages using conda:
    ```bash
    conda install pandas numpy scipy pickle scikit-learn
    ```

2. Install Streamlit:
    ```bash
    conda install streamlit
    ```

3. Run the application:
    ```bash
    streamlit run app.py
    ```

**Note:** If you encounter a pickling error due to a newer version of pandas, create a conda environment and install pandas version 1.3.0:
```bash
conda create --name your_environment_name
conda activate your_environment_name
conda install pandas==1.3.0
