#!/usr/bin/env bash

# Train a model on the EPO dataset  

fairseq-train data-bin \
--source-lang epo.g \
--target-lang epo.p \
--seed 20160615 \
--arch transformer \
--attention-dropout=0.1 \
--dropout 0.2 \
--lr .001 \
--batch-size 32 \
--max-update 800 \
--no-epoch-checkpoints \
--clip-norm 1 \
--label-smoothing .1 \
--optimizer adam \
--clip-norm 1 \
--criterion label_smoothed_cross_entropy \
--encoder-embed-dim 128 \
--decoder-embed-dim 128 \
--encoder-layers 1 \
--decoder-layers 1