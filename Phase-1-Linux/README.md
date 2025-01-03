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


## Topic 3: Infrastructure as Code

## Topic 4: SSH

## Linux Command Line CTF Challenge
