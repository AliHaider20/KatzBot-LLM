import streamlit as st
from transformers import AutoTokenizer, pipeline

# model_id = "neuralmagic/OpenHermes-2.5-Mistral-7B-pruned50-quant-ds"
model_id = "mistralai/Mistral_Instruct_Latest"

tokenizer = AutoTokenizer.from_pretrained(model_id)
tokenizer.pad_token = tokenizer.eos_token

pipe = pipeline(task="text-generation", model=model_id, tokenizer=tokenizer, max_length=200, trust_remote_code=True, low_cpu_mem_usage=True)

st.title("Chat Interface")

system_message = "Answer the question truthfully and to the point: "

query = st.text_input("User Query:")
result = pipe(system_message + f"{query}")[0]['generated_text']

st.text_area("Generated Response:", result)
