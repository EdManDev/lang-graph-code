#!/usr/bin/env python3
"""Diagnostic script for ZhipuAI account issues"""

from zhipuai import ZhipuAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("ZHIPUAI_API_KEY")
client = ZhipuAI(api_key=api_key)

print("ZhipuAI Account Diagnostics")
print("=" * 50)
print(f"API Key: {api_key[:10]}...{api_key[-10:]}")
print()

# Check if we can make any API call at all
print("Testing basic API connectivity...")
try:
    # Try the most basic model call
    response = client.chat.completions.create(
        model="glm-3-turbo",
        messages=[{"role": "user", "content": "Hi"}],
        max_tokens=10,
    )
    print("✓ Basic API call successful")
    print(f"  Response: {response.choices[0].message.content}")
except Exception as e:
    error_str = str(e)
    print(f"✗ API call failed")

    # Parse the error
    if "429" in error_str:
        print("\n⚠️  Rate Limit/Quota Error (429)")
        print("This means:")
        print("  • Your account has hit the API rate limit")
        print("  • You may have exhausted your free quota")
        print("  • Billing might not be set up correctly")
        print("\n📋 Next steps:")
        print("  1. Visit https://open.bigmodel.cn/")
        print("  2. Check your account balance/quota")
        print("  3. Verify billing is set up")
        print("  4. Check available models in your console")

    elif "1211" in error_str:
        print("\n⚠️  Model Not Available (1211)")
        print("This means:")
        print("  • Your account doesn't have access to this model")
        print("  • The model name might be incorrect")
        print("\n📋 Next steps:")
        print("  1. Check what models are available in your account")
        print("  2. Visit https://open.bigmodel.cn/console/modelapi")
        print("  3. Verify your API key has the right permissions")

    elif "401" in error_str or "403" in error_str:
        print("\n⚠️  Authentication Error")
        print("This means:")
        print("  • Your API key is invalid or expired")
        print("  • The key doesn't have the right permissions")
        print("\n📋 Next steps:")
        print("  1. Regenerate your API key in the console")
        print("  2. Update your .env file with the new key")

    else:
        print(f"\n⚠️  Unknown Error: {error_str}")

print("\n" + "=" * 50)
print("💡 Quick Links:")
print("  • ZhipuAI Console: https://open.bigmodel.cn/")
print("  • Model API Docs: https://open.bigmodel.cn/console/modelapi")
print("  • API Keys: https://open.bigmodel.cn/console/apikeys")