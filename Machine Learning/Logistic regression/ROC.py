try:
    from sklearn.metrics import roc_curve, roc_auc_score #type:ignore
    import matplotlib.pyplot as plt #type:ignore

    # Step 1: probability
    y_prob = model.predict_proba(X_test)[:,1] #type:ignore

    # Step 2: ROC values
    fpr, tpr, thresholds = roc_curve(y_test, y_prob) #type:ignore

    # Step 3: Plot
    plt.plot(fpr, tpr, label="Model")
    plt.plot([0,1],[0,1],'--')

    plt.xlabel("FPR")
    plt.ylabel("TPR")
    plt.title("ROC Curve")
    plt.legend()
    plt.show()

    # Step 4: AUC
    print("AUC:", roc_auc_score(y_test, y_prob)) #type:ignore
except:
    print('This code is only for copy paste')
finally:
    print('ROC Curve: Har threshold par model performance check karta hai TPR vs FPR')