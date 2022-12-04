
  /**
   * This snippet has been automatically generated and should be regarded as a code template only.
   * It will require modifications to work.
   * It may require correct/in-range values for request initialization.
   * TODO(developer): Uncomment these variables before running the sample.
   */
  /**
   *  Required. The name of the Endpoint requested to serve the explanation.
   *  Format:
   *  `projects/{project}/locations/{location}/endpoints/{endpoint}`
   */
  // const endpoint = 'abc123'
  /**
   *  Required. The instances that are the input to the explanation call.
   *  A DeployedModel may have an upper limit on the number of instances it
   *  supports per request, and when it is exceeded the explanation call errors
   *  in case of AutoML Models, or, in case of customer created Models, the
   *  behaviour is as documented by that Model.
   *  The schema of any single instance may be specified via Endpoint's
   *  DeployedModels' Model's google.cloud.aiplatform.v1.DeployedModel.model 
   *  PredictSchemata's google.cloud.aiplatform.v1.Model.predict_schemata 
   *  instance_schema_uri google.cloud.aiplatform.v1.PredictSchemata.instance_schema_uri.
   */
  // const instances = 1234
  /**
   *  The parameters that govern the prediction. The schema of the parameters may
   *  be specified via Endpoint's DeployedModels' Model's  google.cloud.aiplatform.v1.DeployedModel.model 
   *  PredictSchemata's google.cloud.aiplatform.v1.Model.predict_schemata 
   *  parameters_schema_uri google.cloud.aiplatform.v1.PredictSchemata.parameters_schema_uri.
   */
  // const parameters = {}
  /**
   *  If specified, overrides the
   *  explanation_spec google.cloud.aiplatform.v1.DeployedModel.explanation_spec  of the DeployedModel.
   *  Can be used for explaining prediction results with different
   *  configurations, such as:
   *   - Explaining top-5 predictions results as opposed to top-1;
   *   - Increasing path count or step count of the attribution methods to reduce
   *     approximate errors;
   *   - Using different baselines for explaining the prediction results.
   */
  // const explanationSpecOverride = {}
  /**
   *  If specified, this ExplainRequest will be served by the chosen
   *  DeployedModel, overriding Endpoint.traffic_split google.cloud.aiplatform.v1.Endpoint.traffic_split.
   */
  // const deployedModelId = 'abc123'

  // Imports the Aiplatform library
  const {PredictionServiceClient} = require('@google-cloud/aiplatform').v1;

  // Instantiates a client
  const aiplatformClient = new PredictionServiceClient();

  async function callExplain() {
    // Construct request
    const request = {
      endpoint,
      instances,
    };

    // Run request
    const response = await aiplatformClient.explain(request);
    console.log(response);
  }

  callExplain();

  //https://tfhub.dev/tensorflow/efficientnet/lite0/feature-vector/2
  //https://tfhub.dev/google/imagenet/resnet_v1_101/feature_vector/5