import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

# Stargate Ingest: April 8, 2026 Close (Hormuz Truce Inflection)
metrics = {
    'Asset': ['JPMorgan (JPM)', 'BNY Mellon (BK)', 'JPM Asset Mgmt (JEPQ)'],
    'Notional_USD_Billion': [5.8549, 1.4717, 1.1249],
    'Volume_Millions': [19.01, 12.05, 19.70],
    'Status': ['Front-Running', 'Custodial Anchor', 'Yield Capture']
}

df = pd.DataFrame(metrics)

plt.style.use('dark_background')
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plotting Notional Data
colors = ['#0056b3', '#002d5a', '#007bff']
bars = ax1.bar(df['Asset'], df['Notional_USD_Billion'], color=colors, alpha=0.8)
ax1.set_ylabel('Notional Volume (Billions USD)', color='white', fontsize=12)
ax1.set_ylim(0, 7)

# Annotations for April 8, 2026
plt.title('STARGATE CLUSTER: Institutional Liquidity Mapping (v13.2)', fontsize=16, fontweight='bold', pad=20)
ax1.annotate('BRENT CRASH: $94.53\nCeasefire Confirmed', xy=(0.5, 6.5), xytext=(1.5, 6.5),
             arrowprops=dict(facecolor='red', shrink=0.05), fontsize=10, color='red', fontweight='bold', ha='center')

plt.tight_layout()
plt.savefig('/home/laurobeck/AzureSQl/Stargate_Final_Telemetry.png', dpi=300)
print(f"[SUCCESS] Stargate Telemetry Materialized at {datetime.now()}")
