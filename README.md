# witt-gpt
Scripts to download, train and inference GPT-NeoX on a grid computing platform (or your own computer if you have the computing capacity) using the Hugging Face Python library.

## How to use:

Intended use is on Unix systems (hasn't been tested on Windows).

1. Clone this repository with and change working directory:

`git clone https://github.com/PiffTheSenpai/witt-gpt `

`cd witt-gpt`

2. Download Hugging Face's Transformers library + other dependencies if you don't have them:

`pip install transformers huggingface_hub`

 (optional) `pip install torch torchvision`

3. Run `download.py` to download the model:

`python download.py`

4. Specify your questions into `prompt.txt` file and run `inference.py` to generate your responses:


## Important links with settings explanations

In order to change settings, please change respective python script, ie: `inference.py` and `train.py`.

https://huggingface.co/docs/transformers/main/en/model_doc/gpt_neox

https://huggingface.co/docs/transformers/main_classes/tokenizer

https://huggingface.co/docs/transformers/main_classes/text_generation

https://huggingface.co/docs/transformers/main_classes/trainer

https://huggingface.co/docs/transformers/internal/generation_utils

—————————————————————————————————

## Explanations of parameters (generated with chatGPT, caution is advised):

### Inference:

    do_sample (bool, optional, defaults to False): This parameter determines whether the generation process uses sampling (randomly selecting the next token based on their probabilities) or greedy decoding (always selecting the most likely next token). When set to True, it uses sampling, which can introduce randomness and diversity in the generated text. When set to False, it uses greedy decoding, which might result in more deterministic and focused text.

    num_beams (int, optional, defaults to 1): The number of beams controls how many alternative sequences the model should consider during generation. A higher value (greater than 1) results in beam search, where the model explores multiple possible continuations and selects the best ones. This can lead to more coherent and contextually relevant outputs.

    num_beam_groups (int, optional, defaults to 1): This parameter works in conjunction with num_beams to divide the beams into groups. The purpose of using beam groups is to ensure diversity among different groups of beams, potentially leading to more varied and creative output.

    penalty_alpha (float, optional): This parameter affects the trade-off between model confidence and the degeneration penalty during contrastive search decoding. Contrastive search decoding aims to encourage diverse and informative responses. Adjusting this parameter can influence the balance between generating safe and creative responses.

    use_cache (bool, optional, defaults to True): Caching past key/values attentions from previous decoding steps can speed up the decoding process. However, in some cases, it might affect the quality of the generated text. Setting this parameter to False would result in the model not using the cached attentions, potentially leading to different or more varied outputs.

These parameters give you control over various aspects of text generation, including randomness, diversity, coherence, and speed. Depending on your specific use case and desired output, you can adjust these parameters to fine-tune the behavior of the model during text generation.

---

### Training: