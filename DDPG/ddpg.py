env = gym.make('Pendulum-v0') # tạo một environment
env.reset() #  reset lại environment, hàm reset() trả về state đầu tiên của environment
episodes = 10 # ta chạy 10 episodes
steps = 1000 # mỗi episodes ta chạy nhiều nhất 100 steps
for ep in range(episodes):
    state = env.reset()
    for step in range(steps):
        env.render() # gọi hàm render() để sinh ra animation, mình hay tắt đi vì nó gây crash trên window
        action = env.action_space.sample() # lấy 1 action ngẫu nhiên trong action space
        next_state, reward, done, _ = env.step(action) # thực thi action đó trên environment, giá trị trả về là state tiếp theo s', reward nhận được, và done (đã kết thúc episodes hay chưa)