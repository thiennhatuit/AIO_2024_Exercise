import torch 
import torch.nn as nn

class MySoftMax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self,x):
        x_exp = torch.exp(x)
        partition = x_exp.sum(0, keepdims = True)
        return x_exp/ partition
    
class SoftMaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self,x):
        x_max = torch.max(x,dim = 0, keepdims=True)
        x_exp = torch.exp(x - x_max.values)
        partition = x_exp.sum(0,keepdims=True)
        return x_exp/partition
    
data = torch.Tensor([1,2,3])
my_softmax = MySoftMax()
output = my_softmax(data)
print(output)

data2 = torch.Tensor([2,4,5000])
my_softmaxstable = SoftMaxStable()
output2 = my_softmaxstable(data2)
print(output2)