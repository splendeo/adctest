class FFTSignal(object):
    """a representation of a frequency-domain signal
    """

    def __init__(self, fft, dB = None, time_domain = None):
        """initialize an FFTSignal object

        fft: array of numeric values of the fft
        dB:  true when in dB units, false if raw amplitude
        time_domain: the original time-domain signal if available, None
            otherwise

            self.fft = fft
            self.dB  = dB
            self.time_domain = time_domain
        """

    def process_gain(self):
        """compute the process gain for a given number of samples

        returns: process gain (a number in dB)
        """

    def harmonic_peaks(self, max_peaks):
        """peak detector

        This auxiliary function computes an array of indices into the fft
        array, pointing to the positions of the first max_peaks most
        significant peaks

        max_peaks: integer (usually in a small range, < 10)

        returns: an array of at most  max_peak indices into 
            the fft.fft array
        """

    def noise_floor(self):
        """noise floor of a frequency-domain signal

        returns: the real value of the fft noise floor
        """

    def SFDR(self):
        """spurious free dynamic range

        returns: a real number
        """

    def SINAD(self):
        """signal to noise and distortion ratio

        returns: a real number
        """

    def THD(self):
        """total harmonic distortion

        fft: FFTSignal object
        returns: a real number
        """

    def SNR(self):
        """signal-to-noise ratio

        returns: a real number
        """

    def ENOB(self):
        """effective number of bits

        A direct function of the SINAD, relating both scalar values
        """
