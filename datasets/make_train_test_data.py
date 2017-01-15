from raw_process import make_train_data
from raw_process import make_test_data
for i in range(0, 10, 1):
    make_train_data("dataset"+str(i)+"/train/", "dataset"+str(i)+"/224_train/", 224)
    make_test_data("dataset"+str(i)+"/test/", "dataset"+str(i)+"/224_test/", 224)
    make_train_data("dataset"+str(i)+"/train/", "dataset"+str(i)+"/256_train/", 256)
    make_test_data("dataset"+str(i)+"/test/", "dataset"+str(i)+"/256_test/", 256)
    print("Dataset " + str(i) + " generated\n")
