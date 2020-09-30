import keras
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from .generic_keras import _PlotLossesCallback


class PlotLossesCallback(_PlotLossesCallback, keras.callbacks.Callback):
    """Callback for tensorflow keras"""
    def __init__(self, **kwargs):
        # keras & tensorflow call @ tensorboard
        keras.callbacks.Callback.__init__(self)
        _PlotLossesCallback.__init__(self, **kwargs)
