summary = {
    "Focus": "Scientific and Philosophical Exploration",
    "Themes": ["Exploration of dualities", "Interplay between science and philosophy", "Symbolism and material properties"],
    "Key Elements": [
        {"Concept": "Opposition", "Framework": ["Dualism", "Problem of Evil"]},
        {"Symbol": "Bearer of Light", "Significance": "Knowledge, enlightenment, new beginnings"},
        {"Symbol": "Number 8", "Significance": "Infinity, balance, cyclical processes"},
        {"Material": "Silicon", "Properties": "Photosensitivity, semiconductivity"},
        {"Material": "Copper", "Properties": "Electrical and thermal conductivity"},
        {"Material": "Quartz", "Properties": "Piezoelectricity, interaction with light and vibration"},
        {"Concept": "Cold Light", "Interpretation": "Subtle form of energy or illumination"},
        {"Concept": "Astral Plane", "Description": "Intermediate realm in philosophical and esoteric thought"},
    ],
    "Hypothetical Application": "A theoretical device ('8 tunnel') using copper, quartz, silicon, and light, shaped by the number 8, to potentially bridge divides between realities.",
    "Disclaimer": "The concepts discussed are theoretical and speculative and should not be taken as scientific or medical advice. Consult professionals for such matters."
}

def print_summary(data, indent=0):
    for key, value in data.items():
        print('  ' * indent + f"{key}:")
        if isinstance(value, dict):
            print_summary(value, indent + 1)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    print_summary(item, indent + 1)
                else:
                    print('  ' * (indent + 1) + f"- {item}")
        else:
            print('  ' * (indent + 1) + f"- {value}")

print("Summary of the Conversation (Scientific/Philosophical Focus):")
print_summary(summary)