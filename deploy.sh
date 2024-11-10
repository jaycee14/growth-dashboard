#!/bin/bash
# Purpose: To deploy the App to Cloud Run.

# Google Cloud Project ID
PROJECT=growth-dashboard-441320

# Google Cloud Region
LOCATION=europe-west2

# Deploy app from source code
gcloud run deploy growth-dashboard --source . --region=$LOCATION --project=$PROJECT --allow-unauthenticated