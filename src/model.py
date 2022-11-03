class LinearQNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.linear2 = nn.Linear(hidden_size, output_size)

    def forward(self, state_tensor):
        # TODO: Write some code
        pass

    def save(self, file_name='model.pth'):
        # TODO: Write some code
        pass


class QTrainer:
    def __init__(self, model, lr, gamma):
        self.model = model
        self.lr = lr
        self.gamma = gamma

        self.optimizer = optim.Adam(model.parameters(), lr=lr)
        self.criterion = nn.MSELoss()  # Mean Squared Error (Q2 - Q1)^2 = loss

    def train_step(self, state, action, reward, next_state, done):
        # TODO: Write some code
        pass
