[app]
title = Alawami App
package.name = alawamiapp
package.domain = org.alawami
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,kivymd,pillow
orientation = portrait
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.private_storage = True
android.accept_sdk_license = True
android.archs = arm64-v8a,armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 0
