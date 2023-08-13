import numpy as np
import pandas as pd

class DataCleaner:
    def __init__(self, **kwargs):
        pass
    def clean_card_data(self, df):
        df = df.dropna()
        # TODO: clean & reformat all columns
