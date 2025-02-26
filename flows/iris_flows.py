from prefect import flow, task, get_run_logger
from prefect.variables import Variable
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
# Set up our variables (can be done via UI as well)
def setup_variables():
    """Set up default variables if they don't exist"""
    Variable.set("rf_n_estimators", 100)
    Variable.set("rf_max_depth", 10)
    Variable.set("rf_test_size", 0.2)

@task
def load_data():
    """Load the iris dataset"""
    logger = get_run_logger()
    logger.info("Loading Iris dataset...")
    
    X, y = load_iris(return_X_y=True)
    logger.info(f"Dataset loaded with shape: {X.shape}")
    return X, y
@task
def split_dataset(X, y):
    """Split dataset using configurable test size"""
    logger = get_run_logger()
    
    test_size = Variable.get("rf_test_size", default=0.2)
    logger.info(f"Splitting dataset with test_size: {test_size}")
    
    return train_test_split(X, y, test_size=float(test_size), random_state=42)
@task
def train_model(X_train, y_train):
    """Train model using variables for hyperparameters"""
    logger = get_run_logger()
    
    # Load hyperparameters from variables
    n_estimators = Variable.get("rf_n_estimators", default=100)
    max_depth = Variable.get("rf_max_depth", default=10)
    
    logger.info(f"Training RandomForest with {n_estimators} trees and max_depth {max_depth}")
    
    model = RandomForestClassifier(
        n_estimators=int(n_estimators),
        max_depth=int(max_depth),
        random_state=42
    )
    model.fit(X_train, y_train)
    return model
@task
def evaluate_model(model, X_test, y_test):
    """Evaluate model performance"""
    logger = get_run_logger()
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    logger.info(f"Model Accuracy: {accuracy:.4f}")
    return accuracy
@flow(name="iris-classification")
def iris_classification_flow():
    """Main training flow for Iris classification"""
    logger = get_run_logger()
    logger.info("Starting Iris classification workflow")
    
    try:
        X, y = load_data()
        X_train, X_test, y_train, y_test = split_dataset(X, y)
        model = train_model(X_train, y_train)
        accuracy = evaluate_model(model, X_test, y_test)
        
        logger.info("Workflow completed successfully!")
        return accuracy
        
    except Exception as e:
        logger.error(f"Workflow failed: {str(e)}")
        raise
if __name__ == "__main__":
    # Set up variables with default values if they don't exist
    setup_variables()
    
    # Run the flow
    iris_classification_flow()