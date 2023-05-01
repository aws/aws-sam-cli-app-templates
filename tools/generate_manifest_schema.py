import json

schema = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
    }
}
with open("../manifest.json") as f:
    manifest = json.load(f)
    for runtime in manifest.keys():
        schema["properties"][runtime] = {
            "type": "array",
            "items": []
        }
        for template in manifest[runtime]:
            item = {
                "type": "object",
                "additionalProperties": False,
                "properties": {

                },
                "required": []
            }
            for key in template.keys():
                item["properties"][key] = {
                    "type": "string",
                    "enum": [
                        template[key]
                    ]
                }
                item["required"].append(key)
            schema["properties"][runtime]["items"].append(item)
        schema["properties"][runtime]["minItems"] = len(schema["properties"][runtime]["items"])
        schema["properties"][runtime]["maxItems"] = len(schema["properties"][runtime]["items"])
    with open("../manifest-schema.json", "w") as ff:
        json.dump(schema, ff)
