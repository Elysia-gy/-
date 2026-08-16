[app]

title = 翁法罗斯
package.name = omphalos
package.domain = org.omphalos

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt
# 排除测试目录，解决日志刷屏和超时问题
source.exclude_dirs = tests, docs, examples, .git

version = 1.0

requirements = python3==3.10,kivy

orientation = portrait

android.permissions =

android.ndk = 25b
android.accept_sdk_license = True
android.build_tools = 34.0.0

android.api = 33
android.minapi = 21

android.python_version = 3.10

android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
fullscreen = 0
android.entrypoint = org.kivy.android.PythonActivity
android.debug_artifact = apk

android.pre_build_cmds = export CFLAGS="-D__GNUC_PREREQ(x,y)=1 -D__ANDROID__"

p4a.source_dir = ./p4a

[buildozer]
log_level = 4
warn_on_root = 1
connect_timeout = 400
