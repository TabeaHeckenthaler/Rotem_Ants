import numpy as np
from scipy.linalg import eigvals

with open('whatever.txt', 'r') as txt_file:
    out = txt_file.read()

trials = out.split('\n')

states = 'abcdefghij'

state_to_num = dict((s, i) for i, s in enumerate(states))

tot_states = len(states)

transfer_mat = np.zeros((tot_states,) * 2, float)
transfer_mat_2 = np.zeros((tot_states ** 2,) * 2, float)

for trial in trials:
    trial = trial.split(",")
    for i in range(len(trial) - 1):
        i, j = trial[i:i + 2]
        i = state_to_num[i]
        j = state_to_num[j]
        transfer_mat[i, j] += 1

    for i in range(len(trial) - 2):
        i, j, k = trial[i:i + 3]
        i = state_to_num[i]
        j = state_to_num[j]
        k = state_to_num[k]
        index1 = i*tot_states + j
        index2 = j*tot_states + k
        transfer_mat_2[index1, index2] += 1

transfer_mat /= np.sum(transfer_mat, 1)[..., np.newaxis]  # ??
transfer_mat_2 /= np.sum(transfer_mat_2, 1)[..., np.newaxis]  # ??

mat_eigvals   = sorted(eigvals(transfer_mat),   key=lambda z: np.abs(z))
mat_2_eigvals = sorted(eigvals(transfer_mat_2), key=lambda z: np.abs(z))

S = np.log(np.abs(mat_eigvals[-2])/np.abs(mat_2_eigvals[-2]))

print(S)
