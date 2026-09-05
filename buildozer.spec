[app]
# (str) Title of your application
title = لعبة الرعب

# (str) Package name
package.name = HorrorGame

# (str) Package domain (needed for android/ios packaging)
package.domain = com.nassimmrad64

# (str) Source code where the main.py live
source.dir = .

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (str) The format used to package the app
# (yes/no) Use fullscreen
fullscreen = 1

# (str) Presplash image
# presplash.filename = %(source.dir)s/data/presplash.png

# (int) Target API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android entry point, default is ok
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is 'import android'
#android.theme = '@android:style/Theme.NoTitleBar'

# (str) Icon
#icon.filename = %(source.dir)s/icon.png

# (list) Gradle dependencies
# android.gradle_dependencies = []
