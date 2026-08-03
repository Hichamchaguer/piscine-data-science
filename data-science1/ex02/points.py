import pandas as pd
import matplotlib.pyplot as plt

# Load data
train = pd.read_csv('../csv/Train_knight.csv')
test = pd.read_csv('../csv/Test_knight.csv')

# Split training data
sith = train[train['knight'] == 'Sith']
jedi = train[train['knight'] == 'Jedi']

# ============================================
# CREATE ONE FIGURE WITH 3 SUBPLOTS
# ============================================
fig, axes = plt.subplots(2, 2, figsize=(18, 6))

# ============================================
# PLOT 1: Empowered vs Stims (Training Data)
# ============================================
axes[0, 0].scatter(sith['Empowered'], sith['Stims'], 
                label='Sith', color='red', alpha=0.5)
axes[0, 0].scatter(jedi['Empowered'], jedi['Stims'], 
                label='Jedi', color='blue', alpha=0.5)
axes[0, 0].set_xlabel('Empowered')
axes[0, 0].set_ylabel('Stims')
axes[0, 0].set_title('1. Empowered vs Stims (Training)')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# ============================================
# PLOT 2: Push vs Deflection (Training Data ONLY)
# ============================================
axes[0, 1].scatter(sith['Push'], sith['Deflection'], 
                label='Sith', color='red', alpha=0.5)
axes[0, 1].scatter(jedi['Push'], jedi['Deflection'], 
                label='Jedi', color='blue', alpha=0.5)
axes[0, 1].set_xlabel('Push')
axes[0, 1].set_ylabel('Deflection')
axes[0, 1].set_title('2. Push vs Deflection (Training)')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)

# ============================================
# PLOT 3: Push vs Deflection (Test Data)
# ============================================
axes[1,0].scatter(test['Empowered'], test['Stims'], 
                label='knights', color='green', alpha=0.5)
axes[1,0].set_xlabel('Push')
axes[1,0].set_ylabel('Deflection')
axes[1,0].set_title('3. Push vs Deflection (Test Data)')
axes[1,0].legend()
axes[1,0].grid(True, alpha=0.3)


axes[1,1].scatter(test['Push'], test['Deflection'], 
                label='Knights', color='green', alpha=0.5)
axes[1,1].set_xlabel('Push')
axes[1,1].set_ylabel('Deflection')
axes[1,1].set_title('Push vs Deflection (Test Data)')
axes[1,1].legend()
axes[1,1].grid(True, alpha=0.3)

# ============================================
# ADJUST LAYOUT AND SHOW
# ============================================
plt.suptitle('Knight Data Analysis: Training vs Test Comparison', fontsize=16, y=1.02)
plt.tight_layout()
plt.show()