import pandas as pd
import matplotlib.pyplot as plt
from flower_plot import flower_plot  # from the GitHub repo

# ---------- 1. Load pan-genome table ----------
# Adjust the file name if needed
counts = pd.read_csv("strain_pangenome_counts.tsv", sep="\t")

# Clean column names (remove leading/trailing spaces)
counts.columns = counts.columns.str.strip()

print("Columns in table:", list(counts.columns))

# Figure out which columns are which
# strain
if "strain" in counts.columns:
    strain_col = "strain"
else:
    raise ValueError(f"No 'strain' column found. Got: {counts.columns}")

# core
core_col_candidates = ["core", "n_core", "core_genes"]
core_col = next((c for c in core_col_candidates if c in counts.columns), None)
if core_col is None:
    raise ValueError(f"No core column found. Got: {counts.columns}")

# shell / dis / disp
shell_col_candidates = ["dis", "disp", "shell", "accessory"]
shell_col = next((c for c in shell_col_candidates if c in counts.columns), None)
if shell_col is None:
    raise ValueError(
        f"No shell/disp column found. Tried {shell_col_candidates}, got: {counts.columns}"
    )

# unique
unique_col_candidates = ["unique", "uniq"]
unique_col = next((c for c in unique_col_candidates if c in counts.columns), None)
if unique_col is None:
    raise ValueError(f"No unique column found. Got: {counts.columns}")

print(f"Using columns -> strain: {strain_col}, core: {core_col}, shell: {shell_col}, unique: {unique_col}")

# ---------- 2. Build genome_to_data dict ----------
genome_to_data = {}
cmap = plt.get_cmap("tab20")
n = len(counts)

for i, row in counts.iterrows():
    genome_name = str(row[strain_col])
    shell_genes = int(row[shell_col])
    unique_genes = int(row[unique_col])

    color = cmap(float(i) / max(1, n - 1))

    genome_to_data[genome_name] = {
        "color": color,
        "shell": shell_genes,
        "unique": unique_genes,
    }

# ---------- 3. Core genes ----------
# If all core values are same, this just picks that value
n_core = int(counts[core_col].mode()[0])
print("n_core used for plot:", n_core)

# ---------- 4. Draw flower & save SVG ----------
fig, ax = plt.subplots(figsize=(8, 8))

flower_plot(
    genome_to_data=genome_to_data,
    n_core=n_core,
    shell_color=(0.96, 0.80, 0.25),   # yellow shell ring
    core_color=(0.96, 0.55, 0.15),    # orange core
    alpha=0.95,
    rotate_shell=False,
    rotate_unique=False,
    rotate_genome=True,
    default_fontsize=8,
    core_fontsize=26,
    ax=ax,
)

ax.set_aspect("equal")
ax.axis("off")

plt.tight_layout()
plt.savefig("Erwinia_pangenome_flower_flowerplot.svg", format="svg")
plt.close()
print("Saved SVG: Erwinia_pangenome_flower_flowerplot.svg")


