# Python script that allows you to all items can be tested for deployment locally first
# Install Python 3.12, the fabric-cicd library and Azure CLI locally
# Ensure you create the workspace beforehand
# Log in with Azure CLI (az login) prior to execution

# Syntax to run 'python .\auth_local_hard_coded.py'

from pathlib import Path

from azure.identity import AzureCliCredential
from fabric_cicd import FabricWorkspace, publish_all_items, unpublish_all_orphan_items

# Assumes your script is one level down from root
root_directory = Path(__file__).resolve().parent

# Sample values for FabricWorkspace parameters
workspace_id = "{TARGET WORKSPACE ID HERE}"
environment = "Test"
repository_directory = str(root_directory / "workspace")
# item_type_in_scope = ["Report","SemanticModel"]

# Use Azure CLI credential to authenticate
token_credential = AzureCliCredential()

# Initialize the FabricWorkspace object with the required parameters
target_workspace = FabricWorkspace(
    workspace_id=workspace_id,
    environment=environment,
    repository_directory=repository_directory,
    token_credential=token_credential,
)

# Publish all items defined in item_type_in_scope
publish_all_items(target_workspace)

# Unpublish all items defined in item_type_in_scope not found in repository
unpublish_all_orphan_items(target_workspace)