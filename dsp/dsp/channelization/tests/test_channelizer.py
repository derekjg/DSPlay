#!/usr/bin/env python
from functools import reduce

import numpy as np

def test_channelizer_64x64(channelizer):
    # Create input signal
    fs = 64e6
    freqs = np.arange(-32e6, 32e6, 1e6)
    amps = list(range(len(freqs)))
    w = 2 * np.pi * freqs
    t = np.arange(0, 1, 1/fs)
    signals = [amp * np.exp(1j * omega * t) for amp, omega, in zip(amps, w)]

    
    input_signal = reduce(lambda out, sig: out + sig, signals)
    
    channelized = channelize(input_signal)
    
    for id, subchannel in enumerate(channelized):
        # check each amplitude
        pass
