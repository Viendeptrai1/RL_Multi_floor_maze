# 🏢 RL Multi-Floor Maze

Dự án mô phỏng và huấn luyện AI (Agent) di chuyển trong môi trường mê cung nhiều tầng (Multi-Floor Maze) sử dụng các thuật toán Reinforcement Learning (Học tăng cường). Agent phải học cách tìm đường tới đích, né bẫy, thu thập tài nguyên (máu, đạn) và đối phó với kẻ địch.

---

## ✨ Những gì dự án đã làm được

Dự án hiện tại bao gồm các thành phần chính:

1. **Môi trường Multi-Floor Maze (Gymnasium)**:
   - Mô phỏng mê cung với lưới 2D/3D (nhiều tầng nối nhau qua cầu thang).
   - Tích hợp hệ thống sinh tồn: máu (HP), đạn (Ammo), thể lực (Stamina) và hệ thống tiếng ồn (Stealth).
   - Quái vật đa dạng: Patrol (Đi tuần), Chaser (Săn đuổi), Sniper (Bắn tỉa).
   - Hỗ trợ Render trực quan toàn bộ mê cung và các tác nhân bên trong.

2. **Huấn luyện bằng Reinforcement Learning**:
   - Sử dụng thư viện `stable-baselines3`.
   - Cài đặt và tuỳ biến các thuật toán: **PPO, A2C, DQN**.
   - Curriculum Learning: Huấn luyện qua 9 cấp độ (từ "Crawl" dễ nhất cho đến "Master" khó nhất).

3. **Cấu trúc File**:
   - `Multi_Floor_Maze.ipynb`: Chứa toàn bộ mã nguồn mô phỏng môi trường, trích xuất đặc trưng (Feature Extraction - CNN) và quy trình huấn luyện Agent.
   - `Multi_Floor_Maze.json`: File backup cấu trúc gốc dạng Zeppelin Notebook.

---

## 🛠 Cài đặt và Sử dụng

**Yêu cầu hệ thống:**
```bash
pip install gymnasium numpy torch stable-baselines3 Pillow
```

**Cách chạy:**
1. Mở file `Multi_Floor_Maze.ipynb` bằng Jupyter Notebook hoặc VS Code.
2. Chạy lần lượt các block để khởi tạo môi trường (Phần A).
3. Ở Phần B, thay đổi đường dẫn `MFM_ROOT` thành thư mục bạn muốn lưu model. Sau đó chạy các hàm `train_one("exp1_ppo")` hoặc `train_one("exp2_a2c")` để huấn luyện.

---

## 📚 Dành cho viết Tiểu luận / Báo cáo môn học

*(Phần này được đính kèm để hỗ trợ việc viết báo cáo dễ dàng và mạch lạc hơn)*

### 1. Bố cục đề xuất
1. Mở đầu: Giới thiệu bài toán mê cung sinh tồn nhiều tầng.
2. Cơ sở lý thuyết: Reinforcement Learning, PPO, A2C, DQN.
3. Xây dựng môi trường: State (Ảnh CNN + Vector trạng thái), Action (10 hành động), Reward.
4. Thực nghiệm & Ví dụ minh hoạ: So sánh hiệu năng các thuật toán qua các cấp độ.
5. Kết luận.

### 2. Cơ sở lý thuyết (Các công thức chính)
- **Phương trình Bellman (Q-value):**
  $$ Q^{\pi}(s, a) = \mathbb{E} \left[ r_t + \gamma V^{\pi}(s_{t+1}) | s_t=s, a_t=a \right] $$
- **A2C (Advantage Actor-Critic):** Sử dụng lợi thế (Advantage) $A(s,a) = r_t + \gamma V(s_{t+1}) - V(s_t)$.
  Loss của mạng chính sách: $$ L^{actor}(\theta) = -\mathbb{E} \left[ \log \pi_\theta(a|s) A(s, a) \right] $$
- **PPO (Proximal Policy Optimization):** Tránh cập nhật chính sách quá tay.
  $$ L^{CLIP}(\theta) = \mathbb{E} \left[ \min \left( r_t(\theta) A_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) A_t \right) \right] $$

### 3. Ví dụ chạy tay thuật toán (Step minh hoạ)
Giả sử Agent ở ô $(3,3)$ đang đối mặt với kẻ địch ở ô $(3,4)$.
- **State $s_t$**: Máu 1, đạn 1.
- **Actor quyết định**: Dự đoán $70\%$ nên "Bắn xuống" (Shoot Down). Agent thực hiện hành động này.
- **Environment phản hồi**: Kẻ địch bị tiêu diệt. Reward $r_t = +1.25$ (Diệt địch) - $0.04$ (Chi phí bắn) = $+1.21$. Đạn còn 0. Chuyển sang state $s_{t+1}$.
- **Critic tính toán**: 
  - Đánh giá $s_t$: $V(s_t) = -0.5$ (Nguy hiểm).
  - Đánh giá $s_{t+1}$: $V(s_{t+1}) = 1.5$ (An toàn hơn).
  - Tính lợi thế: $A = 1.21 + 0.99 \times 1.5 - (-0.5) = 3.195$.
- **Cập nhật**: Vì $A > 0$, hành động "Bắn" là tốt, mạng Neural sẽ tự động cập nhật trọng số để ưu tiên hành động này trong tương lai.
