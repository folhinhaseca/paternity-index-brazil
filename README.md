# Allele Frequency Analysis for Paternity Test Loci

This project consolidates and analyzes STR (Short Tandem Repeat) genotypic data used in paternity testing. The script reads multiple `.txt` files with individual STR data, removes technical replicates, and generates allele frequency charts per locus.

## 🚀 Purpose

- Merge genotypic data from multiple files.
- Remove technical duplicates.
- Calculate allele frequencies per genetic locus.
- Generate graphical visualizations of allele distributions.

## 🧰 Technologies & Libraries

- Python 3
- pandas
- matplotlib
- seaborn

## 📁 Expected `.txt` File Format

Each file should contain the following columns:

- `Indivíduo` (Individual)
- `Lócus` (Locus)
- `Alelo 1` (Allele 1)
- `Alelo 2` (Allele 2)

Files must be tab-separated (`.tsv`) and encoded in UTF-8.

## 📌 Notes
- The script processes multiple files and skips unreadable ones without stopping.

- Useful for population studies and STR panel validation.
