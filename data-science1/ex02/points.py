import pandas as pd
import matplotlib.pyplot as plt



train = pd.read_csv('Train_Knight.csv')
test = pd.read_csv('Test_Knight.csv')


sith = train[train['knight'] == 'Sith']
jedi = train[train['knight'] == 'Jedi']

# plt.figure(figsize=(10, 5))
# plt.scatter(sith['Empowered'], sith['Stims'], label='Sith', color='red', alpha=0.2)
# plt.scatter(jedi['Empowered'], jedi['Stims'], label='Jedi', color='blue', alpha=0.5)
# plt.xlabel('Empowered')
# plt.ylabel('Stims')
# plt.legend()
# plt.show()
# plt.close()

# plt.figure(figsize=(10, 5))
# plt.scatter(train['Push'], train['Deflection'], label='Sith', color='red', alpha=0.5)
# plt.scatter(test['Push'], test['Deflection'], label='Jedi', color='blue', alpha=0.5)
# plt.xlabel('Push')
# plt.ylabel('Deflection')
# plt.legend()
# plt.show()
# plt.close()

plt.figure(figsize=(10, 5))
plt.scatter(sith['Push'], sith['Deflection'], label='Knight', color='green', alpha=0.5)
plt.scatter(jedi['Push'], jedi['Deflection'], color='green', alpha=0.5)
plt.xlabel('Push')
plt.ylabel('Stims')
plt.legend()
plt.show()
plt.close()