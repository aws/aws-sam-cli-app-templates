# script to generate the manifest file schema.
# it generates the schema from the current manifest file. It creates a detailed schema to make sure that we can only
# remove runtimes from the manifest file, but could not add new one, add/remove runtime templates, or change any
# property values.

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
                # this property makes sure that we could add new attributes for the templates
                "additionalProperties": False,
                "properties": {

                },
                "required": []
            }
            for key in template.keys():
                item["properties"][key] = {
                    "type": "string",
                    # this property makes sure that we could not change any attribute value
                    "enum": [
                        template[key]
                    ]
                }
                # this property makes sure that we could not remove any of the existing attributes for the templates
                item["required"].append(key)
            schema["properties"][runtime]["items"].append(item)
        # these properties make sure that we could not add new templates to any runtime.
        schema["properties"][runtime]["minItems"] = len(schema["properties"][runtime]["items"])
        schema["properties"][runtime]["maxItems"] = len(schema["properties"][runtime]["items"])
    with open("../manifest-schema.json", "w") as ff:
        json.dump(schema, ff)
