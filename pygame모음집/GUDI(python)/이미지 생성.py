import requests
import base64


URL = "https://api.kakaobrain.com/v2/inference/karlo/t2i"
api_key = "64f852e9319a7f5ced55b93e2fd0fd83" 

# 이미지 생성 요청을 위한 파라미터 설정
headers = {
    "Authorization": f"KakaoAK {api_key}",
    "Content-Type": "application/json"
}

request_data = {
    "prompt": "cat",

    "negative_prompt" : "ugly",  
    "width": 512,  
    "height": 512,  
    "samples": 1,  
    "return_type": "base64_string"  
}

# API 요청

response = requests.post(URL, json=request_data, headers=headers)

if response.status_code == 200:
    response_data = response.json()
    images = response_data.get("images", [])

    for idx, image_info in enumerate(images):
        image_data = image_info.get("image")
        image_format = image_info.get("image_format", "webp")

        # Base64 디코딩하여 이미지 파일로 저장
        image_bytes = base64.b64decode(image_data)
        with open(f"generated_image_{idx + 1}.{image_format}", "wb") as image_file:
            image_file.write(image_bytes)
        
        print(f"Image {idx + 1} saved successfully!")

else:
    print("Error:", response.text)