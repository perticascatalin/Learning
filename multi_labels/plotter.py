import pickle
import matplotlib.pyplot as plt

X = []
for step in range(100, 4001, 100):
	X.append(step)

ml_losses = pickle.load(open('./pickles/ml_losses.p', 'rb'))
ml_train_accs = pickle.load(open('./pickles/ml_train_accs.p', 'rb'))
ml_val_accs = pickle.load(open('./pickles/ml_val_accs.p', 'rb'))

co_losses = pickle.load(open('./pickles/co_losses.p', 'rb'))
co_train_accs = pickle.load(open('./pickles/co_train_accs.p', 'rb'))
co_val_accs = pickle.load(open('./pickles/co_val_accs.p', 'rb'))

plt.xlabel('step')
plt.plot(X, ml_losses, X, ml_train_accs, X, ml_val_accs,
	X, co_losses, X, co_train_accs, X, co_val_accs)
plt.legend(['multi-label loss', 'multi-label train acc', 'multi-label val acc', 'combo loss', 'combo train acc', 'combo val acc'])
#plt.show()
plt.savefig('multi_label_vs_combo.png')