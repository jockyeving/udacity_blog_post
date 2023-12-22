import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def merge_results(dict1, dict2):
    '''
    INPUT:
    dict1 (dict) - programming languages by current workers
    dict2 (dict) - programming languages based on future plans
    OUTPUT:
    result (pd.DataFrame) - both dictionaries merged into a pandas DataFrame 
    
    Merges the two dictionaries based on their keys, into a pandas DataFrame.
    '''
    
    result = pd.DataFrame(columns = ['HaveWorkedLanguage', 'WantWorkLanguage'], index=list(dict2.keys()))
    for language in list(dict2.keys()):
        result.at[language, 'HaveWorkedLanguage'] = dict1[language]
        result.at[language, 'WantWorkLanguage'] = dict2[language]

    return result

def languages_by_column(df, colname):
    '''
    INPUT:
    df (pd.DataFrame) - raw dataset
    colname (str) - name of the row to do the calculation on
    OUTPUT:
    result (dict) - programming languages counted in selected column 
    
    Counts preset set of programming languages in a given column.
    '''

    tmp = df[colname] + ';'
    tmp = tmp.dropna().reset_index().drop('index',axis=1)

    languages = [ 'Python', 'Ruby', 'R', 'Java', 'JavaScript', 'Assembly', 'C', 'C++', 'PHP', 'C#', 'SQL', 'Rust']
    result = {'Python' : 0,
              'R' : 0,
              'Ruby' : 0,
              'Rust' : 0,
              'Java' : 0,
              'JavaScript' : 0,
              'PHP' : 0,
              'SQL' : 0,
              'C' : 0,
              'C++' : 0,
              'C#' : 0,
              'Assembly' : 0
    }

    for row in tmp[colname]:
        for language in languages:
            if language + ';' in row:
                result[language] += 1

    return result

def plot_result(result):
    '''
    INPUT:
    result (pd.DataFrame) - count of programming languages stored in a DataFrame
    
    Plots worked, and desired programming languages side by side, ordered by which is worked on by most currently.
    '''
    
    x = np.arange(len(result))
    y1 = result.HaveWorkedLanguage
    y2 = result.WantWorkLanguage

    fig, ax = plt.subplots(figsize =(12, 8))

    ax.grid(b = True, color ='grey',
            linestyle ='-.', linewidth = 0.5,
            alpha = 0.2)


    plt.barh(x, y1, height=0.3, color= 'deepskyblue', tick_label = list(result.index), label = 'Have worked before')
    plt.barh(x-0.3, y2, height=0.3,  color = 'orange', label = 'Want to work in the future')

    for i in ax.patches:
        plt.text(i.get_width(), i.get_y()+0.05, 
                str(round((i.get_width()), 2)),
                fontsize = 10,
                color ='grey')

    ax.set_title('Worked and desired programming languages',
                loc ='left', )

    plt.xlabel = 'languages'
    plt.ylabel = 'number of people'
    plt.legend()
    plt.show()