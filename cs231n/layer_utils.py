from cs231n.layers import *
from cs231n.fast_layers import *


def affine_relu_forward(x, w, b):
  """
  Convenience layer that perorms an affine transform followed by a ReLU

  Inputs:
  - x: Input to the affine layer
  - w, b: Weights for the affine layer

  Returns a tuple of:
  - out: Output from the ReLU
  - cache: Object to give to the backward pass
  """
  a, fc_cache = affine_forward(x, w, b)
  out, relu_cache = relu_forward(a)
  cache = (fc_cache, relu_cache)
  return out, cache


def affine_relu_backward(dout, cache):
  """
  Backward pass for the affine-relu convenience layer
  """
  fc_cache, relu_cache = cache
  da = relu_backward(dout, relu_cache)
  dx, dw, db = affine_backward(da, fc_cache)
  return dx, dw, db


def affine_norm_relu_forward(x, w, b, gamma, beta, bn_param):
    """
    Forward pass for the affine-norm-relu convenience layer
    """
    a, fc_cache = affine_forward(x, w, b)
    b, norm_cache = batchnorm_forward(a, gamma, beta, bn_param)
    out, relu_cache = relu_forward(b)
    cache = (fc_cache, norm_cache, relu_cache)
    return out, cache

def affine_norm_relu_backward(dout, cache):
    """
    Backward pass for the affine-norm-relu convenience layer
    """
    fc_cache, norm_cache, relu_cache = cache
    
    dbn = relu_backward(dout, relu_cache)
    da, dgamma, dbeta = batchnorm_backward_alt(dbn, norm_cache)
    dx, dw, db = affine_backward(da, fc_cache)
    return dx, dw, db, dgamma, dbeta

def affine_norm_relu_dropout_forward(x, w, b, gamma, beta, bn_param, dropout_param):
    """
    Forward pass for the affine-norm-relu-dropout convenience layer
    """
    a, fc_cache = affine_forward(x, w, b)
    b, norm_cache = batchnorm_forward(a, gamma, beta, bn_param)
    r, relu_cache = relu_forward(b)
    out, dropout_cache = dropout_forward(r, dropout_param)
    cache = (fc_cache, norm_cache, relu_cache, dropout_cache)
    return out, cache

def affine_norm_relu_dropout_backward(dout, cache):
    """
    Backward pass for the affine-norm-relu-dropout convenience layer
    """
    fc_cache, norm_cache, relu_cache, dropout_cache = cache
    dr = dropout_backward(dout, dropout_cache)
    dbn = relu_backward(dr, relu_cache)
    da, dgamma, dbeta = batchnorm_backward_alt(dbn, norm_cache)
    dx, dw, db = affine_backward(da, fc_cache)
    return dx, dw, db, dgamma, dbeta

def conv_relu_forward(x, w, b, conv_param):
  """
  A convenience layer that performs a convolution followed by a ReLU.

  Inputs:
  - x: Input to the convolutional layer
  - w, b, conv_param: Weights and parameters for the convolutional layer
  
  Returns a tuple of:
  - out: Output from the ReLU
  - cache: Object to give to the backward pass
  """
  a, conv_cache = conv_forward_fast(x, w, b, conv_param)
  out, relu_cache = relu_forward(a)
  cache = (conv_cache, relu_cache)
  return out, cache


def conv_relu_backward(dout, cache):
  """
  Backward pass for the conv-relu convenience layer.
  """
  conv_cache, relu_cache = cache
  da = relu_backward(dout, relu_cache)
  dx, dw, db = conv_backward_fast(da, conv_cache)
  return dx, dw, db


def conv_relu_pool_forward(x, w, b, conv_param, pool_param):
  """
  Convenience layer that performs a convolution, a ReLU, and a pool.

  Inputs:
  - x: Input to the convolutional layer
  - w, b, conv_param: Weights and parameters for the convolutional layer
  - pool_param: Parameters for the pooling layer

  Returns a tuple of:
  - out: Output from the pooling layer
  - cache: Object to give to the backward pass
  """
  a, conv_cache = conv_forward_fast(x, w, b, conv_param)
  s, relu_cache = relu_forward(a)
  out, pool_cache = max_pool_forward_fast(s, pool_param)
  cache = (conv_cache, relu_cache, pool_cache)
  return out, cache


def conv_relu_pool_backward(dout, cache):
  """
  Backward pass for the conv-relu-pool convenience layer
  """
  conv_cache, relu_cache, pool_cache = cache
  ds = max_pool_backward_fast(dout, pool_cache)
  da = relu_backward(ds, relu_cache)
  dx, dw, db = conv_backward_fast(da, conv_cache)
  return dx, dw, db

