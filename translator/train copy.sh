#!/usr/bin/env bash

# Train a model on the EPO dataset  

fairseq-train data-bin \
--source-lang epo.g \
--target-lang epo.p \
--seed 20160615 \
--arch lstm \
--encoder-bidirectional \
--dropout 0.2 \
--lr .001 \
--max-update 800 \
--no-epoch-checkpoints \
--batch-size 3000 \
--clip-norm 1 \
--label-smoothing .1 \
--optimizer adam \
--clip-norm 1 \
--criterion label_smoothed_cross_entropy \
--encoder-embed-dim 256 \
--decoder-embed-dim 256 \
--encoder-layers 1 \
--decoder-layers 1