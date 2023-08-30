#!/bin/bash
cd $SCRATCHDIR
git clone https://github.com/PiffTheSenpai/witt-gpt
cd witt-gpt
singularity shell --nv /cvmfs/singularity.metacentrum.cz/NGC/PyTorch\:21.05-py3.SIF 
pip install transformers huggingface_hub
python download.py
HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python train.py
HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python inference.py
cd EleutherAI/gpt-neox-20b
cp -r checkpoints /storage/brno2/home/tvrzj/
