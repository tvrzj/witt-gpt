# download modelu a ulozeni do lokalu
from transformers import AutoTokenizer, AutoModelForCausalLM

path = "EleutherAI/gpt-neox-20b"

tokenizer = AutoTokenizer.from_pretrained(path)
model = AutoModelForCausalLM.from_pretrained(path)

tokenizer.save_pretrained("./EleutherAI/gpt-neox-20b")
model.save_pretrained("./EleutherAI/gpt-neox-20b")

#ve vysledku predelat na download script pro muj natrenovany model


''' # nakonec ne, zjistil jsem ze je to jen jina metoda
# stazeni configu
from huggingface_hub import hf_hub_download

hf_hub_download(repo_id="bigscience/T0_3B", filename="config.json", cache_dir="./your/path/bigscience_t0")
'''