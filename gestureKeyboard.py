from __future__ import print_function
from pygarl.base import CallbackManager
from pygarl.classifiers import SVMClassifier
from pygarl.mocks import VerboseMiddleware
from pygarl.data_readers import SerialDataReader
from pygarl.predictors import ClassifierPredictor
from pygarl.sample_managers import DiscreteSampleManager

MODEL_PATH="C:\\Users\\Hacktivist\\model.svm"
PORT="COM13"

def receive_character(number):
    print(number)


# Create the SerialDataReader
sdr = SerialDataReader(PORT, expected_axis=6, verbose=False)

# Create the SampleManager
manager = DiscreteSampleManager()

# Attach the manager
sdr.attach_manager(manager)

# Create a classifier
classifier = SVMClassifier(model_path=MODEL_PATH)

# Load the model
classifier.load()

# Print classifier info
classifier.print_info()

# Create a ClassifierPredictor
predictor = ClassifierPredictor(classifier)

# Attach the classifier predictor
manager.attach_receiver(predictor)

# Create a CallbackManager
callback_mg = CallbackManager(verbose=True)

# Attach the callback manager
predictor.attach_callback_manager(callback_mg)

# Bind all the numbers
for c in ["1", "2", "3", "4"]:
    callback_mg.attach_callback(c, receive_character)

# Open the serial connection
sdr.open()
print("Opened!")

# Start the main loop
sdr.mainloop()
