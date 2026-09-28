[app]
title = PS4 Car Cooker
package.name = ps4carcooker
package.domain = org.alawami
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt
version = 1.0
requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# الإصدار المستقر والقديم الذي يحتوي على أداة Aidl تلقائياً لمنع الخطأ
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk_api = 21
android.private_storage = True

android.archs = arm64-v8a
android.allow_backup = True