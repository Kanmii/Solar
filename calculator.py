# Appliance Energy Calculator

# This script calculates the total wattage and kWh usage for a list of appliances.

import pandas as pd

def load_appliance_data():
    """
    Loads appliance data from appliances.csv into a pandas DataFrame.
    """
    try:
        df = pd.read_csv('appliances.csv')
        # Clean up column names for easier access
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
        return df
    except FileNotFoundError:
        print("Error: appliances.csv not found. Make sure the file is in the same directory as the script.")
        return None

def find_appliance(df, appliance_name):
    """
    Finds an appliance in the DataFrame based on its name.
    """
    appliance_name = appliance_name.strip().lower()
    results = df[df['appliance'].str.lower() == appliance_name]
    return results

def get_user_appliance_selection(appliances):
    """
    Prompts the user to select an appliance from a list of matches.
    """
    print("\nMultiple appliances found. Please select one:")
    for i, row in appliances.iterrows():
        print(f"{i+1}: {row['appliance']} - {row['type/variant']} ({row['min_power_w']}W - {row['max_power_w']}W)")

    while True:
        try:
            choice = int(input(f"Enter your choice (1-{len(appliances)}): "))
            if 1 <= choice <= len(appliances):
                return appliances.iloc[choice - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """
    Main function to run the appliance energy calculator.
    """
    print("Appliance Energy Calculator")
    print("---------------------------")

    df = load_appliance_data()
    if df is None:
        return

    total_wattage = 0
    total_kwh = 0
    selected_appliances = []

    while True:
        appliance_name = input("\nEnter the name of an appliance (or 'done' to finish): ")
        if appliance_name.lower() == 'done':
            break

        matches = find_appliance(df, appliance_name)

        if len(matches) == 0:
            print(f"Appliance '{appliance_name}' not found. Please try again.")
            continue
        elif len(matches) == 1:
            appliance = matches.iloc[0]
        else:
            appliance = get_user_appliance_selection(matches)

        while True:
            try:
                hours = float(input(f"Enter the daily usage in hours for {appliance['appliance']}: "))
                if hours >= 0:
                    break
                else:
                    print("Please enter a non-negative number for hours.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Use the average of min and max power for calculation
        wattage = (appliance['min_power_w'] + appliance['max_power_w']) / 2
        kwh = (wattage * hours) / 1000

        total_wattage += wattage
        total_kwh += kwh
        selected_appliances.append((appliance['appliance'], wattage, hours, kwh))

        print(f"\nAdded: {appliance['appliance']} ({wattage:.2f}W) for {hours} hours -> {kwh:.2f} kWh")

    print("\n---------------------------")
    print("Calculation Complete")
    print("---------------------------")
    print("Selected Appliances:")
    for name, wattage, hours, kwh in selected_appliances:
        print(f"- {name}: {wattage:.2f}W, {hours} hours/day, {kwh:.2f} kWh/day")

    print("\nTotal Wattage: {:.2f} W".format(total_wattage))
    print("Total Daily Energy Consumption: {:.2f} kWh".format(total_kwh))


if __name__ == "__main__":
    main()
