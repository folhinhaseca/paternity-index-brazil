{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "0ab574ad",
   "metadata": {},
   "source": [
    "# Allele Frequency Analysis for Paternity Test Loci\n",
    "\n",
    "This project consolidates and analyzes STR (Short Tandem Repeat) genotypic data used in paternity testing. The script reads multiple `.txt` files with individual STR data, removes technical replicates, and generates allele frequency charts per locus.\n",
    "\n",
    "## 🚀 Purpose\n",
    "\n",
    "- Merge genotypic data from multiple files.\n",
    "- Remove technical duplicates.\n",
    "- Calculate allele frequencies per genetic locus.\n",
    "- Generate graphical visualizations of allele distributions.\n",
    "\n",
    "## 🧰 Technologies & Libraries\n",
    "\n",
    "- Python 3\n",
    "- pandas\n",
    "- matplotlib\n",
    "- seaborn\n",
    "\n",
    "## 📁 Expected `.txt` File Format\n",
    "\n",
    "Each file should contain the following columns:\n",
    "\n",
    "- `Indivíduo` (Individual)\n",
    "- `Lócus` (Locus)\n",
    "- `Alelo 1` (Allele 1)\n",
    "- `Alelo 2` (Allele 2)\n",
    "\n",
    "Files must be tab-separated (`.tsv`) and encoded in UTF-8.\n",
    "\n",
    "## 📌 Notes\n",
    "- The script processes multiple files and skips unreadable ones without stopping.\n",
    "\n",
    "- Useful for population studies and STR panel validation."
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
