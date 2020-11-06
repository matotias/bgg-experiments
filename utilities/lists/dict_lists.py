from typing import List, Dict, Any


def deduplicate_dict_list(dict_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [dict(t) for t in {tuple(sorted(d.items())) for d in dict_list}]