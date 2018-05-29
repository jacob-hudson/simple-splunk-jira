import sys
import json
import requests

def create_jira_incident(settings, global_settings):
    token_raw = str(settings.get('jira_user')) + ":" + str(settings.get('jira_password'))
    token_encoded = base64.b64encode(token_raw.encode('ascii'))

    key = str(settings.get('key'))
    type = str(settings.get('type'))
    summary = str(settings.get('summary'))
    description = str(settings.get('description'))

    data = {"fields":{"project":{"key":key},"summary":summary,"description":description,"issuetype":{"name":type}}}
    headers = {"content-type":"application/json", "Authorization:Basic" token_encoded}

    requests.post(jira_url, headers=headers, data=data)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "--execute":
        payload = json.loads(sys.stdin.read())
        settings = payload
        config = payload.get('configuration')
        if not create_jira_indicent(config, settings):
            print >> sys.stderr, "FATAL Creating the jira incident failed"
