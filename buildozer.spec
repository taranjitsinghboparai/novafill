[app]
title = NovaFill
package.name = novafill
package.domain = org.novafill.app
source.dir = .
source.include_exts = py,png,jpg,ttf,otf,pdf
version = 1.1
requirements = python3,kivy,pillow,pytesseract,reportlab
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 33
android.minapi = 21
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.arch = arm64-v8a
