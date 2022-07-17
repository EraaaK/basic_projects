import matplotlib.pyplot as plt

fig, ax = plt.subplots()
circle = plt.Circle((0, 0), 0.64, color='white')
lbls = ['Aberto', 'Em Andamento', 'Finalizado', 'Reaberto']

ax.pie([15, 20, 65, 3],
       labels=lbls,
       autopct='%1.1f%%',
       pctdistance=.82)
ax.add_artist(circle)
ax.set_title('Tickets por Estado', fontsize=16)
plt.show()
