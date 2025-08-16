# Django-and-flutter-integration

This README documents the steps I applied to make a **Django web project** accessible from a **Flutter Android app** (using WebView).  
The setup allows the app running on a physical Android device (via USB) to load the Django site served on the laptop.
Also, I had to download Platform-tools from Android to be able to discover my device; make sure to add it to the path in variable environment. after that u can write on CMD adb devices and you should get your device number. 

## 1. Django Side 
The Django Project I already made it you will find it in my repositries but I changed instead of 6 motors I did for 4.
I will upload the new version of it 

### Run Django on localhost
As we always do test it on localhost by running the command in the terminal
```bash
python manage.py runserver 127.0.0.1:8000
```

### Why `127.0.0.1`?
- This means Django listens on the laptop only (localhost).  
- Since I am connecting the Android device via USB, I will mirror this port to the phone.

## 2. Flutter Side
In flutter you need to do these steps: 

### Add Internet Permission
In `android/app/src/main/AndroidManifest.xml`:
```xml
<uses-permission android:name="android.permission.INTERNET"/>
<application android:usesCleartextTraffic="true" ...>
```
These settings allow the Flutter app to connect to your local Django server over unencrypted HTTP; otherwise, the connection will be blocked.

### Use WebView
In `pubspec.yaml`:
```yaml
dependencies:
  webview_flutter: ^4.4.2
```
In `main.dart`, configure WebView to point to `http://127.0.0.1:8000/`.

### Map Laptop Port to Phone (adb reverse)
Run this once while the phone is connected via USB:
```bash
adb reverse tcp:8000 tcp:8000
```
This tells Android: "when you access **127.0.0.1:8000** on the phone, redirect traffic to the laptop's **127.0.0.1:8000**."  

## 3. Android NDK Warning

I saw a build warning about **NDK version mismatch**.  I looked up for soultions and this help
Solution: in `android/app/build.gradle.kts` add:
```kotlin
android {
    ndkVersion = "27.0.12077973"
}
```
This ensures consistency with plugins requiring NDK 27. The warning does not block the app, but this change removes it.

## 4. Summary of Key Changes

- Added `webview_flutter` dependency in Flutter.  
- Added `<uses-permission android:name="android.permission.INTERNET"/>` in AndroidManifest.  
- Added `android:usesCleartextTraffic="true"` to allow HTTP connections.  
- Used `adb reverse tcp:8000 tcp:8000` to tunnel phone traffic to laptop.  
- Must keep Django running at `127.0.0.1:8000`.  
- Adjusted `main.dart` to open `http://127.0.0.1:8000/` in WebView.  

---

## Notes: 
I did extra changes in codes because I was testing every way possible, but this one finally worked, ignore the others. 

---

## App Picture
<img width="494" height="991" alt="MotorsAdjust" src="https://github.com/user-attachments/assets/8b643bdc-29fa-4da8-976e-370a71698429" />

