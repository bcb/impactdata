# PTV Alerts

Alert public transport users when their train line has disrupted services.

## Installation

Install Python 3.6 and create a virtual environment which uses that.

Install the requirements:
```sh
pip install -r requirements.txt
```

Set environment variables for your PTV API Key
([instructions](https://static.ptv.vic.gov.au/PTV/PTV%20docs/API/1475462320/PTV-Timetable-API-key-and-signature-document.RTF))
and a Slack token
([instructions](https://api.slack.com/custom-integrations/legacy-tokens)):

```sh
export PTV_KEY='(your key)'
export SLACK_TOKEN='(your token)'
```

## Usage

```python
>>> from ptvalerts import ptv, alerts
>>> disruptions = ptv.get_disruptions()
>>> users = [ptv.User('Beau', '@beau', 'Belgrave', 1)]
>>> alerts.send(disruptions, users)
```

To alert the four users from the test document:
```sh
python main.py
```
