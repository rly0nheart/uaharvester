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
 > <code>$ python uaharvester.py "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/0.0.0.0 Safari/537.36 Edg/0.0.0.0"</code>

**Note**:
*You can add the --is-crawler flag to check if the user agent is a crawler or not*
