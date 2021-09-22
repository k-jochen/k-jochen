# Customized multi-model endpoint with Sagemaker
## 1. Content
```
.
├── Readme.md
├── upload_image.sh            -->   Script to push the inference image to ECR.
├── Dockerfile                 -->   Inference image docker file.
├── model_handler.py           -->   Script define the model handler.
├── dockerd-entrypoint.py      -->   Script for inference image entrypoint.
├── endpoint_deploy.ipynb      -->   Notebook example to deploy the inference endpoint and run inference.
├── endpoint_inference.ipynb   -->   Notebook example to run inference with the endpoint.
└── src/                       -->   Customized inference code. 
```

## 2. Usage instruction
- 1. Update the Dockerfile with need dependencies.
- 2. Within `src/`, create a separate folder for the python code to run load the model and run inference. A example can be found in `custom_model1`.
- 3. Expose your model in `model_handler.py` via `model_factory`.
- 4. Build and push the inference image to ECR. Run,
    ```
    ./upload_image.sh [YOUR-IMAGE-NAME] [YOUR-AWS-PROFILE-NAME]
    ```
- 5. In Sagemaker, use the `endpoint_deploy.ipynb` notebook to deploy the endpoint, the notebook also includes a sample code code snippet for inference.
- 6. To consume the endpoint as a RESTful API, checkout the Sagemaker API manual [here](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_runtime_InvokeEndpoint.html), you may need to sign your post request with [AWS signature V4](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-auth-using-authorization-header.html).