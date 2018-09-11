from model.data_utils import Dataset
from model.models import HANNModel
from model.config import Config
import argparse
import os

parser = argparse.ArgumentParser()

def main():
    # create instance of config
    config = Config(parser)

    # build model
    model = HANNModel(config)
    model.build()
    if config.restore:
        model.restore_session("results/test/model.weights/") # optional, restore weights

    # create datasets
    dev   = Dataset(config.filename_dev, config.processing_word,
                    config.processing_tag, config.max_iter)
    train = Dataset(config.filename_train, config.processing_word,
                    config.processing_tag, config.max_iter)
    test  = Dataset(config.filename_test, config.processing_word,
                    config.processing_tag, config.max_iter)

    # train model
    model.train(train, dev)

    # evaluate model
    model.restore_session(config.dir_model)
    metrics = model.evaluate(test)

    with open(os.path.join(config.dir_output, 'test_results.txt'), 'a') as file:
        file.write('{}\n'.format(metrics['classification-report']))
        file.write('{}\n'.format(metrics['confusion-matrix']))
        file.write('{}\n\n'.format(metrics['weighted-f1']))

if __name__ == "__main__":
    main()
