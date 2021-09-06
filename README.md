# UAHarvester

![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat&logo=python)
![OS](https://img.shields.io/badge/OS-GNU%2FLinux-red?style=flat&logo=linux)
![GitHub](https://img.shields.io/github/license/rlyonheart/uaharvester?ystyle=flat)
![CodeFactor](https://www.codefactor.io/repository/github/rlyonheart/uaharvester/badge)
![Lines of code](https://img.shields.io/tokei/lines/github/rlyonheart/uaharvester)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/rlyonheart/uaharvester) 
![GitHub repo size](https://img.shields.io/github/repo-size/rlyonheart/uaharvester)

User-Agent information harvester

# Intallation
**Clone this repo**:
> <code>$ git clone https://github.com/rlyonheart/uaharvester.git</code>
  
> <code>$ cd uaharvestr</code>

> <code>$ pip install -r requirements.txt</code>

# Usage
> <code>$ python uaharvester.py TARGET USER-AGENT</code>

**Note**:
*The target user agent should be put inside quote " " symbols*

**Example**:
 > <code>$ python uaharvester.py "Mozilla/5.0 (*this user agent is obviously not valid*) AppleWebKit/537.36 (KHTML, like Gecko) Safari/0.0.0.0 Safari/0.0.0.0"</code>
 ![uaharvester_1](https://user-images.githubusercontent.com/74001397/132225176-6031a05a-8d04-40f1-922f-95372fd24ee4.jpg)


**Note**:
*You can add the  **--is-crawler**  flag to check if the user agent is a crawler or not*
![uaharverster_2](https://user-images.githubusercontent.com/74001397/132225292-53522e6b-397e-4eba-a206-81cf23522bdf.jpg)

