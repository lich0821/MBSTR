# -*- coding: utf-8 -*-


from .base import AbstractDataset

import pandas as pd


class OttoDataset(AbstractDataset):
    @classmethod
    def code(cls):
        return "otto"

    def load_df(self):
        folder_path = self._get_rawdata_root_path()
        file_path = folder_path.joinpath("otto.txt")
        df = pd.read_csv(file_path, sep="\t", header=None)
        df.columns = ["uid", "sid", "timestamp", "behavior"]
        return df
