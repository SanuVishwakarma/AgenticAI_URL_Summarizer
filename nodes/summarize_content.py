from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)
summarizer_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer, device=-1)

def summarize_content(state):
    content = state["content"]
    text = " ".join(content['headings'] + content['paragraphs'][:10])[:1500]

    prompt = (
        "<|system|>You are an expert summarizer. Read the following website content carefully "
        "and create a clear, well-structured summary with important bullet points and key takeaways."
        "<|user|>Content:\n" + text + "<|assistant|>"
    )

    result = summarizer_pipeline(prompt, max_new_tokens=300, do_sample=True)[0]['generated_text']

    # Clean output: extract only what the assistant said
    if "<|assistant|>" in result:
        summary = result.split("<|assistant|>")[-1].strip()
    else:
        summary = result.strip()

    return {
        "url": state["url"],
        "summary": summary
    }
