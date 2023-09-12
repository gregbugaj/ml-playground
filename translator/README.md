#
The TSV is shuffled using shuf and then split into three TSV files: an 80% training set, a 10% development set, and a 10% test set using a Python script

```shell

python  split.py \
--seed 103 \
--input_path epo.tsv \
--train_path epo_train.tsv \
--dev_path epo_dev.tsv \
--test_path epo_test.tsv

```


The generated files are now ready for pre-processing in Fairseq:

```shell

fairseq-preprocess \
--source-lang epo.g \
--target-lang epo.p \
--trainpref train \
--validpref dev \
--testpref test \
--tokenizer space \
--thresholdsrc 2 \
--thresholdtgt 2

```

This pre-processing creates a folder called data-bin with binaries and a log file that provides the number of tokens found.  We can now start the training:

```shell

fairseq-train \
--data-bin \
--source-lang epo.g \
--target-lang epo.p \
--encoder-bidirectional \
--seed 20160615 \
--arch lstm \
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
--encoder-embed-dim 128 \  
--decoder-embed-dim 128 \  
--encoder-layers 1 \
--decoder-layers 1

```


To determine how well each model is doing, we use fairseq-generate that provides us an error analysis that details where our model came up short.

```shell

fairseq-generate data-bin \
    --source-lang epo.g \
    --target-lang epo.p \
    --path checkpoints/checkpoint_best.pt \
    --gen-subset valid \
    --beam 8  > predictions-attention.txt
    
```

The rows in predictions.txt are Source, Target, Hypothesis (tokenized, meaning any punctuation symbols in a project with sentences would be space-separated), and Detokenized (not broken into separate linguistic units).  The number before the hypothesis is the log-probability of this hypothesis.  For our project, if the Target matches the Hypothesis, the model has predicted correctly.




## References

https://journal.code4lib.org/articles/17038#note14