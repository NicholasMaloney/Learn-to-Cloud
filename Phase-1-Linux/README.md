# Table of Contents
- [Topic 1: Version Control](#topic-1-version-control)
- [Topic 2: Cloud CLI setup](#topic-2-cloud-cli-setup)
- [Topic 3: Infrastructure as Code](#topic-3-infrastructure-as-code)
- [Linux Command Line CTF Challenge](#linux-command-line-ctf-challenge)
  - [Setting Up The CTF Environment](#setting-up-the-ctf-environment)
- [CTF Challenges](#ctf-challenges)

## Topic 1: Version Control

### Environment Setup
- **Note**: I initially used a Kali Linux VM as I was having issues with WSL. I later fixed my issue with WSL and moved to using Ubuntu via WSL.
  
- **Steps**:
    - Installed Git and VS Code.
    - Created a directory named `12c` and cloned the GitHub repository:
      ```
      https://github.com/rishabkumar7/ltc-labs
      ```
      ![Env-setup](https://github.com/user-attachments/assets/2bd4b753-3a05-4405-9506-0d3bba58a258)

### Configuring Git
- **Steps**:
    - Created a GitHub repository named **Learn-to-Cloud**.
    - Navigated to `~/12c`.
    - Created a directory called **GitHub**:
        - Within `~/12c/Github`, I created a directory called **Learn-to-Cloud**.
    - Navigated to the **Learn-to-Cloud** directory:
        - Configured Git:
            ```
            git init
            git config user.name "Your Name"
            git config user.email "your_email@example.com"
            ```
            ![git](https://github.com/user-attachments/assets/a524775f-c0b7-4648-ac17-ac20f88261ff)
    - Established a Git remote connection to the **Learn-to-Cloud** repository: Repo alias: **Origin**
      ![Git remote connection](https://github.com/user-attachments/assets/daed2eac-d10c-4921-8798-5224f8b761fc)
    - Set up a GitHub access token for the repository:
        - Created a classic token on GitHub and granted it full permissions for 30 days.
    - Using the access token, I configured Git/GitHub authentication/authorization:
      ![access token](https://github.com/user-attachments/assets/ff793153-b0d7-498c-8c38-6172109c99ff)
    - Pulled all commits for the repository:
        ```
        git fetch origin
        ```
      - `origin` is the alias given to the repository.
    - Switched to the main branch:
        ```
        git switch main
        ```
        ![Pull](https://github.com/user-attachments/assets/561fb3a4-b99c-44e3-9f0e-2ca78d37870f)
    - Updated `README.md`:
        ![read](https://github.com/user-attachments/assets/7317958d-6061-4087-aa71-7705b36e325c)
    - Pushed the changes to GitHub:
        ```
        git add .
        git commit -m "Updated README"
        git push origin
        ```
        ![Readme-push](https://github.com/user-attachments/assets/0e3a01d1-a76a-4788-9506-916b201c92a5)

## Topic 2: Cloud CLI Setup
- **Install Azure CLI **
  ```
    https://learn.microsoft.com/en-au/cli/azure/install-azure-cli-linux?pivots=apt 
  ```
  - Logged into my Azure account
    ```
    az login
    ```
  - Verified I am in the right Subscription
     ```
     az account show
     ```
     ![az-show](https://github.com/user-attachments/assets/adfe3164-f44d-45be-af3c-0537935f23ec)

## Topic 3: Infrastructure as Code
### Installing Terraform 
```
https://developer.hashicorp.com/terraform/tutorials/azure-get-started/install-cli
```
  - **Steps**
    - Verify system is uptodate and you have the required packages installed: gnupg, software-properties-common, and curl
      ```
      sudo apt list --installed | grep packageName
      sudo apt-get update && sudo apt-get install -y gnupg software-properties-common
      ```
    - Install the HashiCorp GPG key.
      ```
      wget -O- https://apt.releases.hashicorp.com/gpg | \
      gpg --dearmor | \
      sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null
      ```
      ![GPGkey](https://github.com/user-attachments/assets/4ee0dcf8-c23f-45b5-89c0-e28defe1a95b)

    - Verify the key's fingerprint
      ```
      gpg --no-default-keyring \
      --keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
      --fingerprint
      ```
      ![fingerprint](https://github.com/user-attachments/assets/2ece58d5-286d-4768-8b24-5487c6595bfd)
      - Navigate to this website: https://www.hashicorp.com/trust/security?product_intent=terraform
        - Scroll to the **Linux package checksum verification**
          - “f search” paste key: 798A EC65 4E5C 1542 8C8E  42EE AA16 FCBC A621 E701
          - Remove a space between “8C8E 42EE”
      ![checksum](https://github.com/user-attachments/assets/642ca5a5-2dcf-48a8-b64a-5a734d343704)
    - Add the official HashiCorp repository to your system
      ```
      echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
      https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
      sudo tee /etc/apt/sources.list.d/hashicorp.list
      ```
    - Download the package information from HashiCorp
      ```
      sudo apt update
      ```
    - Install Terraform from the new repository.
      ```
      sudo apt-get install terraform
      ```
    - Verify the installation
      ```
      terraform -help
      ```
      ![terra-help](https://github.com/user-attachments/assets/3613eb02-6182-4d86-9939-20a18ba4d6bf)

# Linux Command Line CTF Challenge
### Setting Up The CTF Environment
  - Replaced the VM Configuration to use Azure Spot Instances as I am using a student subscription: https://github.com/g-now-zero/l2c-guides/blob/main/posts/ctf-azure-spot-instances-guide.md
    - Navigate to /12c/ltc-labs/azure
      - Modified the main.tf file
      - Added subscription id
        ```
        provider "azurerm" {
        features {}
        subscription_id = "your-subscription-id-here"
        }
        ```
      - Initialised Terraform in the /12c/ltc-labs/azure directory
      - Created Terraform plan
      - I got this error: “Error: static IP allocation must be used when creating Standard SKU public IP addresses”
        
        ![error-t](https://github.com/user-attachments/assets/9f32aa1a-4959-4ef6-a279-9e31943048e6)

      - **To fix the “Error: static IP allocation…”**
        - Open main.tf with vscode
        - Modify the section: resource "azurerm_public_ip" "ctf_public_ip”
        - Change “allocation_method” from “Dynamic” to Static
        - Add “sku = Standard”

          ![ip-err-res](https://github.com/user-attachments/assets/a1efd3d0-5161-41f5-8820-321076b52f16)

        - Now the main.tf file has been changed, run: `terraform plan`
          - Then run: `terraform apply -var="az_region=australiaeast"`
            - When prompted enter: `yes`

              ![yes](https://github.com/user-attachments/assets/254d55fd-8b55-4be0-ae4e-b97f801d37dc)

        - After a few minutes configurations should be applied and you will get this message  

          ![t-msg](https://github.com/user-attachments/assets/09d6c961-aee2-4da9-b4e1-158b5969666a)

        - You can now login to the VM via SSH using the IP address output above: `ssh ctf_user@52.237.252.186`
# CTF Challenges 

### 1. CTF
- First flag found | CTF{hidden_files_revealed}
  - `ls -a`  to show the hidden files
  - `cat .hidden_flag`  to display contents
    
    ![1-CTF](https://github.com/user-attachments/assets/9644a63e-5ee0-4fd2-ab6a-967ad6d0d786)

### 2. CTF
- Second flag | CTF{grep_is_your_friend}
  - ` find . -name "secret"` search for any file or directory with "secret" anywhere in its name
    
    ![2-CTF](https://github.com/user-attachments/assets/76bdd546-7880-44be-815a-9d828f632468)

### 3. CTF
- Third flag | CTF{size_matters_in_linux}
- Navigated to /var/log
  - Ran:  `grep -r "CTF{" .`
  - Got a hit in the ‘journal’ directory. Looks like the ‘user-1001.journal: binary file matches

     ![3-1-CTF](https://github.com/user-attachments/assets/eaa6b111-c0a8-444a-8249-f1e247549e38)

  - From var/log I navigated to ./journal/e3a5daaa… 
    - ran `grep -a "CTF{" user-1001.journal`
    
      ![3-CTF](https://github.com/user-attachments/assets/4b3d1e60-6b72-49d9-a8d6-19c69750ab6c)

### 4. CTF
- I ram into issues with this flag and have reported it accordingly, big shout out to rishabkumar7 as he was super quick to respond and is currently testing this issue: https://github.com/learntocloud/ltc-linux-challenge/issues/13#issuecomment-2569465689

### 5. CTF
- fifth flag | CTF{permission_granted}
  - Ran: `find /root -type f -perm -u+r`
  - Only file that didn’t throw an error is “/root/everyone_can_access_me”
  - Read file: `cat /root/everyone_can_access_me`

    ![5-CTF](https://github.com/user-attachments/assets/ac76dbcd-f89a-422c-be27-b71306f70f3e)

### 6. CTF
- Sixth flag | CTF{port_explorer}
  - I found this earlier when searching for flag four :)
    - Navigate to `/home/ctf_user/ctf_challenges`
    - Ran: `ls -a`
    - Found file: `port_8080_service.sh `
      - `cat port_8080_service.sh`

        ![6-CTF](https://github.com/user-attachments/assets/714ba425-6d16-4bf2-a591-7b6f10eb06ae)

### 7. CTF
- Seventh flag | CTF{base64_decoder}
  - Navigate to /home/ctf_user/ctf_challenges
  - List the files in the dir: ls
  - Read contents of encoded_flag.txt
    - `cat encoded_flag.txt`
  - Decrypt the base64 output
    - `echo "Q1RGe2Jhc2U2NF9kZWNvZGVyfQ==" | base64 -d`
    
      ![7-CTF](https://github.com/user-attachments/assets/79e4c7b3-c5b5-413b-8639-793736eaa78d)



