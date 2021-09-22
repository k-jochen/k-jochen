"""
ModelHandler defines an example model handler for load and inference requests for MXNet CPU models
"""
from src.models.model import StdDetector, RMSDetector,IsoDetector
from src import logger 

class ModelHandler(object):
    """
    A sample Model handler implementation.
    """

    def __init__(self):
        self.model = None
        self.model_name = None
        self.initialized = False
        self.model_factory = {
            "StdDetector.tar.gz": StdDetector,
            "RMSDetector.tar.gz": RMSDetector,
            "IsoDetector.tar.gz": IsoDetector
        }


    def initialize(self, context):
        """
        Initialize model. This will be called during model loading time
        :return:
        """
        self.initialized = True
    
    def handle(self, data, context):
        """
        Call preprocess, inference and post-process functions
        :param data: input data
        :param context: mms context
        """
        self.model_name = context.get_request_header(0, "X-Amzn-SageMaker-Target-Model")
        print('self.model_name',self.model_name)
        print('self.model_factory',self.model_factory)
        #logger.info("model handler : 36")
        try:
            if self.model_name in self.model_factory:
                #logger.info("Found model %s" % (self.model_name))
                self.model = self.model_factory[self.model_name]()
                self.model.load_model(context)
                #logger.info("MODEL LOADED")
                inference_ret_val = self.model.inference(data, context=context)
                #logger.info("MODEL INFERENCE DONE")
                return inference_ret_val
            else:
                raise NotImplementedError(f"This inference function for {self.model_name} is not implemented in this endpoint.")
        except Exception as e:
            logger.error(e)

_service = ModelHandler()


def handle(data, context):
    if not _service.initialized:
        _service.initialize(context)

    if data is None:
        return None

    return _service.handle(data, context)
