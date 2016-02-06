#Data Science - Cheat List

#Utility funciton to chenge the format of data into a more convenient and easy to use format

import pickle as pickle
pickle_file = 'reviews.pickle'
def data_to_pickle(scores, summaries):
    try:
        f = open(pickle_file, 'wb')
        save = {
            'scores': scores,
            'summaries': summaries,
        }
        pickle.dump(save, f, pickle.HIGHEST_PROTOCOL)
        f.close()
    except Exception as e:
        print ('Unable to save data to', pickle_file, ':', e)
        raise

data_to_pickle(scores, summaries)

#pull data from pickle
file = open('reviews.pickle', 'rb')
data = pickle.load(file)
scores, summaries = data['scores'],data['summaries']