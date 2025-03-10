import torch
import torch.nn.functional as F
import torch.nn as nn

class Model(nn.Module):

  def __init__(self, input_size=4, hl1=17, hl2=11, hl3=12, output_size=3):
    super().__init__()
    self.fc1 = nn.Linear(input_size,hl1)
    self.fc2 = nn.Linear(hl1, hl2)
    self.fc3 = nn.Linear(hl2, hl3)
    self.fout = nn.Linear(hl3, output_size)

  def forward(self, x):
    x = F.relu(self.fc1(x))
    x = F.relu(self.fc2(x))
    x = F.relu(self.fc3(x))
    x = self.fout(x)

    return x

new_model = Model()
new_model.load_state_dict(torch.load("NeuraD.pt", map_location=torch.device("cpu")))
new_model.eval()

