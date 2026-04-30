try:
    from sklearn.model_selection import RandomizedSearchCV #type:ignore
    param_dist = {
        "C": [0.1, 1, 10, 50, 100],
        "penalty": ["l2"],
        "solver": ["lbfgs"]
    }

    random_search = RandomizedSearchCV(
        model , #type:ignore
        param_distributions=param_dist,
        n_iter=3,   # kitne random combinations try kare
        cv=5,
        scoring="accuracy",
        random_state=42
    ) 

    random_search.fit(X_train, y_train) #type:ignore

    best_model = random_search.best_estimator_

    print("Best Params:", random_search.best_params_)
    print("Best Score:", random_search.best_score_)
except:
    print('This code only for copy paste')
finally:
    print('RandomizedSearchCV: Random parameter combinations try karke fast best result deta hai')