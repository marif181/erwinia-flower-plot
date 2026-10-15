## Erwinia Pangenome Flower Plot

Python script that draws a flower plot (core, shell, and strain-unique genes)
for Erwinia strains from a pan-genome summary table and saves it as SVG.

## Requirements
- Python 3.8+
- pandas, matplotlib
- `flower_plot.py` (plotting function, must be in the same folder as this script)

```bash
pip install pandas matplotlib
```

## Input
A tab-separated file named `strain_pangenome_counts.tsv`, one row per strain:

| strain   | core | dis | unique |
|----------|------|-----|--------|
| strain_A | 3200 | 850 | 120    |

Accepted column names (case-sensitive):
- strain: `strain`
- core: `core`, `n_core`, `core_genes`
- shell: `dis`, `disp`, `shell`, `accessory`
- unique: `unique`, `uniq`

The core gene count is taken as the most common value in the core column.

## Usage
```bash
python erwinia_flower_plot.py
```
Output: `Erwinia_pangenome_flower_flowerplot.svg`
