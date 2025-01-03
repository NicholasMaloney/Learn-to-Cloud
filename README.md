# Learn-to-Cloud
I am undertaking the Learn to Cloud project to strengthen my understanding of cloud concepts and gain hands-on experience with cloud security.
* Learn to Cloud website: https://learntocloud.guide/

### Socials 
* Linkedin: https://www.linkedin.com/in/nicholas-mal/
* My website: https://nicholasmaloney.notion.site/

### Notes 
- Fix my issue with WSL
    - Updated from Windows 10 home to Windows 10 Pro 
    - Disabled all virtualisation features & WSL (win + r | optionalfeatures)
    - Uninstalled WSL Run PowerShell as administrator  
        - Run command: Get-AppxPackage MicrosoftCorporationII.WindowsSubsystemForLinux | Remove-AppxPackage
    - Restart PC 
    - Install WSL (Open PowerShell as an administrator. Run the following command: wsl --install)
- Set up WSL, using Ubuntu
    - Installed git, vscode, authenticated to github
    - ~~Need to install Azure CLI~~ Azure CLI installed 
    - ZSH & ZSH plugins installed 
    - Terraform installed 
    - Completed Topic 4 
        - Created an Azure VM, connected to it via SSH 
        - Created and run a Node.js application on Azure VM Using SSH
    - Deployed the "Linux Command Line CTF Challenge" environment
        - Modified the main.tf file 
            - Added "subscription_id" under "provider azurerm"
            - Replace the VM Configuration to use Azure Spot Instances as I am using a student subscription
            - I got a “Error: static IP allocation…” when trying to apply the Terraform Configuration
                - To fix it, I done the following 
                    - Modified the section: resource "azurerm_public_ip" "ctf_public_ip
                    - Changed “allocation_method” from “Dynamic” to "Static"
                    - Added new variable “sku = Standard” 
                    - Reran the command: terraform plan
                    - Ran the command: terraform apply -var="az_region=australiaeast"
                    - Followed prompts and saved the output public IP address 
- Currently working on the "Linux Command Line CTF Challenge" 
    - I have solved the first 3 CTF flags
    - Completed all Linux CTF challenges 
- Moving on to Phase 2: Programming
    
