import shutil
import time
import os
import numpy as np
from cmdstanpy import CmdStanModel

def main():
    thisdir = os.path.dirname(os.path.realpath(__file__))

    model_fname = f'{thisdir}/bernoulli.stan'
    output_dir = f'{thisdir}/output_'
    num_draws = 400000

    # remove the output directory if it exists
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    # Load the bernoulli model
    model = CmdStanModel(stan_file=model_fname)

    # Sample the posterior distribution conditioned on some data
    with Timer(label='fit', verbose=True):
        fit = model.sample(data={'N': 5, 'y': [0, 1, 0, 0, 0]}, output_dir=output_dir, iter_sampling=num_draws)

    # Report the average value of the theta parameter
    # (this is probably not theoretically correct, just trying to get familiar)
    with Timer(label='Load draws', verbose=True):
        draws = fit.draws() # First dimension is the draw index, second is the chain index, and third is the column index
    print(f'{draws.shape[0]} draws; {draws.shape[1]} chains')
    theta_draws = draws[:, :, 7] # 7th column is the theta
    print(np.mean(theta_draws))

class Timer:
    def __init__(self, *, label='', verbose=False):
      self._label = label
      self._start_time = None
      self._stop_time = None
      self._verbose = verbose

    def elapsed(self):
      if self._stop_time is None:
        return time.time() - self._start_time
      else:
        return self._stop_time - self._start_time

    def __enter__(self):
      self._start_time = time.time()
      return self

    def __exit__(self, exc_type, exc_value, exc_tb):
      self._stop_time = time.time()
      if self._verbose:
        print(f"Elapsed time time for {self._label}: {self.elapsed()} sec")

if __name__ == '__main__':
    main()