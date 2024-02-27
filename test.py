import sys
import anthropic

def main(api_key):
    client = anthropic.Anthropic(api_key=api_key)
    message = client.messages.create(
        model="claude-2.1",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "Hello, Claude"}
        ]
    )
    print(message.content)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <API_KEY>")
        sys.exit(1)
    api_key = sys.argv[1]
    main(api_key)
