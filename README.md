# Examples on how to deploy Microsoft Fabric workspace items with the deploy-microsoft-fabric-items GitHub Action

Test repository that contains three examples of how to deploy with the [deploy-microsoft-fabric-items GitHub Action](https://github.com/EnchantedData/deploy-microsoft-fabric-items).

All of which can be found in the .github\workflows subfolder in this repository.

- `deploy-microsoft-fabric-items-entire-workspace-fabric-cicd-vers.yml`  - Shows how to deploy all items to a new workspace using a specific version of the fabric-cicd library.
- `deploy-microsoft-fabric-items-entire-workspace.yml`  - Shows how to deploy all items to a new workspace with latest version of fabric-cicd library.
- `deploy-microsoft-fabric-items-selected-items.yml`  - Shows how to deploy selected items to a new workspace with latest version of fabric-cicd library.

In order to use any of these workflows in GitHub you can either clone or fork this repository into another GitHub repository.

All of the files contain details about what secrets and/or variables to add in order for the specific workflow to run. To run a specific workflow go into the `Actions` tab in your version of the Git repository and run the relevant workflow. 