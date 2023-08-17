import openai

openai.api_key = "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"

model_engine = "davinci"

def generate_code(prompt):    
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=0.7,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.5
    )

    return response.choices[0].text.strip()

# 사용할 프롬프트 설정
prompt = "Please provide a detailed summary about the current state of global warming, its main causes and impacts, and effective solutions to address the issue."

# 함수 호출 및 결과 출력
generated_text = generate_code(prompt)
print(generated_text)
