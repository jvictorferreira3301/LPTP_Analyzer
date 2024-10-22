import matplotlib.pyplot as plt
import os
from statsmodels.graphics.tsaplots import plot_acf

def plot_graphs(log_files, dataframes, y_label, plot_suffix, color='blue', single_log_file=None):
    if single_log_file is not None:
        dataframes = {single_log_file: dataframes[single_log_file]}
        log_files = [single_log_file]
    
    global_min_seconds = float('inf')
    global_max_seconds = float('-inf')
    global_min_value = float('inf')
    global_max_value = float('-inf')

    for log_file in log_files:
        df = dataframes[log_file]
        global_min_seconds = min(global_min_seconds, df['seconds'].min())
        global_max_seconds = max(global_max_seconds, df['seconds'].max())
        global_min_value = min(global_min_value, df['offset'].min())
        global_max_value = max(global_max_value, df['offset'].max())

    for log_file in log_files:
        df = dataframes[log_file]
        
        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 6), gridspec_kw={'width_ratios': [3, 1]})
        
        ax1.plot(df['seconds'], df['offset'], color=color)
        ax1.set(xlabel='Elapsed Time (s)', ylabel=y_label)
        ax1.set_xlim(global_min_seconds, global_max_seconds)
        ax1.set_ylim(global_min_value, global_max_value)
        ax1.set_title(os.path.basename(log_file))
        
        ax2.hist(df['offset'], bins=50, orientation='horizontal', edgecolor='black', color=color)
        ax2.set(ylabel=y_label, xlabel='Occurrences')
        ax2.set_ylim(ax1.get_ylim())
        
        plt.tight_layout()
        
        base_name = os.path.basename(log_file)
        plot_file_name = f'plots/{base_name}_{plot_suffix}.png'
        plt.savefig(plot_file_name, format='png', bbox_inches='tight')
        plt.show()

def plot_acf_log(df, column, title, lags=50):
    plt.figure(figsize=(10, 6))
    plot_acf(df[column], lags=lags, alpha=0.05)
    plt.title(title)
    plt.xlabel('Lags')
    plt.ylabel('Autocorrelation')
    plt.show()

def plot_frequency_graphs(log_files, dataframes, y_label, plot_suffix, color='blue', single_log_file=None):
    if single_log_file is not None:
        dataframes = {single_log_file: dataframes[single_log_file]}
        log_files = [single_log_file]
    
    global_min_seconds = float('inf')
    global_max_seconds = float('-inf')
    global_min_value = float('inf')
    global_max_value = float('-inf')

    for log_file in log_files:
        df = dataframes[log_file]
        global_min_seconds = min(global_min_seconds, df['seconds'].min())
        global_max_seconds = max(global_max_seconds, df['seconds'].max())
        global_min_value = min(global_min_value, df['frequency'].min())
        global_max_value = max(global_max_value, df['frequency'].max())

    for log_file in log_files:
        df = dataframes[log_file]
        
        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 6), gridspec_kw={'width_ratios': [3, 1]})
        
        ax1.plot(df['seconds'], df['frequency'], color=color)
        ax1.set(xlabel='Elapsed Time (s)', ylabel=y_label)
        ax1.set_xlim(global_min_seconds, global_max_seconds)
        ax1.set_ylim(global_min_value, global_max_value)
        ax1.set_title(os.path.basename(log_file))
        
        ax2.hist(df['frequency'], bins=50, orientation='horizontal', edgecolor='black', color=color)
        ax2.set(ylabel=y_label, xlabel='Occurrences')
        ax2.set_ylim(ax1.get_ylim())
        
        plt.tight_layout()
        
        base_name = os.path.basename(log_file)
        plot_file_name = f'plots/{base_name}_{plot_suffix}.png'
        plt.savefig(plot_file_name, format='png', bbox_inches='tight')
        plt.show()