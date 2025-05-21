// convert ipynb to py
``` bash
jupyter nbconvert --to script system_ISLES2022_Transformer.ipynb
```

// add conda environment to jupyter notebook list of kernels
``` bash
conda activate adi_ani_tf
conda install ipykernel
python -m ipykernel install --user --name=adi_ani_tf --display-name "Python (adi_ani_tf)"
jupyter notebook
```
