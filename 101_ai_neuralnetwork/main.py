import numpy
import scipy.special

# ニューラルネットワーククラス
class neuralNetwork:
  # ニューラルネットワークの初期化
  def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
    # 入力層、隠れ層、出力層のノード数の設定
    self.inodes = inputnodes
    self.hnodes = hiddennodes
    self.onodes = outputnodes

    # リンクの重み行列 wih と who
    # 行列内の重み w_i_j ノード i から次の層のノード j へのリンクの重み
    # w11 w21
    # w12 w22 など

    # 重みを初期化する改善前のコード
    #self.wih = (numpy.random.rand(self.hnodes, self.inodes) - 0.5)
    #self.who = (numpy.random.rand(self.onodes, self.hnodes) - 0.5)

    # 改善後のコード
    self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
    self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))

    # 学習率の設定
    self.lr = learningrate

    # 活性化関数はシグモイド関数
    self.activation_function = lambda x: scipy.special.expit(x)
    pass
  
  # ニューラルネットワークの学習
  def train():
    pass
  
  # ニューラルネットワークへの照会
  def query(self, inputs_list):
    # 入力リストを行列に変換
    inputs = numpy.array(inputs_list, ndmin=2).T

    # 隠れ層に入ってくる信号の計算
    hidden_inputs = numpy.dot(self.wih, inputs)
    # 隠れ層で結合された信号を活性化関数により出力
    hidden_outputs = self.activation_function(hidden_inputs)

    # 出力層に入ってくる信号の計算
    final_inputs = numpy.dot(self.who, hidden_outputs)
    # 出力層で結合された信号を活性化関数により出力
    final_outputs = self.activation_function(final_inputs)
    
    return final_outputs


# 入力層、隠れ層、出力層のノード数
input_nodes = 3
hidden_nodes = 3
output_nodes = 3

# 学習率
learning_rate = 0.3

# ニューラルネットワーククラスのインスタンスの生成
n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

#-------------------------------------------------------------
n_list = n.query([1.0, 0.5, -1.5])
print(nlist)
