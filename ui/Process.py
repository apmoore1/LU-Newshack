import json


class Process:
    _file = ""
    def __init__(self, uri, threshold):
        f = open(_file)
        output = json.loads(f.read())
        f.close()

        relevant_uris = output[uri]
        language_dict = {}

        for rel_uri in relevant_uris:
            lang, sim = relevant_uris[rel_uri]
            if lang in language_dict:
                language_dict[lang].append((rel_uri,sim))
            else:
                language_dict = [(rel_uri,sim)]

        sorted_language_dict = {}

        for lang in language_dict:
            sorted_list = sorted(language_dict[lang], key=lambda item: item[1])
            sorted_language_dict[lang] = sorted_list
        return sorted_language_dict