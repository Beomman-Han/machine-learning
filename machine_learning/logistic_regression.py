import numpy as np

def sigmoid(x : np.array) -> np.array:
    """Sigmoid function"""
    return 1 / (1 + np.exp(-x))
    

def prediction(X : np.array, theta : np.array) -> np.array:
    """Hypothesis function of logistic regression"""
    return sigmoid(X @ theta)

def gradient_descent(
    X : np.array,
    theta : np.array,
    y : np.array,
    iterations : int,
    alpha : float
    ) -> np.array:
    
    """Gradient descent algorithm of logistic regression"""
    
    m = len(X)  # 입력 변수 개수 저장

    for _ in range(iterations):
        error = prediction(X, theta) - y
        theta = theta - alpha / m * (X.T @ error)
            
    return theta


if __name__ == '__main__':
    # 입력 변수
    hours_studied = np.array([0.2, 0.3, 0.7, 1, 1.3, 1.8, 2, 2.1, 2.2, 3, 4, 4.2, 4, 4.7, 5.0, 5.9])  # 공부 시간 (단위: 100시간)
    gpa_rank = np.array([0.9, 0.95, 0.8, 0.82, 0.7, 0.6, 0.55, 0.67, 0.4, 0.3, 0.2, 0.2, 0.15, 0.18, 0.15, 0.05]) # 학년 내신 (백분률)
    number_of_tries = np.array([1, 2, 2, 2, 4, 2, 2, 2, 3, 3, 3, 3, 2, 4, 1, 2])  # 시험 응시 횟수

    # 설계 행렬 X 정의
    X = np.array([
        np.ones(16),
        hours_studied,
        gpa_rank,
        number_of_tries
    ]).T

    # 파라미터 theta 정의
    theta = [0.5, 0.3, -2, 0.2]  

    print(prediction(X, theta))