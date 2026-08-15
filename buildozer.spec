[app]

title = 翁法罗斯
package.name = omphalos
package.domain = org.omphalos

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt
# 排除测试目录，解决日志刷屏和超时问题
source.exclude_dirs = tests, docs, examples, .git

version = 1.0

# ✅ 按你本地环境，锁定 Python 3.10，并指定同版本的 hostpython3
requirements = python3==3.10.0,hostpython3==3.10.0,kivy

orientation = portrait

android.permissions =

android.ndk = 25c
android.accept_sdk_license = True
android.build_tools = 34.0.0

android.api = 33
android.minapi = 21

# ✅ 这里同步改为 3.10
android.python_version = 3.10

android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
fullscreen = 0
android.entrypoint = org.kivy.android.PythonActivity
android.debug_artifact = apk

# ✅ 解决宿主系统头文件错误的编译参数（这个没变，必须保留）
android.pre_build_cmds = export CFLAGS="-D__GNUC_PREREQ(x,y)=1 -D__ANDROID__"

p4a.source_dir = ./p4a

[buildozer]
log_level = 2
warn_on_root = 1
