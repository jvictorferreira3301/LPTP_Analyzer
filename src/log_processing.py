import pandas as pd
import re

def process_log_file(log_file, offset_pattern, freq_pattern):
    with open(log_file, 'r') as file:
        log_data = file.read()
        
    offset_data = re.findall(offset_pattern, log_data)
    df_offsets = pd.DataFrame(offset_data, columns=['elapsed_time', 'time_offset'])
    df_offsets['elapsed_time'] = pd.to_numeric(df_offsets['elapsed_time'])
    df_offsets['time_offset'] = pd.to_numeric(df_offsets['time_offset'])

    freq_data = re.findall(freq_pattern, log_data)
    df_frequencies = pd.DataFrame(freq_data, columns=['elapsed_time', 'frequency_offset'])
    df_frequencies['elapsed_time'] = pd.to_numeric(df_frequencies['elapsed_time'])
    df_frequencies['frequency_offset'] = pd.to_numeric(df_frequencies['frequency_offset'])
    
    df = pd.merge(df_offsets, df_frequencies, on='elapsed_time', how='outer')
    df = df.sort_values(by='elapsed_time').reset_index(drop=True)
    df['seconds'] = df['elapsed_time'] - df['elapsed_time'].iloc[0]
    df = df[['seconds', 'time_offset', 'frequency_offset']]

    return df