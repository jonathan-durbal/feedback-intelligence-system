# test_api.py - Test that your UT API works
import requests
import json
from config import AZURE_API_KEY, AZURE_ENDPOINT_URL, HEADERS, PARAMS, MODEL

def test_api():
    """Test UT Azure OpenAI API connection"""
    
    print("Testing UT Azure API connection...")
    print(f"Using model: {MODEL}")
    print(f"API Key starts with: {AZURE_API_KEY[:10]}...")
    
    # Simple test payload
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": "Respond with exactly: API is working!"}
        ],
        "max_tokens": 50,
        "temperature": 0
    }
    
    try:
        # Make the API call
        response = requests.post(
            AZURE_ENDPOINT_URL,
            headers=HEADERS,
            params=PARAMS,
            json=payload,
            timeout=30
        )
        
        # Check if successful
        response.raise_for_status()
        
        # Get the result
        result = response.json()
        message = result['choices'][0]['message']['content']
        
        print("\n✅ SUCCESS! Your UT Azure API is working!")
        print(f"API Response: {message}")
        print("\nYou're ready to start building your project! 🚀")
        return True
        
    except requests.exceptions.HTTPError as e:
        print(f"\n❌ HTTP ERROR: {e}")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        print("\nCheck:")
        print("1. Is your API key correct in config.py?")
        print("2. Has your UT API key expired?")
        return False
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        print("\nTroubleshooting:")
        print("1. Check your API key in config.py")
        print("2. Make sure you're connected to internet")
        print("3. Verify config.py is in the same folder as test_api.py")
        return False

if __name__ == "__main__":
    test_api()