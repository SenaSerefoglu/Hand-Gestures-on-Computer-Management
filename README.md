# Hand Gesture-Based Computer Control System

This project allows users to control various computer functions using predefined hand gestures captured in real-time via webcam. It is designed to enhance computer accessibility and user interaction, particularly for individuals with physical disabilities.

## 📄 Project Description
The system captures real-time hand gestures using a webcam and maps recognized gestures to specific computer commands such as:

- `Win + Tab`
- `Right Arrow`
- `Left Arrow`
- `Alt + F4`
- `Print Screen`
- `Volume Up`
- `Volume Down`
- `Enter`

### Key Technologies Used
- **MediaPipe**: For hand gesture recognition
- **OpenCV**: For camera integration and real-time frame capture
- **PyAutoGUI**: For triggering corresponding computer commands

## 🔬 Features
- Real-time hand gesture detection
- Custom image dataset creation
- Data augmentation (mirroring and rotation)
- Gesture-based control of system functions


## 🚀 Example Gestures
The dataset includes folders such as:
- `altf4`
- `enter`
- `sag` (right)
- `sol` (left)
- `sesac` (volume up)
- `seskapa` (volume down)
- `ss` (screenshot)
- `wintab`

## 📈 Future Work
- GUI interface to allow users to define custom gestures
- Macro assignment for more flexibility
- Improved performance metrics and latency reduction

