import math
from stock_volatility import stock_vol
class stock_options():
    def __init__(self, S0, K, r, T, N, prm):
        self.S0 = S0 # stock price
        self.K = K #strike price
        self.r = r #risk free intereset rate
        self.T = T # time per year
        self.N = N # no of iteration
        self.tk = prm.get('tk', None) # ticker label
        self.start = prm.get('start', None) # start date
        self.end = prm.get('end', None) #end date
        self.div = prm.get('div', 0) #dividend
        self.is_calc = prm.get('is_calc', False)
        self.use_garch = prm.get('use_garch', False)
        self.vol = stock_vol(self.tk, self.start, self.end) # volatility
        if self.is_calc:
            if self.use_garch:
                self.sigma = self.vol.garch_sigma()
            else:
                self.sigma = self.vol.mean_sigma()
        else:
             self.sigma = prm.get('sigma', 0)
        self.is_call = prm.get('is_call', True)
        self.eu_option = prm.get('eu_option', True)
        self.dt = T/float(N)
        self.df = math.exp(-(r-self.div)*self.dt)