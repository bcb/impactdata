# PTV Alerts

Alert public transport users when their train line has disrupted services.

## Installation

Install Python 3.6 and create a virtual environment which uses that.

Install the requirements:
```sh
pip install -r requirements.txt
```

Set environment variables for your [PTV API
Key](https://static.ptv.vic.gov.au/PTV/PTV%20docs/API/1475462320/PTV-Timetable-API-key-and-signature-document.RTF)
and [Slack token](https://api.slack.com/custom-integrations/legacy-tokens):

```sh
export PTV_KEY='(your key)'
export SLACK_TOKEN='(your token)'
```

## Usage

```python
from ptvalerts import ptv, slack
users = [ptv.User('@beau', 'Belgrave', 1)]
disruptions = ptv.get_disruptions()
slack.send(users, disruptions)
```

To alert the four users from the Impact Data test PDF:
```sh
python main.py
```
