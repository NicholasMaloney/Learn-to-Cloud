# Serverless Pokémon API Web App
This project iterates on my previous project: [Pokemon API Web App](https://github.com/NicholasMaloney/Learn-to-Cloud/tree/main/Phase-2-Programming#pok%C3%A9mon-api-web-app)
- The goal of this iteration is to make the project serverless, host all aspects of the project in Azure and get hands-on experience with Azure SDKs & Functions, Python and Terraform
  - if possible I will be reusing the HTML code / front end from my previous project. The reason being, I want to dedicate the time to learning Azure, Python and Terraform instead of learning HTML.
- My previous project was overwhelming, but taught me a valuable lesson: "you cannot expect the world when you cannot grasp what is under your feet," this has led me to establish personal guidelines for this project as I continue to navigate unfamiliar technologies.

### Guidelines
- I will only ask AI for assistance after 2 hours of attempting to solve the problem using Microsoft documentation, Stack Overflow and Reddit with no progress. If at the end of the two hours I have made meaningful progress I will continue without the use of AI.
- In the event I copy code or use AI to solve a problem, I will type the solution by hand and not copy/paste.
- I will break down and understand any and all code gained from foreign sources before using it in my project
- Note: I created these guidelines to assist my learning in a few ways,
  - To not become dependent on AI
  - To make sure what I am doing I am learning, whilst understanding knowledge is not retained in one attempt but through continuous repetition
  - To alleviate frustration with being stuck on a problem
  - Finally to allow myself to use AI when it is needed
## Plan
![Capstone-Plan](https://github.com/user-attachments/assets/49a60953-a399-4c72-ad92-43d2eec9a369)

## Project Flow
- Web app hosted in Azure
    - Users input; Name, Type, Pokédex ID
    - Web app passes the User input to the Azure functions
- Azure functions process the request from the web app and retrieve the data from Cosmos DB
   
### Technology Stack
- Azure services
    - Cosmos DB NoSQL for data store
    - Blob storage for image store
    - Azure Functions to get the data
- Azure SDKs
    - azure-cosmos
    - azure-storage-blob
    - azure-functions
- Terraform to build and deploy the cloud infrastructure
- Python & related Azure SDKs to;
    - Created the functions
    - Interact with Cosmos DB and Blob
    - Upload JSON data into Cosmos DB
    - Upload images to Blob storage

