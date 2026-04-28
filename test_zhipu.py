#!/usr/bin/env python3
"""Test script to check ZhipuAI API key and available models"""

from zhipuai import ZhipuAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("ZHIPUAI_API_KEY")
if not api_key:
    print("❌ ZHIPUAI_API_KEY not found in environment variables")
    print("Please check your .env file")
    exit(1)

print(f"✓ API Key found: {api_key[:10]}...{api_key[-10:]}")

client = ZhipuAI(api_key=api_key)

# Common ZhipuAI models to test
models_to_test = [
    "glm-3-turbo",
    "glm-4",
    "glm-4-flash",
    "glm-4-plus",
    "glm-4-air",
    "chatglm3-6b",
]

print("\nTesting available models:")
print("-" * 50)

for model in models_to_test:
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": "test"}],
        )
        print(f"✓ {model:15s} - Available")
    except Exception as e:
        error_msg = str(e)
        if "1211" in error_msg:  # Model doesn't exist error
            print(f"✗ {model:15s} - Not available")
        else:
            print(f"✗ {model:15s} - Error: {error_msg[:50]}")

print("\n" + "=" * 50)
print("If no models are available, check:")
print("1. Your API key is correct in the .env file")
print("2. Your account has API access enabled")
print("3. You have available credits/quota")