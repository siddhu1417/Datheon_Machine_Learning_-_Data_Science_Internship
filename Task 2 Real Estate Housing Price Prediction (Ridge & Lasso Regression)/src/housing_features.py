"""Feature engineering used by the California housing regression pipelines."""

import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class HousingFeatures(BaseEstimator, TransformerMixin):
    """Add interpretable density ratios and income interaction features."""

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        data = X.copy()
        households = data["households"].replace(0, np.nan)
        rooms = data["total_rooms"].replace(0, np.nan)
        data["rooms_per_household"] = data["total_rooms"] / households
        data["bedrooms_per_room"] = data["total_bedrooms"] / rooms
        data["population_per_household"] = data["population"] / households
        data["income_x_rooms_per_household"] = data["median_income"] * data["rooms_per_household"]
        data["income_x_age"] = data["median_income"] * data["housing_median_age"]
        return data
