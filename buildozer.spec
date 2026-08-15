[app]

title = 翁法罗斯
package.name = omphalos
package.domain = org.omphalos

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt
# ✅ 你这里已经排除了 tests，做得非常对！
source.exclude_dirs = tests, docs, examples, .git

version = 1.0

# ✅ 建议修改：锁定 Python 3.11 版本，防止 p4a 误抓不兼容的 Python 3.14
requirements = python3==3.11.0,kivy

orientation = portrait

android.permissions =

android.ndk = 25c
android.accept_sdk_license = True
android.build_tools = 34.0.0

android.api = 33
android.minapi = 21

android.python_version = 3.11

android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
fullscreen = 0
android.entrypoint = org.kivy.android.PythonActivity
android.debug_artifact = apk

# ✅ 最关键的新增配置：绕过宿主系统 (GitHub Ubuntu) 头文件错误的 C 编译参数
android.pre_build_cmds = export CFLAGS="-D__GNUC_PREREQ(x,y)=1 -D__ANDROID__"

p4a.source_dir = ./p4a

[buildozer]
log_level = 2
warn_on_root = 1
