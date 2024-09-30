# 初始化一个空的用户数据列表（字典列表）
users = []

# 增加用户
def create_user(name, age):
    # 自动生成用户ID
    user_id = len(users) + 1
    user = {"id": user_id, "name": name, "age": age}
    users.append(user)
    print(f"User {name} has been added with ID {user_id}.")

# 读取用户信息
def read_user(user_id):
    for user in users:
        if user['id'] == user_id:
            return user
    return f"User with ID {user_id} not found."

# 更新用户信息
def update_user(user_id, name=None, age=None):
    for user in users:
        if user['id'] == user_id:
            if name:
                user['name'] = name
            if age:
                user['age'] = age
            print(f"User {user_id} has been updated.")
            return
    print(f"User with ID {user_id} not found.")

# 删除用户
def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    print(f"User with ID {user_id} has been deleted.")

# 测试增删改查操作
create_user("Alice", 25)
create_user("Bob", 30)

print(read_user(1))  # 读取ID为1的用户信息
update_user(2, name="Bobby")  # 更新ID为2的用户信息
print(read_user(2))  # 读取更新后的用户信息
delete_user(1)  # 删除ID为1的用户
print(users)  # 查看所有剩余用户
