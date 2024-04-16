import json


def load_from_jsonl(json_path):
    data = []
    with open(json_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    return data


def save_to_jsonl(data, json_path):
    with open(json_path, 'w', encoding='utf-8') as f:
        if isinstance(data, list):
            for sample in data:
                f.write(json.dumps(sample, ensure_ascii=False) + '\n')
        if isinstance(data, dict):
            for image, QAs in data.items():
                f.write(json.dumps({'image': image, 'QAs': list(QAs)}, ensure_ascii=False) + '\n')


def append_to_jsonl(sample, json_path):
    with open(json_path, 'a', encoding='utf-8') as f:
        f.write(json.dumps(sample, ensure_ascii=False) + '\n')
