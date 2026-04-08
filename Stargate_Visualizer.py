import matplotlib.pyplot as plt
import pandas as pd

# Data from Stargate Cluster v13.2
data = {
    'Entity': ['JPMorgan (JPM)', 'BNY Mellon (BK)', 'JPM Asset Mgmt (JEPQ)'],
    'Notional_Sales_Billion': [5.854, 1.471, 1.124]
}
df = pd.DataFrame(data)

plt.figure(figsize=(10, 6), facecolor='#f4f4f4')
colors = ['#004a99', '#002a5c', '#0072ce']
bars = plt.bar(df['Entity'], df['Notional_Sales_Billion'], color=colors, edgecolor='black')

plt.title('STARGATE CLUSTER: Institutional Liquidity Sink (April 8, 2026)', fontsize=14, fontweight='bold')
plt.ylabel('Notional USD (Billions)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Highlight the Truce Catalyst
plt.text(1, 6.2, 'BRENT CRASH: $94.36 (-13.5%)', color='red', fontweight='bold', ha='center', bbox=dict(facecolor='white', alpha=0.8))

plt.savefig('Stargate_Final_Report.png', dpi=300)
print("[SUCCESS] Report generated: Stargate_Final_Report.png")
