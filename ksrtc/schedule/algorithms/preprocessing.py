import pandas as pd

class DataPreprocessor:
    def __init__(self):
        self.df = pd.DataFrame()

    # Function to convert time to seconds
    @staticmethod
    def time_to_seconds(time_obj):
        return time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second

    # Function to convert seconds to human-readable time format
    @staticmethod
    def seconds_to_time(df, columns):
        df[columns] = df[columns].apply(lambda x: pd.to_datetime(x, unit='s').dt.strftime('%H:%M:%S'))

    def preprocess_data(self, input_file_path):
        try:
            # Read the Excel file and drop duplicates
            self.df = pd.read_excel(input_file_path)
        except FileNotFoundError:
            return None

        if not all(self.df.columns):
            return None

        self.df = self.df.dropna().drop_duplicates()

        # Iterate through each column name and apply renaming logic
        for col in self.df.columns:
            if 'sl no.' in col.casefold():
                self.df = self.df.rename(columns={col: 'Sl No.'})
            elif 'departure' in col.casefold() and 'place' in col.casefold():
                self.df = self.df.rename(columns={col: 'Departure Place'})
            elif 'departure' in col.casefold() and 'time' in col.casefold():
                self.df = self.df.rename(columns={col: 'Departure Time'})
            elif 'arrival' in col.casefold() and 'place' in col.casefold():
                self.df = self.df.rename(columns={col: 'Arrival Place'})
            elif 'arrival' in col.casefold() and 'time' in col.casefold():
                self.df = self.df.rename(columns={col: 'Arrival Time'})
            elif 'Running' in col.casefold() and 'time' in col.casefold():
                self.df = self.df.rename(columns={col: 'Running Time'})

        # Convert time columns to datetime and then to seconds
        time_columns = ['Departure Time', 'Arrival Time', 'Running Time']
        for col in time_columns:
            self.df[col] = pd.to_datetime(self.df[col], format='%H:%M:%S', errors='coerce').dt.time
            self.df[col] = self.df[col].apply(self.time_to_seconds)

        # Convert other columns to appropriate data types
        for col in self.df.columns:
            if col not in time_columns:  # Exclude time columns
                self.df[col] = self.df[col].convert_dtypes()

        # Sort the DataFrame by 'Departure Time' column
        sorted_df = self.df.sort_values('Departure Time', ascending=True).reset_index(drop=True)

        return sorted_df

def processor_main(input_file_path):
    data_preprocessor = DataPreprocessor()
    preprocessed_df = data_preprocessor.preprocess_data(input_file_path)
    if preprocessed_df is not None:
        return preprocessed_df
    else:
        return pd.DataFrame()

# # Example usage:
# result_df = processor_main()
# print(result_df)
