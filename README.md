# query-intent-classification
Classify queries using word2vec


word2vec download: (gzipped binary representation of words and vectors)

https://drive.google.com/uc?id=0B7XkCwpI5KDYNlNUTTlSS21pQmM&export=download

You can use the `gensim` library to read the model into memory and interact with it.

See `word2vec_jonathan` notebook.

query_cnn.py [-h] [--pretrained-embedding] [--num-embed NUM_EMBED]
                    [--gpus GPUS] [--kv-store KV_STORE]
                    [--num-epochs NUM_EPOCHS] [--batch-size BATCH_SIZE]
                    [--optimizer OPTIMIZER] [--lr LR] [--dropout DROPOUT]
                    [--disp-batches DISP_BATCHES] [--save-period SAVE_PERIOD]

query_cnn.py [-h] [--pretrained-embedding] [--num-embed NUM_EMBED]
                    [--gpus GPUS] [--kv-store KV_STORE]
                    [--num-epochs NUM_EPOCHS] [--batch-size BATCH_SIZE]
                    [--optimizer OPTIMIZER] [--lr LR] [--dropout DROPOUT]
                    [--disp-batches DISP_BATCHES] [--save-period SAVE_PERIOD]
