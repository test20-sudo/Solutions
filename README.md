# Answers to Problem 2

## 1. Why did you choose the particular algorithm?

I chose **Gradient Boosting** over other models after benchmarking it against several algorithms. It stood out by providing a strong balance of **accuracy**, **precision**, and **recall**, making it ideal for my task. Unlike other models, it consistently delivered the best overall results, demonstrating robustness in handling complex data patterns and minimizing both false positives and negatives. Its ability to improve iteratively through **boosting** further reinforced its reliability, making it the top choice among all tested algorithms.

## 2. What are the different tuning methods used for the algorithm?

The tuning methods used for the algorithms in the code are primarily focused on adjusting key hyperparameters to optimize model performance. Below are the key hyperparameters tuned for each algorithm:

- **Logistic Regression**: 
  - Regularization strength
  - Penalty type
  - Solver
  
- **Decision Trees**:
  - Maximum depth
  - Minimum samples for splitting
  - Minimum samples for leaf nodes
  
- **Support Vector Machines**:
  - Regularization parameter
  - Kernel type
  - Gamma
  
- **Random Forests**:
  - Number of estimators
  - Tree depth
  - Splitting criteria
  
- **K-Nearest Neighbors**:
  - Number of neighbors
  - Weight function
  - Distance metric
  
- **Gradient Boosting and XGBoost**:
  - Number of estimators
  - Learning rate
  - Tree depth

These hyperparameter adjustments help improve predictive accuracy and model robustness.

## 3. Did you consider any other choice of algorithm? Why or why not?

I did not consider **Naive Bayes** for this task because, while it is a simple and effective model for certain types of problems, it assumes feature independence, which may not hold in many real-world datasets. Given the models I've already used—such as **Decision Trees**, **Random Forest**, **Gradient Boosting**, and **XGBoost**—these algorithms are more robust and flexible in handling complex relationships between features, and they do not rely on the independence assumption. Additionally, **Naive Bayes** may struggle with performance when the features are highly correlated, which is common in many datasets. Therefore, I chose to focus on models that provide better performance and flexibility for the task.

## 4. What is the accuracy?

**Accuracy** is a measure of how often the model correctly classifies instances. In the case of **Gradient Boosting**, the accuracy is **0.9945**, meaning the model correctly predicted the class for approximately 99.45% of the total instances. While accuracy is a fundamental metric, it doesn’t capture all aspects of a model's performance, especially in imbalanced datasets. Given the high accuracy, this indicates that **Gradient Boosting** is performing exceptionally well, correctly identifying most of the true positives and true negatives.

## 5. What are the different types of metrics that can be used to evaluate the model?

There are several metrics that can be used to evaluate a model's performance, each providing a different perspective. For **Gradient Boosting**, the key metrics include:

- **Accuracy**: Measures the overall proportion of correct predictions.  
  - **Gradient Boosting**: 0.9945 (99.45% accuracy)

- **Precision**: Indicates how many of the positive predictions made by the model are actually correct. It helps assess the model’s ability to avoid false positives.  
  - **Gradient Boosting**: 0.9955

- **Recall**: Reflects how many of the actual positives the model correctly identified.  
  - **Gradient Boosting**: 0.9868

- **F1 Score**: The harmonic mean of precision and recall, providing a balance between the two.  
  - **Gradient Boosting**: 0.9911

- **AUC-ROC Score**: Measures the model's ability to distinguish between classes across various thresholds. A higher AUC indicates better performance.  
  - **Gradient Boosting**: 0.9924

- **MCC (Matthews Correlation Coefficient)**: Provides a more balanced measure by considering all four confusion matrix categories (true positives, true negatives, false positives, false negatives).  
  - **Gradient Boosting**: 0.9872

These metrics provide a comprehensive view of the model’s performance across various aspects, not just overall accuracy. A combination of these metrics helps assess the model’s ability to handle both balanced and imbalanced datasets.

## Conclusion

The **Gradient Boosting** algorithm, when tuned and evaluated across various performance metrics, demonstrated robust results with high accuracy, precision, recall, and F1 score. The other models tested also offered valuable insights, but Gradient Boosting consistently outperformed others in terms of overall performance and reliability.

