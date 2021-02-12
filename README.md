## Installing cmdstan

Followed these instructions: https://cmdstanpy.readthedocs.io/en/v0.9.67/installation.html#function-install-cmdstan

First installed cmdstanpy and a couple optional packages:

```
pip install --upgrade cmdstanpy tqdm ujson
```

Then installed cmdstan via cmdstanpy:

```
install_cmdstan
```

This downloaded and built cmdstan-2.26.0 in ~/.cmdstan

I then verified that this binary ran successfully:

```
> ~/.cmdstan/cmdstan-2.26.0/bin/stanc --version
stanc3 v2.26.0 (Unix)
```

## Usage tutorial

Followed this tutorial: https://cmdstanpy.readthedocs.io/en/v0.9.67/hello_world.html#bayesian-estimation-via-stan-s-hmc-nuts-sampler

And created this example: [./examples/hello_bernoulli](./examples/hello_bernoulli)
