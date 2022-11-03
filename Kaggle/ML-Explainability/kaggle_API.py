import kaggle.api
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

# Download all files of a dataset
# Signature: dataset_download_files(dataset, path=None, force=False, quiet=True, unzip=False)
# api.dataset_download_files('avenn98/world-of-warcraft-demographics')

# download single file
# Signature: dataset_download_file(dataset, file_name, path=None, force=False, quiet=True)
api.dataset_download_file("mathan/fifa-2018-match-statistics", "FIFA 2018 Statistics.csv")
