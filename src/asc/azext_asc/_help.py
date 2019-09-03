# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import

helps['asc'] = """
    type: group
    short-summary: Commands to manage Spring cloud service.
"""

helps['asc create'] = """
    type: command
    short-summary: Create a spring cloud service.
    examples:
    - name: Create a new spring cloud service in westus.
      text: az asc create -n Myasc -g MyResourceGroup -l westus      
"""

helps['asc delete'] = """
    type: command
    short-summary: Delete a Spring cloud service.
"""

helps['asc list'] = """
    type: command
    short-summary: List all Spring cloud services in the given resource group, otherwise list the subscription's.
"""

helps['asc show'] = """
    type: command
    short-summary: Show the details for a Spring cloud service.
"""

helps['asc test-endpoint'] = """
    type: group
    short-summary: Commands to manage  test-endpoint in Spring cloud service.
"""

helps['asc test-endpoint enable'] = """
    type: command
    short-summary: Enable test endpoint of the Spring cloud service.
"""

helps['asc test-endpoint disable'] = """
    type: command
    short-summary: Disable test endpoint of the Spring cloud service.
"""

helps['asc test-endpoint list'] = """
    type: command
    short-summary: List test endpoint keys of the Spring cloud service.
"""

helps['asc test-endpoint renew-keys'] = """
    type: command
    short-summary: Regenerate a test-endpoint key for the Spring cloud service.
"""

helps['asc app'] = """
    type: group
    short-summary: Commands to manage apps in Spring cloud service.
"""

helps['asc app create'] = """
    type: command
    short-summary: Create a new app with a default deployment in the Spring cloud service.
    examples:
    - name: Create an app with the default configuration.
      text: az asc app create -n MyApp -s Myasc
    - name: Create an public accessible app with 3 instance and 2 cpu cores and 3 Gb of memory per instance.
      text: az asc app create -n MyApp -s Myasc -is-public true -cpu 2 -memory 3 -instance-count 3 
"""

helps['asc app update'] = """
    type: command
    short-summary: Update configurations of an app.
    examples:
    - name: Create an app with the default configuration.
      text: az asc app update --tags foo=bar
"""

helps['asc app delete'] = """
    type: command
    short-summary: Delete an app in the Spring cloud service.
"""

helps['asc app list'] = """
    type: command
    short-summary: List all apps in the Spring cloud service.
"""

helps['asc app show'] = """
    type: command
    short-summary: Show the details of an app in the Spring cloud service.
"""

helps['asc app start'] = """
    type: command
    short-summary: Start instances of the app, default to in production deployment.
"""

helps['asc app stop'] = """
    type: command
    short-summary: Stop instances of the app, default to in production deployment.
"""

helps['asc app restart'] = """
    type: command
    short-summary: Restart instances of the app, default to in production deployment.
"""

helps['asc app deploy'] = """
    type: command
    short-summary: Deploy source code or built binary to an app and update related configurations.
    examples:
    - name: Deploy source code to an app. This will pack current directory, build binary with Pivotal Build Service and then deploy to the app.
      text: az asc app deploy -n MyApp -s Myasc
    - name: Deploy a built jar to an app with jvm options and environment variables.
      text: az asc app deploy -n MyApp -s Myasc --jar-path app.jar --jvm-options "-XX:+UseG1GC -XX:+UseStringDeduplication" --env foo=bar
    - name: Deploy source code to a specific deployment of an app.
      text: az asc app deploy -n MyApp -s Myasc -d green-deployment
"""

helps['asc app scale'] = """
    type: command
    short-summary: Manually scale an app or its deployments.
    examples:
    - name: Scale up an app to 4 cpu cores and 8 Gb of memory per instance.
      text: az asc app scale -n MyApp -s Myasc --cpu 3 --memory 8
    - name: Scale out a deployment of the app to 5 instances.
      text: az asc app scale -n MyApp -s Myasc -d green-deployment --instance-count 5
"""

helps['asc app show-deploy-log'] = """
    type: command
    short-summary: Show a specificed deployment's log of the app, default to in production deployment.
"""

helps['asc app set-deployment'] = """
    type: command
    short-summary: Set in production deployment of an app.
    examples:
    - name: Swap a staging deployment of an app to production.
      text: az asc app set-deployment -d green-deployment -n MyApp -s Myasc
"""

helps['asc app deployment'] = """
    type: group
    short-summary: Commands to manage deployments of an app in Spring cloud service.
"""

helps['asc app deployment list'] = """
    type: command
    short-summary: List all deployments in an app.
"""

helps['asc app deployment show'] = """
    type: command
    short-summary: Show the details of a deployment.
"""

helps['asc app deployment delete'] = """
    type: command
    short-summary: Delete a deployment of the app.
"""

helps['asc app deployment create'] = """
    type: command
    short-summary: Create a staging deployment for the app.
    examples:
    - name: Deploy source code to a new deployment of an app. This will pack current directory, build binary with Pivotal Build Service and then deploy.
      text: az asc app deployment create -n green-deployment --app MyApp -s Myasc
    - name: Deploy a built jar to an app with jvm options and environment variables.
      text: az asc app deployment create -n green-deployment --app MyApp -s Myasc --jar-path app.jar --jvm-options "-XX:+UseG1GC -XX:+UseStringDeduplication" --env foo=bar
"""

helps['asc config-server'] = """
    type: group
    short-summary: Commands to manage config server in Spring cloud service.
"""

helps['asc config-server show'] = """
    type: command
    short-summary: Commands to show config server.
"""

helps['asc config-server set'] = """
    type: command
    short-summary: Commands to set config server.
"""

helps['asc config-server clear'] = """
    type: command
    short-summary: Commands to clear config server.
"""

helps['asc app binding'] = """
    type: group
    short-summary: Commands to manage service bindings of an app in Spring cloud service, and only restart app can make settings take effect.
"""

helps['asc app binding cosmos'] = """
    type: group
    short-summary: Commands to manage cosmosdb bindings.
"""

helps['asc app binding mysql'] = """
    type: group
    short-summary: Commands to manage mysql bindings.
"""

helps['asc app binding redis'] = """
    type: group
    short-summary: Commands to manage redis bindings.
"""
helps['asc app binding list'] = """
    type: command
    short-summary: List all service bindings in an app.
"""

helps['asc app binding show'] = """
    type: command
    short-summary: Show the details of a service binding.
"""
helps['asc app binding delete'] = """
    type: command
    short-summary: Delete a service binding of the app.
"""

helps['asc app binding cosmos add'] = """
    type: command
    short-summary: Bind an Azure Cosmos DB service with the app.
    examples:
    - name: Bind an Azure Cosmos DB service.
      text: az asc app binding cosmos create -n mysqlProduction --app MyApp --resource-id ${COSMOSDB_ID} --api-type mongo --database mymongo
"""

helps['asc app binding cosmos update'] = """
    type: command
    short-summary: Update an Azure Cosmos DB service binding of the app.
"""

helps['asc app binding mysql add'] = """
    type: command
    short-summary: Bind an Azure DB for MySQL service with the app.
"""

helps['asc app binding mysql update'] = """
    type: command
    short-summary: Update an Azure DB for MySQL service binding of the app.
"""

helps['asc app binding redis add'] = """
    type: command
    short-summary: Bind an Azure Redis Cache service with the app.
"""

helps['asc app binding redis update'] = """
    type: command
    short-summary: Update an Azure Redis Cache service binding of the app.
"""