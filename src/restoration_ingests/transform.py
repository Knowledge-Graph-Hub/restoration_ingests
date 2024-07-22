import uuid  # For generating UUIDs for associations

from biolink_model.datamodel.pydanticmodel_v2 import *  # Replace * with any necessary data classes from the Biolink Model
from koza.cli_utils import get_koza_app

koza_app = get_koza_app("sevilleja_transform")

while (row := koza_app.get_row()) is not None:
    # Code to transform each row of data
    # For more information, see https://koza.monarchinitiative.org/Ingests/transform
    entity_a = Entity(
        id=f"plot:{row['Plot']}",
        name=row['Plot'],
        category=["biolink:Entity"],
    )
    entity_b = Entity(
        id=f"treat:{row['treat']}",
        name=row['treat'],
        category=["biolink:Entity"],
    )
    association = Association(
        id=str(uuid.uuid1()),
        subject=row['Plot'],
        predicate="plot_received_treatment",
        object=row['treat'],
        subject_category="SUBJ",
        object_category="OBJ",
        category=["biolink:Association"],
        knowledge_level="not_provided",
        agent_type="not_provided",
    )
    koza_app.write(entity_a, entity_b, association)
