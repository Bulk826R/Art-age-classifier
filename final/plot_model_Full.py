import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['text.color'] = 'black'
matplotlib.rcParams['grid.color'] = 'grey'
matplotlib.rcParams['grid.linestyle'] = '--'
matplotlib.rcParams['grid.linewidth'] = 0.


data_dir = 'Full'
train_Loss = np.loadtxt(data_dir+'/train_Loss.txt')
test_Loss = np.loadtxt(data_dir+'/test_Loss.txt')
train_Acc = np.loadtxt(data_dir+'/train_Acc.txt')
test_Acc = np.loadtxt(data_dir+'/test_Acc.txt')

x = np.arange(len(train_Loss))

print('Max train acc = ', np.max(train_Acc))
print('Max test acc = ', np.max(test_Acc))

####

fig = plt.figure()
fig.set_size_inches(8, 14)

ax1 = fig.add_subplot(2, 1, 1)
ax1.plot(x, train_Loss, color = 'royalblue', alpha = 0.8, lw = 1.6, label = r'Training')
ax1.plot(x, test_Loss, color = 'crimson', alpha = 0.8, lw = 1.6, label = r'Validation')
ax1.set_xlabel(r'$\mathrm{Epoch}$', fontsize = 24, labelpad = 8)
ax1.set_ylabel(r'$\mathrm{Loss}$', fontsize = 24, labelpad = 8)
ax1.tick_params(labelsize = 18)
ax1.legend(loc = 'upper right', fontsize = 16, frameon = False, borderpad = 0.5)

ax2 = fig.add_subplot(2, 1, 2)
ax2.plot(x, train_Acc, color = 'darkturquoise', alpha = 0.8, lw = 1.6, label = r'Training')
ax2.plot(x, test_Acc, color = 'orange', alpha = 0.8, lw = 1.6, label = r'Validation')
ax2.set_xlabel(r'$\mathrm{Epoch}$', fontsize = 24, labelpad = 8)
ax2.set_ylabel(r'$\mathrm{Accuracy}$', fontsize = 24, labelpad = 8)
ax2.tick_params(labelsize = 18)
ax2.legend(loc = 'lower right', fontsize = 16, frameon = False, borderpad = 0.5)

fig.savefig(data_dir+'/Loss.pdf', dpi = 400, bbox_inches = 'tight')
plt.show()