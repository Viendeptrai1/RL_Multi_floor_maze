# RL Multi-Floor Maze

Dự án mô phỏng và huấn luyện AI (Agent) di chuyển trong môi trường mê cung nhiều tầng (Multi-Floor Maze) sử dụng các thuật toán Reinforcement Learning (Học tăng cường). Agent phải học cách tìm đường tới đích, né bẫy, thu thập tài nguyên (máu, đạn) và đối phó với kẻ địch.

---

## Những gì dự án đã làm được

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

## Cài đặt và Sử dụng

**Yêu cầu hệ thống:**

```bash
pip install gymnasium numpy torch stable-baselines3 Pillow
```

**Cách chạy:**

1. Cài đặt Zeppelin phiên bản 0.8.2
2. Import file Json "Multi_Floor_Maze.json"
3. Cài đặt thư viện và chạy tất cả các cell theo hướng dẫn trong file notebook sau khi import
