import pandas as pd
import matplotlib.pyplot as plt
import os
#First we prepare our required data in a format easier to plot.
def prep_data(scores, weights):
    """
    This functions starts by reshaping our data in a format suitable for plotting.
    It takes as input both the scores and weights lists.
    It returns a dataframe that describes the attributes of each trial.
    params:
    scores: the scores list
    weights: the weights list
    """
    df= pd.DataFrame(weights, scores)
    df['scores']= scores
    df['trial']= range(0, len(scores))
    return df
#First visualization is a histogram that shows the score distribution.
def vis_scores(scores,weights, save_path=None):
    """
    This function is used for the first visualization of the score distribution.
    A histogram is used as it can show frequencies even among large datasets of trials.
    It starts by preparing the data and then uses the scores column.
    params:
    scores: the scores list
    weights: the weights list
    """

    df= prep_data(scores,weights)

    plt.figure()
    plt.hist(df['scores'], bins= 'auto')
    plt.title('Score Distribution')
    plt.xlabel('Score')
    plt.ylabel('Frequency')

    # saving the plot to the data file.
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path)

    plt.show()


#The weight plots will show the weights frequency.
#This tests if the algorithm was biased to choose a certain answer repeatedly.
def vis_weights(score,weights, possible_answers, save_path=None):
    """
    This function is used for the second visualization of the relative weights distribution.
    It represents each choice from the possible answers in a histogram that counts the weight frequencies of that choice.
    All the histograms are in a shared figure but each with its own subplot.
    It starts by preparing the data then visualizing the weights column.
    params:
    scores: the scores list
    weights: the weights list
    possible_answers: the list of possible answers to choose from
    """

    df= prep_data(score,weights)

    fig, axes = plt.subplots(1, len(possible_answers), sharey=True)
    axes = axes.flatten()

    for i, col in enumerate(possible_answers):
        axes[i].hist(df[col])
        axes[i].set_title(f"{col} Weight")
        axes[i].set_xlabel(col)
    fig.supylabel('Frequency')
    plt.tight_layout()

    # saving the plot to the data file
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path)

    plt.show()


#The next plot tests the randomness of the guess as trials progress.
#I.e. does the trial number(random seed) affect the choices' accuracy.
def vis_seeds(scores,weights,save_path=None):
    """
    This function visualizes the relation between the random seed/trial number and the score obtained in that trial.
    It takes into account the visualization suitable for the size of the trial.
    The plots have been split into conditions: less than 50 trials, between 50 and 100, between 100 and 500, between 500 and 1000 and more than 1000.
    Each condition has its own style, with line plots useful for small samples, and scatter plots for larger.
    The larger samples also use chunked subplots to avoid messy plots.
    It starts by preparing the data then uses the scores and trial number column.
    params:
    scores: the scores list
    weights: the weights list
    """
    df= prep_data(scores,weights)

    #A simple line plot is suitable for data with less than 50 points.
    if len(df['scores']) <=50:
        plt.figure()
        plt.plot(df['trial'], df['scores'])
        plt.title('Seed vs. Score')
        plt.xlabel('Seed Number')
        plt.ylabel('Score')

        #saving the plot
        if save_path:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            plt.savefig(save_path)

        plt.show()


    #A scatter plot with moderate transparency is suitable for data with 50-100 points.
    elif 50 < len(df['scores']) <= 100:
        plt.figure()
        plt.scatter(df['trial'], df['scores'], s=0.5)
        plt.title('Seed vs. Score')
        plt.xlabel('Seed Number')
        plt.ylabel('Score')

        #saving the plot
        if save_path:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            plt.savefig(save_path)

        plt.show()


    #2 Scatter plots in the same row for data between 100-500 points
    elif 100 < len(df['scores']) <= 500:
        chunk_size=len(df['scores'])//2
        fig, ax= plt.subplots(1,2, sharey=True)
        for i in range(0,2):
            data=df.iloc[i*chunk_size:(i+1)*chunk_size]
            ax[i].scatter(data['trial'], data['scores'], s=0.5)
            plt.tight_layout(rect=(0,0,1,0.95))
        fig.suptitle('Seed vs. Score')
        fig.supxlabel('Seed Number')
        fig.supylabel('Score')

        #saving the plot
        if save_path:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            plt.savefig(save_path)

        plt.show()

    #5 scatter plots in the same row
    elif 500 < len(df['scores']) <= 1000:
        chunk_size=len(df['scores'])//5
        fig, ax= plt.subplots(1,5, sharey=True)
        for i in range(0,5):
            data=df.iloc[i*chunk_size:(i+1)*chunk_size]
            ax[i].scatter(data['trial'], data['scores'], s=0.5)
            plt.tight_layout(rect=(0,0,1,0.95))
        fig.suptitle('Seed vs. Score')
        fig.supxlabel('Seed Number')
        fig.supylabel('Score')

        #saving the plot
        if save_path:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            plt.savefig(save_path)

        plt.show()

    #25 subplots for over 1000 points
    else:
        chunk_size= len(df['scores'])//25
        fig, axes= plt.subplots(5, 5,sharey=True)
        for i in range(0, 25):
            data= df.iloc[i*chunk_size:(i+1)*chunk_size]
            row= i//5
            col= i%5
            axes[row, col].scatter(data['trial'], data['scores'], s=0.1)
        plt.tight_layout(rect=(0,0,1,0.95))
        fig.suptitle('Seed vs. Score')
        fig.supxlabel('Seed Number')
        fig.supylabel('Score')

        #saving the plot
        if save_path:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            plt.savefig(save_path)

        plt.show()




