import json

path = r'C:\Users\anura\.gemini\antigravity\brain\6dfb09c6-f09d-4b03-a587-1bda95fb6d32\.system_generated\logs\transcript.jsonl'
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        d = json.loads(line)
        print("STEP:", d.get('step_index'), "TYPE:", d.get('type'))
        if d.get('tool_calls'):
            for tc in d.get('tool_calls'):
                print("  Tool:", tc.get('name'))
        if d.get('content'):
            print("  Content:", str(d.get('content'))[:200])
