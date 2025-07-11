[app]
title            = NovaFill
package.name     = novafill
package.domain   = org.novafill.app
version          = 1.1
source.dir       = .
source.include_exts = py,png,jpg,ttf,otf,pdf
requirements     = python3,kivy,pillow,pytesseract,reportlab
orientation      = portrait
fullscreen       = 1

# --- python-for-android branch ---
p4a.branch       = develop

python_version   = 3.10
env.RL_NO_ACCEL  = 1          ; still fine – double safety

[android]
android.api      = 33
android.minapi   = 21
android.arch     = arm64-v8a
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
