[app]
title = ZOKII BUILDER
package.name = zokiibuilder
package.domain = com.zokii.builder
source.dir =.
source.include_exts = py
version = 1.0
requirements = python3,kivy
orientation = portrait

[app:permissions]
android.permissions = INTERNET

[app:android]
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreements = True

[buildozer]
log_level = 2