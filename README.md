# batch_background_removal
This repository is automate script for multiple images background removal

# requirement
- anaconda or miniconda - [download](https://www.anaconda.com/download/success)
- miniconda is prefered for smaller files size

# simple usage
1. run `setup.bat` to setup environment (one time process, skip to second step if already done)
2. put all input images in `images\input\`
3. run `runall.bat` to start removing process
4. all processed images locate in `images\output\`

# setup
``` bash
# create conda environment
conda env create --file environment.yaml --yes --name background_remover 

```

# usage
``` bash
# activate conda environment
conda activate background_remover

# run python script
python remove.py

# deactivate conda environment
conda deactivate
```