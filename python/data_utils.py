import pickle
import numpy as np
from scipy.io import loadmat

MODS = ['8PSK', 'AM-DSB', 'AM-SSB', 'BPSK', 'CPFSK', 'GFSK', 'PAM4', 'QAM16', 'QAM64', 'QPSK', 'WBFM']

def load_and_split_pickle(path):
    with open(path, 'rb') as f:
        d = pickle.load(f, encoding='latin1')
    
    snrs, mods = map(lambda j: sorted(list(set(map(lambda x: x[j], d.keys())))), [1, 0])
    X, lbl = [], []
    for mod in mods:
        for snr in snrs:
            X.append(d[(mod, snr)])
            for i in range(d[(mod, snr)].shape[0]):
                lbl.append((mod, snr))
    
    X = np.vstack(X)
    X = np.reshape(X, (-1, 2, 128, 1))
    
    # Simple 50/50 split logic
    n_examples = X.shape[0]
    train_idx = np.random.choice(range(0, n_examples), size=n_examples//2, replace=False)
    test_idx = list(set(range(0, n_examples)) - set(train_idx))
    
    # One-hot encoding helper
    def to_onehot(indices):
        categorical = np.zeros([len(indices), len(MODS)])
        categorical[np.arange(len(indices)), indices] = 1
        return categorical

    y_indices = [MODS.index(lbl[x][0]) for x in range(len(lbl))]
    y = to_onehot(y_indices)
    
    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]

def load_mat_signal(file_path):
    data_dict = loadmat(file_path)
    var_name = [k for k in data_dict.keys() if not k.startswith('_')][0]
    raw_signal = data_dict[var_name]
    # Normalize and expand dims for CNN
    input_data = np.expand_dims(raw_signal, axis=-1).astype('float32')
    input_data = input_data / (np.max(np.abs(input_data)) + 1e-9)
    return input_data