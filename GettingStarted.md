## Getting Started


#### Keras model:
[keras.ipynb](https://github.com/VisionBrain/realtimeplt/blob/master/examples/keras.ipynb) 
```python
%matplotlib inline

from keras.datasets import mnist
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Flatten, Dense, Activation

# raw keras
from livelossplot import PlotLossesKeras

# tensorflow.keras
# from livelossplot import PlotLossesKerasTF
```

#### PyTorch:
[pytorch.ipynb](https://github.com/VisionBrain/realtimeplt/blob/master/examples/pytorch.ipynb)
```python

import numpy as np
from sklearn.model_selection import train_test_split

import torch
from torch import nn
from torch import optim
from torch.utils.data import TensorDataset, DataLoader

from livelossplot import PlotLosses
```


#### Poutyne:

[poutyne.ipynb](https://github.com/VisionBrain/realtimeplt/blob/master/examples/poutyne.ipynb)
```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torch.nn.init import xavier_normal_

from torchvision import transforms
from torchvision.datasets.mnist import MNIST

from pkg_resources import parse_version
import poutyne
assert parse_version(poutyne.__version__) >= parse_version('0.4'), "Please update your Poutyne version."

from poutyne.framework import Model

from livelossplot import PlotLossesPoutyne
```

#### Matplotlib:
[matplotlib.ipynb](https://github.com/VisionBrain/realtimeplt/blob/master/examples/matplotlib.ipynb)
```python


%matplotlib inline

from time import sleep
from matplotlib import pyplot as plt
import numpy as np

from livelossplot import PlotLosses
from livelossplot.outputs import MatplotlibPlot
```


