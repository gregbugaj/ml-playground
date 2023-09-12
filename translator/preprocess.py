import contextlib
import csv
# data was shuffled using `shuf` and split 80-10-10 using `split.py`
 
TRAIN = "epo_train.tsv"
TRAIN_G = "train.epo.g"
TRAIN_P = "train.epo.p"
 
DEV = "epo_dev.tsv"
DEV_G = "dev.epo.g"
DEV_P = "dev.epo.p"
 
TEST = "epo_test.tsv"
TEST_G = "test.epo.g"
TEST_P = "test.epo.p"


# Processes training data.
with contextlib.ExitStack() as stack:
    source = csv.reader(stack.enter_context(open(TRAIN, "r")), delimiter="\t")
    g = stack.enter_context(open(TRAIN_G, "w"))
    p = stack.enter_context(open(TRAIN_P, "w"))
    
    for graphemes, phones in source:
        print(" ".join(graphemes), file=g)
        print(phones, file=p)

# Processes development data.
with contextlib.ExitStack() as stack:
    source = csv.reader(stack.enter_context(open(DEV, "r")), delimiter="\t")
    g = stack.enter_context(open(DEV_G, "w"))
    p = stack.enter_context(open(DEV_P, "w"))
    for graphemes, phones in source:
        print(" ".join(graphemes), file=g)
        print(phones, file=p)        

# Processes test data.
with contextlib.ExitStack() as stack:
    source = csv.reader(stack.enter_context(open(TEST, "r")), delimiter="\t")
    g = stack.enter_context(open(TEST_G, "w"))
    p = stack.enter_context(open(TEST_P, "w"))
    for graphemes, phones in source:
        print(" ".join(graphemes), file=g)
        print(phones, file=p)