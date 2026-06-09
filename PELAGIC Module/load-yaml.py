# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 13:02:05 2026

@author: Huffmaar

#Code prompte generated with aid from CHAT-GPT.

"""

import sys
import yaml
from linkml_runtime.utils.schemaview import SchemaView
#from linkml_runtime.loaders import yaml_loader


def load_yaml_raw(file_path):
    """
    Load YAML file using PyYAML (basic validation).
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        print("✅ YAML loaded successfully (basic parse)")
        return data
    except yaml.YAMLError as e:
        print(f" YAML parsing error: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f" File not found: {file_path}")
        sys.exit(1)


def load_linkml_schema(file_path):
    """
    Load YAML as a LinkML schema.
    """
    try:
        schema_view = SchemaView(file_path)
        print(f" LinkML schema loaded: {schema_view.schema.name}")
        return schema_view
    except Exception as e:
        print(f" Failed to load LinkML schema: {e}")
        sys.exit(1)


def inspect_schema(schema_view):
    """
    Print some useful schema details.
    """
    print("\n--- Schema Overview ---")
    print(f"Name: {schema_view.schema.name}")
    
    print("\nClasses:")
    for cls in schema_view.all_classes():
        print(f" - {cls}")
    
    print("\nSlots:")
    for slot in schema_view.all_slots():
        print(f" - {slot}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python load_linkml_yaml.py <schema.yaml>")
        sys.exit(1)

    file_path = sys.argv[1]

    # Step 1: Raw YAML validation
    load_yaml_raw(file_path)

    # Step 2: Load as LinkML schema
    schema_view = load_linkml_schema(file_path)

    # Step 3: Inspect schema contents
    inspect_schema(schema_view)


if __name__ == "__main__":
    main()