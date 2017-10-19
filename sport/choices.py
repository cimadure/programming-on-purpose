import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
# from sklearn.feature_extraction import DictVectorizer
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics import classification_report
# from sklearn.pipeline import FeatureUnion
# from sklearn.pipeline import Pipeline

#class LinearRegression(LinearModel, RegressorMixin)
#ClassifierMixin

# League , Pool, team

class BasePlayer():#BaseEstimator, TransformerMixin):

    games_played = None
    goals = None
    assists = None
    points = None
    penalty_minutes = None

    wins = None
    losses = None
    ties = None

