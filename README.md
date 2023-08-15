# Bayesian machine learning in astronomy: Investigating and comparing methods

In this project, we'd like to compare the advantages and disadvantages of different methods for approximate Bayesian ML, while learning a lot about how to implement Bayesian ML methods in the process. Which have the best uncertainty properties? Which are the most practical? And how can we implement them in libraries like TensorFlow and PyTorch?

You can find more information about the project in the Google doc [here](https://docs.google.com/document/d/1vhYWhdmTzp7xzw0ISpkbWc5ozvJIVMqzucH9viglvrs/edit?usp=sharing).


## Available data
There are currently two available datasets:

* `curve`: a 1D function with a relatively intricate shape, 250 training points, and some noise (contributed by Emily)
* `stellar_spectra`: simulated stellar spectra with 100 data points each + parameters in a table such as $T_\text{eff}$ and $\log g$.