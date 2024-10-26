
# MSD Project

## 项目简介
这是一个医疗管理系统的项目，包含医院用户认证、预约管理、住院信息管理等基础功能模块。后端使用 Python 编写，代码存放在 `backend/src/` 中，同时相关的测试代码存放在 `backend/tests/` 中。

---

## 项目结构

```bash
MSD_PROJECT/
│
├── backend/
│   ├── src/                    # 后端代码目录
│   │   ├── password_reset.py   # 密码重置功能
│   │   ├── doctor_register_patient.py  # 医生为病人预约专家
│   │   ├── access_medical_records.py   # 访问病历信息
│   │   └── ...                # 更多功能代码
│   └── tests/                 # 测试代码目录
│       ├── test_password_reset.py  # 密码重置测试
│       └── ...               # 更多测试代码
│
├── frontend/                  # 前端代码（假代码占位）
│   ├── public/
│   └── src/
│       └── components/
│           ├── Button/
│           ├── Dashboard/
│           ├── LoginPage/
│           └── ...           # 更多组件
│
└── .github/
    └── workflows/ci.yml      # GitHub Actions 配置文件
```

---

## 功能模块
1. **用户认证与账户管理**：
   - 用户可以重置密码。
   - 医生可以为病人注册账户。

2. **病历管理**：
   - 病人可以查看病历和医疗费用信息。
   - 医生可以更新病人的诊断和治疗计划。

3. **预约管理**：
   - 病人可以在线预约医生，选择合适的就诊时间。
   - 医生可以查看预约状态并合理安排时间。

4. **住院信息管理**：
   - 医生可以查看病人的病房和床位信息。
   - 系统会提醒医生病人的用药或测试时间。

---

## 使用说明

### 1. 克隆项目

```bash
git clone https://github.com/your-username/MSD_PROJECT.git
cd MSD_PROJECT
```

### 2. 后端依赖安装

确保你在 `backend/src/` 目录下有 `requirements.txt` 文件。如果没有依赖，跳过此步骤。

```bash
cd backend/src
pip install -r requirements.txt
```

### 3. 运行测试

使用以下命令运行测试：

```bash
cd backend/tests
pytest --maxfail=5 --disable-warnings
```

---

## GitHub Actions (CI)

该项目已配置 GitHub Actions，实现持续集成 (CI)。每次提交代码或创建 Pull Request 时，GitHub Actions 会自动运行测试，确保代码的稳定性。

**CI 配置文件位置**：
```
.github/workflows/ci.yml
```

---

## 贡献指南

1. **Fork** 这个仓库。
2. 创建你的功能分支：`git checkout -b feature/your-feature-name`。
3. 提交代码：`git commit -m 'Add some feature'`。
4. 推送到远程分支：`git push origin feature/your-feature-name`。
5. 提交一个 Pull Request。

---

## 许可证

该项目遵循 MIT 许可证 - 请查看 [LICENSE](LICENSE) 文件了解更多信息。

---

## 联系信息

如果有任何问题，请联系：
- **项目负责人**：Zhanbo Gong (z.gong.11@student.scu.edu.au)  
- **GitHub**：[ZhanboGong](https://github.com/ZhanboGong)
