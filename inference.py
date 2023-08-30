from transformers import AutoTokenizer, AutoModelForCausalLM, AutoConfig, GPTNeoXForCausalLM

#path = "EleutherAI/gpt-neo-125m"
path = "EleutherAI/gpt-neox-20b"

config = AutoConfig.from_pretrained(path)
model = AutoModelForCausalLM.from_pretrained(path).half().cuda()
tokenizer = AutoTokenizer.from_pretrained(path)

#prompt = open("./prompt.txt").readlines()
prompt = ["What is the gist of Wittgenstein's late philosophy?"]


for line in prompt:

    input_ids = tokenizer(line, return_tensors="pt").input_ids

    gen_tokens = model.generate(
        input_ids,
        do_sample=True,
        #num_beams=4,
        temperature=0.9, # default was 0.9
        max_new_tokens=200,
    )

    gen_text = tokenizer.batch_decode(gen_tokens)[0]
    
    open("./outputs.txt", "a").write(gen_text)

    print(gen_text)