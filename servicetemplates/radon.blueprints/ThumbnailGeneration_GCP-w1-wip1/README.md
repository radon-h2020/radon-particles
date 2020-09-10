## Thumbnail Generation App

This blueprint represents a thumbnail generation example application implemented using Google Cloud.

### Quickstart

1. Install Google Cloud SDK from as described here: <https://cloud.google.com/sdk/docs/downloads-apt-get>
2. Create a Google Cloud Service Account (Google Cloud Console > IAM). 
   Further, generate a new key along with a JSON file that can be downloaded.
3. Initialize xOpera:
   ```
   mkdir gcp && cd gcp
   python3 -m venv .venv && . .venv/bin/activate
   pip install --upgrade pip
   pip install opera
   ```
4. Unzip the CSAR: `unzip ThumbnailGeneration_GCP-w1-wip1.csar`
5. Create an `inputs.yml` file:
   ```
   ---
   project_id: <project_id found in the GCP console>
   service_account_file: <path to the JSON file you downloaded>
   ```
6. Execute the deployment: `opera deploy -i inputs.yml _definitions/radonblueprints__ThumbnailGeneration_GCP-w1-wip1.tosca`
