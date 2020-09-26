<p >
    <br>
    <img src="https://github.com/VisionBrain/realtimeplt/blob/master/realtimeplt.png" width="300"/>
    <br>
</p>

![PyPI status](https://img.shields.io/pypi/status/realtimeplt.svg)
![MIT license - PyPI](https://img.shields.io/pypi/l/realtimeplt.svg)
![Python version - PyPI](https://img.shields.io/pypi/pyversions/realtimeplt.svg)

## Installation
```bash
pip install realtimeplt
```
[VisionBrain PyPi](https://pypi.org/project/realtimeplt/)

realtimeplt is a Python library made by VisionBrain which foucuses on getting the Live training loss plot in Jupyter Notebook for Keras, PyTorch and TensorFlow.Our main objective is to bring the ability to  visualize the data hyperparameters in real time.
![Animated fig for livelossplot tracking log-loss and accuracy](https://github.com/VisionBrain/realtimeplt/blob/master/realtimeplt.gif)


## Most Noticeable changes:
* Runs on the latest version of python
* Runs on the latest version of keras
* Runs on the latest version of pytorch
* Runs on the latest version of tensorflow

## Examples
- [keras.ipynb](https://github.com/VisionBrain/realtimeplt/blob/master/examples/keras.ipynb) - a Keras callback
- [pytorch.ipynb](https://github.com/VisionBrain/realtimeplt/blob/master/examples/pytorch.ipynb) - a bare API, as applied to PyTorch
- [2d_prediction_maps.ipynb](https://github.com/VisionBrain/realtimeplt/blob/master/examples/2d_prediction_maps.ipynb) - 2d prediction maps 
- [matplotlib.ipynb](https://github.com/VisionBrain/realtimeplt/blob/master/examples/matplotlib.ipynb) - data visualization
- [poutyne.ipynb](https://github.com/VisionBrain/realtimeplt/blob/master/examples/poutyne.ipynb) - a pytorch library

## Use 
The major dependency of realtimeplt is livelossplot
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

## Supported DataScience Libraries
Note*** Better results when used with Jupyter Notebook.

- Matplotlib
- Seaborn
- SciPy
- Bokeh

### from livelossplot import ...
`PlotLosses` for a generic API.
```{python}
plotlosses = PlotLosses()
plotlosses.update({'acc': 0.7, 'val_acc': 0.4, 'loss': 0.9, 'val_loss': 1.1})
plot.send()  # draw, update logs, etc
```
### from livelossplot.outputs import ...

Plots: `MatplotlibPlot`, `BokehPlot`
Loggers: `ExtremaPrinter` (to standard output), `TensorboardLogger`, `TensorboardTFLogger`, `NeptuneLogger`.
To use them, initialize PlotLosses with some outputs:
```{python}
plotlosses = PlotLosses(outputs=[MatplotlibPlot(), TensorboardLogger()])
```

## Note***
 [realtimeplt](https://pypi.org/project/realtimeplt/) is a faster and accurate version of [liveplot](https://github.com/PhilReinhold/liveplot) & in no manner VisionBrain is trying to copy liveplot.




