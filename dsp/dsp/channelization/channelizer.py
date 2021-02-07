import typing

import numpy as np
from scipy import signal


class AnalysisChannelizer:
    """

    Channelization happens in two steps
        1. Polyphase filtering
        2. FFT
    """
    def __init__(self, num_subchannels: int, taps: np.ndarray, osr: int = 1):
        """Build the channelizer

        Args:
            num_subchannels: the amount of subchannels to split the input signal into
            taps: the prototype low pass filter
            osr: oversampling ratio
        """
        self.num_subchannels = num_subchannels
        self.osr = osr
        
        # Build polyphase filter bank taps
        if len(taps) % self.num_subchannels != 0:
            raise ValueError(f'Length of prototype filter should be a multiple of subchannel')
        
        self.taps = [
            taps[::self.num_subchannels]
            taps[1::self.num_subchannels]
        ]

    
    def channelize(self, input_samples: np.ndarray) -> typing.Any:
        """Channelizes an input signal
        
        Returns:
            A 2D np.ndarray with num_subchannels columns
        """
        # Input buffering (for sample rate changes)
        # For osr == 1, just group into num_subchannels groups
        # input_2d = np.reshape(input_samples, self.num_subchannels)

        # Use a polyphase filter bank on the input samples
        # scipy.signal.resample_poly won't work - we want the output of the
        # filterbanks, not the sum. 
        
        # More buffer rearrangement

        # FFT
        pass
    