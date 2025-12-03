import os, json
from typing import Dict, Any

OPENAI_AVAILABLE = False
try:
    import openai
    OPENAI_AVAILABLE = True
except Exception:
    OPENAI_AVAILABLE = False

def _local_template(summary: Dict[str,Any]) -> str:
    lines = []
    lines.append(f"Rows: {summary.get('rows')}, Columns: {summary.get('cols')}." )
    if 'numeric_stats' in summary and summary['numeric_stats']:
        lines.append(f"Found {len(summary['numeric_stats'].keys())} numeric columns.")
    for k in ['impressions','clicks','spend','revenue']:
        if k in summary:
            kp = summary[k]
            lines.append(f"{k.title()}: sum={kp['sum']}, mean={kp['mean']}, max={kp['max']}")
    return '\n'.join(lines)

def generate_narrative(summary: Dict[str,Any], use_llm: bool=False) -> str:
    if use_llm and OPENAI_AVAILABLE and os.getenv('OPENAI_API_KEY'):
        prompt = ("You are an analyst. Given the following JSON summary, produce a 3-5 sentence executive summary."+"\n\n"+json.dumps(summary, default=str))
        openai.api_key = os.getenv('OPENAI_API_KEY')
        try:
            resp = openai.ChatCompletion.create(
                model='gpt-4o' if hasattr(openai,'gpt') else 'gpt-4o-mini',
                messages=[{'role':'user','content':prompt}],
                max_tokens=250,
                temperature=0.2
            )
            if 'choices' in resp and resp['choices']:
                return resp['choices'][0]['message']['content'].strip()
            return str(resp)
        except Exception as e:
            return f"LLM error: {e}\n\n" + _local_template(summary)
    return _local_template(summary)
