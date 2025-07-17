import os
import pandas as pd

# Data Analysis Agent
def run():
    print('Analyzing CSV files...')
    for file in os.listdir('/workspaces/Agents'):
        if file.endswith('.csv'):
            df = pd.read_csv(os.path.join('/workspaces/Agents', file))
            print(df.describe())

if __name__ == '__main__':
    run()
