python main_resample_bayes.py --dataset "MNIST" --cv_type "vgmm" --net_type "3conv3fc" --persist_conf_path "ignore_flat_rst_meta_persist_MNIST.py" # default debug False
python main_resample_bayes.py ---dataset "MNIST" -cv_type "rand" --net_type "3conv3fc" --persist_conf_path "ignore_flat_rst_meta_persist_MNIST.py" # default --debug False
#python refactor_main_Frequentist.py --cv_type "rand" --net_type "3conv3fc"   # default --debug False
#python refactor_main_Frequentist.py --cv_type "vgmm" --net_type "3conv3fc"  # default --debug False
python main_resample_bayes.py --dataset "MNIST" --cv_type "vgmm" --net_type "alexnet" --persist_conf_path "ignore_flat_rst_meta_persist_MNIST.py" # default debug False
python main_resample_bayes.py --dataset "MNIST" --cv_type "rand" --net_type "alexnet" --persist_conf_path "ignore_flat_rst_meta_persist_MNIST.py" # default --debug False
#python refactor_main_Frequentist.py --cv_type "rand" --net_type "alexnet"  # default --debug False
#python refactor_main_Frequentist.py --cv_type "vgmm" --net_type "alexnet"  # default --debug False
python main_resample_bayes.py --dataset "MNIST" --cv_type "vgmm" --net_type "lenet" --persist_conf_path "ignore_flat_rst_meta_persist_MNIST.py" # default debug False
python main_resample_bayes.py --dataset "MNIST" --cv_type "rand" --net_type "lenet" --persist_conf_path "ignore_flat_rst_meta_persist_MNIST.py" # default --debug False
#python refactor_main_Frequentist.py --dataset "MNIST" --cv_type "rand" --net_type "lenet"  # default --debug False
#python refactor_main_Frequentist.py --dataset "MNIST" --cv_type "vgmm" --net_type "lenet"  # default --debug False
