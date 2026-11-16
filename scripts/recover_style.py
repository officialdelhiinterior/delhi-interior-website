import json

path = r'C:\Users\anura\.gemini\antigravity\brain\5a0cf5a8-7652-4678-98dd-d247f98f1178\.system_generated\logs\transcript.jsonl'
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        d = json.loads(line)
        idx = d.get('step_index')
        if idx in [2103, 2186]:
            for c in d.get('tool_calls', []):
                if c.get('name') == 'write_file' and 'generate_master_style' in str(c.get('args')):
                    content = c['args']['Content']
                    out_name = f'scripts/recovered_style_{idx}.py'
                    with open(out_name, 'w', encoding='utf-8') as out:
                        out.write(content)
                    print(f"Step {idx} written to {out_name}, size: {len(content)}")
