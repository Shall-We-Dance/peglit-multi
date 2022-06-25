# pegLIT multithreads running script

[pegRNA Linker Identification Tool (pegLIT)](https://github.com/sshen8/peglit), a powerful tool developed by David Liu lab, can automatically identify non-interfering nucleotide linkers between a pegRNA and 3' motif.

Here we wrote some custom scripts to run peglit with high efficiency, using multithreads.

## Installation

Download this repository.

```
wget https://github.com/Shall-We-Dance/peglit/archive/refs/heads/main.zip
unzip main.zip
```

Install environment using conda, which is much easier than compiling from source code.

```
conda env create -f peglit.yaml
```

## Usage

Activate the conda environment.

```
conda activate peglit
```

Open `run_peglit.py` and specify `THREAD_NUM`, `INPUT_FILE`, `OUTPUT_FILE` and `MOTIF`, then just run the script.

```
python run_peglit.py
```

We also provided an example input `pegRNA_input_example.csv` in this repository, and the output of it should be the same as `pegRNA_result_example.csv`.


