gcloud functions deploy workflow-trigger \
       --region=europe-west1 \
       --entry-point onNewFile \
       --runtime python38 \
       --trigger-resource YOUR_INPUT_BUCKET \
       --trigger-event google.storage.object.finalize \
       --service-account=sa-cf-trigger@YOUR_PROJECT.iam.gserviceaccount.com