# Gradient Descent History
import tensorflow as tf
import matplotlib.pyplot as plt

tf.set_random_seed(777)  # for reproducibility

# X and Y data
X = [1, 2, 3]
Y = [1, 2, 3]


# W(h(x)의 기울기)에 따른 h(x)를 그래프로 보여보자. (X축은 W, Y축은 h(x))
def ex1():
    W = tf.placeholder(tf.float32)

    # Our hypothesis for linear model X * W
    # 여기서 오차값(=입실론, =Y절편, =b)는 생략했다.
    hypothesis = X * W

    # cost(loss) function
    # 가설값과 예측값 차이의 제곱들의 평균
    cost = tf.reduce_mean(tf.square(hypothesis - Y))

    # Launch the graph in a session.
    sess = tf.Session()

    # 그래프를 그리기 위한 값을 저장할 리스트
    W_history = []
    cost_history = []

    # Fit the line
    for i in range(-30, 50):
        # 현재 가중치(기울기)
        # [ -30*0.1, -29*0.1 ... 50*0.1 ]
        curr_W = i * 0.1

        # 현재 비용
        # 기울기가 -3인 경우부터, cost값을 구한다.
        curr_cost = sess.run(cost, feed_dict={W : curr_W})

        # cost와 W 값을 추가한다.
        W_history.append(curr_W)
        cost_history.append(curr_cost)

    # Show the cost function
    plt.plot(W_history, cost_history)
    plt.show()



# cost가 최소가 되는 W를 찾기위해 Gradient Descent를 적용해보자.
def ex2():
    x_data = [1, 2, 3]
    y_data = [1, 2, 3]

    # Try to find values for W and b to compute y_data = W * x_data + b
    # We know that W should be 1 and b should be 0
    # But let's use TensorFlow to figure it out
    # tf.random_normal([1]) : 랜덤값이 담긴 1차원의 배열을 반환한다.
    W = tf.Variable(tf.random_normal([1]), name='weight')
    X = tf.placeholder(tf.float32)
    Y = tf.placeholder(tf.float32)

    # Our hypothesis for linear model X * W
    hypothesis = X * W

    # cost(loss) function
    cost = tf.reduce_mean(tf.square(hypothesis - Y))

    # Minimize: Gradient Descent using derivative: W -= learning_rate * derivative
    learning_rate = 0.1
    gradient = tf.reduce_mean((W * X - Y) * X)
    descent = W - learning_rate * gradient
    update = W.assign(descent)

    # Launch the graph in a session.
    sess = tf.Session()
    # Initializes global variables in the graph.
    sess.run(tf.global_variables_initializer())

    # 랜덤으로 설정한 초기의 W값을 기울기 하강법을 적용한다.
    # cost가 최소가 되는(오차값이 가장 작은) W를 구한다.
    for step in range(21):
        sess.run(update, feed_dict={X: x_data, Y: y_data})
        print(step, sess.run(cost, feed_dict={X: x_data, Y: y_data}), sess.run(W))

    '''
    0 1.93919 [ 1.64462376]
    1 0.551591 [ 1.34379935]
    2 0.156897 [ 1.18335962]
    3 0.0446285 [ 1.09779179]
    4 0.0126943 [ 1.05215561]
    5 0.00361082 [ 1.0278163]
    6 0.00102708 [ 1.01483536]
    7 0.000292144 [ 1.00791216]
    8 8.30968e-05 [ 1.00421977]
    9 2.36361e-05 [ 1.00225055]
    10 6.72385e-06 [ 1.00120032]
    11 1.91239e-06 [ 1.00064015]
    12 5.43968e-07 [ 1.00034142]
    13 1.54591e-07 [ 1.00018203]
    14 4.39416e-08 [ 1.00009704]
    15 1.24913e-08 [ 1.00005174]
    16 3.5322e-09 [ 1.00002754]
    17 9.99824e-10 [ 1.00001466]
    18 2.88878e-10 [ 1.00000787]
    19 8.02487e-11 [ 1.00000417]
    20 2.34053e-11 [ 1.00000226]
    '''


# GradientDescentOptimizer 함수를 사용해 ex2의 결과를 도출한다.
def ex3():
    # Set wrong model weights
    W = tf.Variable(5.0)

    # Linear model
    hypothesis = X * W

    # cost/loss function
    cost = tf.reduce_mean(tf.square(hypothesis - Y))

    # Minimize: Gradient Descent Magic
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
    train = optimizer.minimize(cost)

    # Launch the graph in a session.
    sess = tf.Session()
    # Initializes global variables in the graph.
    sess.run(tf.global_variables_initializer())

    for step in range(100):
        print(step, sess.run(W))
        sess.run(train)

    '''
    0 5.0
    1 1.26667
    2 1.01778
    3 1.00119
    4 1.00008
    ...
    96 1.0
    97 1.0
    98 1.0
    99 1.0
    '''
ex3()