gcloud workflows deploy sample-workflow \
        --location=europe-west4 \
        --description='Sample load workflow' \
        --source=./workflow.yaml \
        --project YOUR_PROJECT \
        --service-account=sa-workflow@YOUR_PROJECT.iam.gserviceaccount.com