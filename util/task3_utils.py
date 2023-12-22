import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_result(result):
    '''
    INPUT:
    result (pd.DataFrame) - DataFrame to be plotted
    
    Plots Job Satisfaction based on whether a worker thinks they are underpaid/overpaid.
    '''

    x = np.arange(len(result.index))
    fig,ax = plt.subplots(figsize =(12, 5))
    ax.grid(b = True, color ='grey',
                linestyle ='-.', linewidth = 0.5,
                alpha = 0.2)
    
    plt.bar(x, result, tick_label = list(result.index), width=0.2)

    ax.set_title('Job satisfaction related to being overpaid/underpaid', loc ='left', )
    plt.xlabel = 'Am I underpaid/overpaid?'
    plt.ylabel = 'Job Satisfaction'
    plt.show()