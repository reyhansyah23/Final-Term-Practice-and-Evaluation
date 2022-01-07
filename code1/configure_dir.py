import os
from google.colab import drive

drive.mount('/content/drive', force_remount=True)
path = "/content/drive/My Drive"

os.chdir("/content/drive/My Drive/UAS/code")

pip uninstall tensorflow

pip install tensorflow==1.13.2
