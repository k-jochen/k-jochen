class BaseModel:
    def __init__(self):
        pass

    def load_model(self, context):
        """Load Model"""
        self.model = None

    def preprocess(self, data, context):
        """Preprocessing"""
        return data
    
    def predict(self, data, context):
        """Run prediction with model"""
        raise NotImplementedError("The predict function must be defined.")

    def postprocess(self, data, context):
        """Postprocessing"""
        return data
    
    def inference(self, data, context):
        """Main Inference entrance function"""
        data = self.preprocess(data, context)
        pred = self.predict(data, context)
        pred = self.postprocess(pred, context)
        return pred
    