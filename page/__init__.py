from selenium.webdriver.common.by import By
"""以下为包名、启动名"""
app_appPackage = "com.bjcsxq.chat.carfriend"
app_appActivity = ".module_main.activity.MainActivity"
"""以下为登录配置数据"""
# 1. 关闭弹窗
login_close_alert = By.ID, "com.bjcsxq.chat.carfriend:id/dialog_close"
# 2. 点击我
login_me = By.ID, "com.bjcsxq.chat.carfriend:id/mine_layout"
# 3. 点击登录/注册
login_sig = By.ID, "com.bjcsxq.chat.carfriend:id/mine_username_tv"
# 4. 输入手机号
login_phone = By.ID, "com.bjcsxq.chat.carfriend:id/login_phone_et"
# 5. 输入密码
login_pwd = By.ID, "com.bjcsxq.chat.carfriend:id/login_pwd_et"
# 6. 点击登录
login_btn = By.ID, "com.bjcsxq.chat.carfriend:id/login_btn"
# 7. 点击签到 确定
login_sign = By.ID, "com.bjcsxq.chat.carfriend:id/btn_neg"
# 8. 获取异常提示信息
login_err_info = By.ID, "com.bjcsxq.chat.carfriend:id/txt_msg"
# 点击确定
login_confirm = By.ID, "com.bjcsxq.chat.carfriend:id/btn_pos"
# 获取昵称
login_nickname = By.ID, "com.bjcsxq.chat.carfriend:id/mine_username_tv"
# 设置
login_setting = By.ID, "com.bjcsxq.chat.carfriend:id/mine_set_rl"
# 退出
login_logout = By.ID, "com.bjcsxq.chat.carfriend:id/set_logout_tv"
# 确认退出
login_logout_ok = By.ID, "com.bjcsxq.chat.carfriend:id/bt_ok"