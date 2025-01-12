from catboost import CatBoostClassifier


def train_cat(X, y, ITERATIONS, LEARNING_RATE, DEPTH, VERBOSE=False):

    model = CatBoostClassifier(iterations=ITERATIONS, learning_rate=LEARNING_RATE, depth=DEPTH, verbose=False)

    model.fit(X, y)

    return model