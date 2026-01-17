[app]

# (str) Title of your application
title = Stok Takip

# (str) Package name
package.name = stoktakip

# (str) Package domain (needed for android/ios packaging)
package.domain = org.stoktakip

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,db

# (list) List of inclusions using pattern matching
source.include_patterns = logos/*.png,logos/*.jpg

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,sqlite3

# (str) Custom source folders for requirements
#requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/logos/Logo1.png

# (str) Supported orientation (comma-separated list: portrait, landscape, portrait-reverse, landscape-reverse)
orientation = portrait, landscape

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
#fullscreen = 0

# (string) Presplash animation using Lottie format.
# See https://lottie-files.com/ for examples and https://airbnb.design/lottie/
# for general documentation.
# Lottie files can be created using various tools, like Adobe After Effect, Synfig, etc.
#presplash.lottie = %(source.dir)s/data/presplash.json

# (str) Adaptive icon of the application (used if Android API level is 26+ at runtime)
#icon.adaptive.filename = %(source.dir)s/data/icon_adaptive.png

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (list) Android application meta-data to set (key=value format)
#android.meta_data =

# (list) Android library project to add (will be added in the
# project.properties automatically.)
#android.libraries =

# (list) Android shared libraries which will be added to the
# classpath.
#android.add_src =

# (list) Android additional gradle dependencies
#android.gradle_dependencies =

# (list) Android add java compile options
# this can for example be necessary when importing certain java libraries using the 'android.gradle_dependencies' option
# see https://developer.android.com/studio/write/java8-support for further information
# android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# (list) Android add aapt options
#android.aapt_options =

# (list) Android additional Java classes to add, as a list of Java class paths.
#android.add_java_classes =

# (list) Android add java compile options
# this can for example be necessary when importing certain java libraries using the 'android.gradle_dependencies' option
# see https://developer.android.com/studio/write/java8-support for further information
# android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# (list) Android add aapt options
#android.aapt_options =

# (list) Android additional Java classes to add, as a list of Java class paths.
#android.add_java_classes =

# (list) Android add Java files to add (as a list of paths)
#android.add_java_files =

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will not be enabled
#android.ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters =

# (str) launchMode to set for the main activity
#android.manifest.launch_mode = standard

# (list) Android additional libraries to copy into libs
#android.add_jars = foo.jar,bar.jar

# (list) Android additional libraries to copy into libs
#android.add_jars = foo.jar,bar.jar

# (list) Android additional libraries to copy into libs
#android.add_jars = foo.jar,bar.jar

# (list) Android additional libraries to copy into libs
#android.add_jars = foo.jar,bar.jar

# (str) Android logcat filters to use
#android.logcat_filters = *:S

# (str) Android additional adb arguments
#android.adb_args = -H host -P port

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# In past, was `android.arch` as we weren't supporting builds for multiple archs at the same time.
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) The format used to package the app for release mode (aab or apk).
# android.release_artifact = aab

# (str) The format used to package the app for debug mode (apk or aab).
# android.debug_artifact = apk

#
# Python for android (p4a) specific
#

# (str) The python version to use
#p4a.python_version = 3.11

# (str) The directory containing the python-for-android toolchain
#p4a.source_dir = .

# (str) The directory in which python-for-android should clone the toolchain
#p4a.local_recipes = .

# (str) The directory in which python-for-android should clone the toolchain
#p4a.bootstrap = sdl2

# (int) overrides automatic minimum sdk calculation for android and apk
#p4a.minimum_sdk_version = 21

# (int) overrides automatic target sdk calculation for android and apk
#p4a.target_sdk_version = 30

# (int) overrides automatic compile sdk version calculation for android and apk
#p4a.compile_sdk_version = 30

# (int) overrides automatic minimum ndk calculation for android and apk
#p4a.minimum_ndk_version = 23

# (str) The app theme, default is ok for Kivy-based app
# p4a.apptheme = "@android:style/Theme.NoTitleBar"

# (list) python-for-android whitelist of included permissons
#p4a.whitelist =

# (str) Path to a custom whitelist file
#p4a.whitelist_src =

# (str) Path to a custom blacklist file
#p4a.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
#p4a.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
#p4a.add_java_files = src/org/ouya/ouyaactivity.java

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will not be enabled
#p4a.ouya_category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#p4a.ouya_icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) Android logcat filters to use
#p4a.logcat_filters = *:S

# (bool) Android copy source instead of using bytecode_pyx
#p4a.android_copy_source = False

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
#p4a.arch = armeabi-v7a

# (str) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# In past, was `p4a.arch` as we weren't supporting builds for multiple archs at the same time.
#p4a.archs = armeabi-v7a, arm64-v8a

# (bool) enables Android auto backup feature (Android API >=23)
#p4a.allow_backup = True

# (str) The format used to package the app for release mode (aab or apk).
# p4a.release_artifact = aab

# (str) The format used to package the app for debug mode (apk or aab).
# p4a.debug_artifact = apk

#
# iOS specific
#

# (str) Path to a custom plist file that will be merged with the app one
#ios.plist =

# (str) Path to a custom entitlements file that will be merged with the app one
#ios.entitlements =

# (str) The iOS deployment target version
#ios.deployment_target = 11.0

# (str) The iOS minimum version supported
#ios.minimum_version = 11.0

# (str) The iOS SDK version to build against
#ios.sdk_version = 

# (str) The iOS archs to build for (comma-separated, choices: arm64, x86_64)
#ios.archs = arm64

# (str) The iOS simulator archs to build for (comma-separated, choices: arm64, x86_64)
#ios.simulator_archs = x86_64

# (str) The iOS device archs to build for (comma-separated, choices: arm64)
#ios.device_archs = arm64

# (bool) Whether or not to sign the code
#ios.codesign.allowed = false

# (str) Name of the certificate to use for signing the debug version (Get
# from the Apple dev portal)
#ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) The development team to use for signing the debug version (get it from
# the Apple dev portal at https://developer.apple.com/account/)
#ios.codesign.development_team.debug = <hexstring>

# (str) Name of the certificate to use for signing the release version (Get
# from the Apple dev portal)
#ios.codesign.release = %(ios.codesign.debug)s

# (str) The development team to use for signing the release version (get it
# from the Apple dev portal at https://developer.apple.com/account/)
#ios.codesign.development_team.release = <hexstring>

# (str) URL pointing to .ipa file to be installed. This is only needed for
# OTA (Over the Air) distribution.
#ios.manifest.app_url =

# (str) URL pointing to an icon (57x57px) to be displayed during download
# This is only needed for OTA distribution.
#ios.manifest.app_icon_url =

# (str) URL pointing to a plist file that is used for OTA distribution
#ios.manifest.plist_url =

# (str) URL pointing to an image (1024x1024px) to be displayed during download
# This is only needed for OTA distribution.
#ios.manifest.full_size_image_url =

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
# bin_dir = ./bin
