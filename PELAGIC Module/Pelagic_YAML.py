# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 13:53:54 2026

@author: huffmaar
Generated via Umich Chat-GPT
SEA-CDM Auto Generator
Generates:
  1. SQL DDL statements
  2. SQLAlchemy ORM classes
"""

from sqlalchemy import (
    Column, String, Integer, Float, Text,
    ForeignKey, DateTime
)
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()


# ----------------------------
# YAML-derived schema as dict
# ----------------------------

SEA_SCHEMA = {
    
    "SEACDMClass": {
        "abstract": True,
        "attributes": {
            "id": "string",
            "entity_type": "string",
            "reference_source_id": "string",
            "reference_source": "string",
            "comments": "string"
        },
        "relationships": {}
    },
    "Study": {
        "extends": "SEACDMClass",
        "attributes": {
            "study_type": "string",
            "study_focus": "string",
            "study_keywords": "string",
            "study_name": "string",
            "study_description": "string"
        },
        "relationships": {}
    },

    "Documentation": {
        "extends": "SEACDMClass",
        "attributes": {
            "documentation_type": "string",
            "documentation_file_access": "string",
            "documentation_reference_source": "string",
            "document_citation": "string",
            "documentation_citation_style": "string",
            "creator_id": "string",
            "creator_id_type": "string",
            "creator_role": "string",
            "document_name": "string",
            "documentation_reference_id": "string"
        },
        "relationships": {
            "study_id": "Study"
        }
    },

    "Experiment": {
        "extends": "SEACDMClass",
        "attributes": {
            "experiment_type": "string",
            "experiment_control": "string",
            "experiment_subject": "string"
        },
        "relationships": {
            "study_id": "Study",
            "documentation_id": "Documentation"
        }
    },

    "Group": {
        "extends": "SEACDMClass",
        "attributes": {
            "subject_group_type": "string",
            "sample_group_type": "string",
            "composition": "string",
            "group_size": "integer",
            "min_age": "float",
            "min_age_unit": "string",
            "max_age": "float",
            "max_age_unit": "string"
        },
        "relationships": {
            "experiment_id": "Experiment"
        }
    },
    
    "Analysis":{
        "extends": "SEACDMClass",

        "attributes": {
        "analysis_type": "string",
        "analysis_input": "string",
         "analysis_data": "string",
         "parameters": "string",
         "hyperparameters": "string",
         "reference_id": "string",
          "reference_source": "string",
          "reference_source_id": "string",
          },
        "relationships": {
          "group_id": "Group",
          "experiment_id": "Experiment"
          }
            }
        },

"Subject": {
        "extends": "SEACDMClass",

  attributes:{
    "age": "number"
    "sex": "string"
    "subject_type": "string"
    "species": "string"
    "race": "string"
    "ethnicity": "string"
    "strain": "string"
    "reference_source_id": "string"
    "reference_source": "string"}
  relationships:{
    "group_id": "Group"
    "experiment_id": "Experiment"}
},

Group:
  extends: SEACDMClass

  attributes:
    "subject_group_type": string
    "sample_group_type": string
    "composition": string
    "group_size": integer
    "min_age": number
    "min_age_unit": string
    "max_age": number
    "max_age_unit": string
    "reference_source_id": string
    "reference_source": string
  relationships:
    "experiment_id": Experiment

Intervention:{
  extends: SEACDMClass

  attributes:
    "material": string
    "intervention_time": string
    "dose": string
    "route": string
    "intervention_type": string
    "reference_source_id": string
    "reference_source": string
  relationships:
    "experiment_id": Experiment
    "subject_id": Subject
    },
    
Sample:
  extends: SEACDMClass

  attributes:
    collection: string
    collection_time: string
    biosample_source: string
    experimental_sample_type: string
  relationships:
    experiment_id: Experiment
    subject_id: Subject
    group_id: Group

Occurrence:
  extends: SEACDMClass
  attributes:
    occurrence: string
    occurrence_type: string
    occurrence_severity: string
    occurrence_onset: string
    occurrence_end: string
  relationships:
    subject_id: Subject

Ontology:
  extends: SEACDMClass
  attributes:
    ontology_name: string
    ontology_IRI: string
    ontology_code: string
  relationships:
    documentation_id: Documentation

Material:
  extends: SEACDMClass
  attributes:
    material_name: string
    material_type: string
    supplier: string
  relationships: {}
    


# ----------------------------
# Type Mapping
# ----------------------------

def map_sql_type(dtype):
    return {
        "string": "TEXT",
        "integer": "INTEGER",
        "float": "FLOAT"
    }.get(dtype, "TEXT")


def map_sqla_type(dtype):
    return {
        "string": Text,
        "integer": Integer,
        "float": Float
    }.get(dtype, Text)


# ----------------------------
# Generate SQL DDL
# ----------------------------

def generate_sql(schema):
    ddl_statements = []

    for class_name, config in schema.items():
        if config.get("abstract"):
            continue

        columns = []
        columns.append("id TEXT PRIMARY KEY")

        # inherited attributes
        base_attrs = schema["SEACDMClass"]["attributes"]

        for attr, dtype in base_attrs.items():
            if attr != "id":
                columns.append(f"{attr} {map_sql_type(dtype)}")

        # own attributes
        for attr, dtype in config["attributes"].items():
            columns.append(f"{attr} {map_sql_type(dtype)}")

        # relationships
        for rel, target in config["relationships"].items():
            columns.append(f"{rel} TEXT REFERENCES {target}(id)")

        ddl = f"CREATE TABLE {class_name} (\n  " + ",\n  ".join(columns) + "\n);"
        ddl_statements.append(ddl)

    return "\n\n".join(ddl_statements)


# ----------------------------
# Generate ORM Classes
# ----------------------------

def generate_orm_classes(schema):
    classes = {}

    class SEACDMClass(Base):
        __abstract__ = True

        id = Column(String, primary_key=True)
        entity_type = Column(String)
        reference_source_id = Column(String)
        reference_source = Column(String)
        comments = Column(Text)

    classes["SEACDMClass"] = SEACDMClass

    for class_name, config in schema.items():
        if config.get:
            next()

