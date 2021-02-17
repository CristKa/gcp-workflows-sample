import json
import google.auth
from google.auth.transport.requests import AuthorizedSession

def onNewFile(event, context):

    print('Event ID: {}'.format(context.event_id))
    print('Event type: {}'.format(context.event_type))
    print('Bucket: {}'.format(event['bucket']))
    print('File: {}'.format(event['name']))

    scoped_credentials, project = google.auth.default(
        scopes=['https://www.googleapis.com/auth/cloud-platform'])
    authed_session = AuthorizedSession(scoped_credentials)

    URL = 'https://workflowexecutions.googleapis.com/v1/projects/YOUR_PROJECT/locations/YOUR_REGION/workflows/sample-workflow/executions'
    file_id_dict = {'file_id': 'gs://{}/{}'.format(event['bucket'], event['name'])}
    PARAMS = { 'argument' : json.dumps(file_id_dict) }
    response = authed_session.post(url=URL, json=PARAMS)

    print(response)