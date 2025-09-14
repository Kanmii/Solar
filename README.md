# Appliance Energy Calculator

This project provides a command-line tool to calculate the total wattage and energy consumption (in kWh) of a list of household appliances.

## Usage

1.  Make sure you have Python 3 and `pip` installed.
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the calculator script:
    ```bash
    python calculator.py
    ```

The script will prompt you to enter the name of an appliance and its daily usage in hours. You can enter as many appliances as you like. When you are finished, type `done`.

## `appliances.csv`

The calculator relies on the `appliances.csv` file for appliance power data. Please ensure this file is present in the same directory as the `calculator.py` script.