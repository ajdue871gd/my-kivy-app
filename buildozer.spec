[app]
title = Periodic App
package.name = periodicapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp3,gif
version = 0.1
requirements = python3,kivy,cython==0.29.33
orientation = portrait
osx.kivy_version = 2.1.0
fullscreen = 0
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True
android.skip_update = False
android.permissions = RECEIVE_BOOT_COMPLETED, FOREGROUND_SERVICE, READ_EXTERNAL_STORAGE, SYSTEM_ALERT_WINDOW
android.services = myservice:service.py
android.boot_service = myservice
log_level = 1
# (int) Android NDK version to use
android.ndk = 26b
p4a.branch = develop
