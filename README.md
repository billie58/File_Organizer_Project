# File_Organizer
**Organize Files the Stress-Free Way**

File_Organizer works like a digital assistant for your files. It can combine automatic organization with human-friendly controls. It also can track every action, letting you experiment freely knowing you can always rewind mistakes. Regular updates keep the tool focus on real-world needs rather than unnecessary complexity.
### 📂 Smart Auto-Sorting and tools

- Automatically moves files to folders by type (documents, images, etc.).
- Finds duplicate files by content (not just names).
- Shows file previews for quick checking (text/images).
- Tracks every change in an activity log.

### ⏮️ Safety First

- Undo accidental file moves.
- All operations can be reversed.
- Never lose files by mistake.



# **Graphical Abstract**

![Image](https://github.com/user-attachments/assets/24d32416-d1a0-4904-9258-ec238c6bc271)  
*This screenshot provides a visual representation of File_Organizer after opening a folder*

*(include files in the test_folder and fuctionalities)*



# **Purpose of the Software**

## Software Development Process
- **Type of Development Process Applied:** Agile
- **Reason for Choosing Agile:** Agile allows for iterative development and continuous improvement, which is essential for our project given the dynamic nature of the target market and the need for rapid adaptation to user feedback.
- **Possible Usage (Target Market):** Our software is designed for [specific industry/field], targeting [target audience], such as [example users]. It aims to [describe the primary use case], providing [list key benefits].

## Perfect For:

- Students organizing projects
- Photographers managing images
- Anyone with a messy downloads folder


# **Software Development Plan**

## Development Process
- **Iterative Development:** We follow an Agile methodology with bi-weekly sprints.
- **Continuous Integration:** Code is integrated daily, with automated testing to ensure stability.
- **User Feedback Loop:** Regular user testing and feedback sessions are conducted to refine features and improve user experience.



## Members
- **Frank**  
  - *Role:* Project Manager  
  - *Responsibilities:* Oversee project timeline, coordinate team efforts, manage client communications.  
  - *Portion:* 34%
- **David**  
  - *Role:* Developer  
  - *Responsibilities:* Architectural design, core feature development, code reviews.  
  - *Portion:* 33%
- **Max**  
  - *Role:* Developer  
  - *Responsibilities:* User interface design, user experience testing, visual assets.  
  - *Portion:* 33%


## Schedule
- **Sprint 1 (Week 1-2):** Initial setup, requirements gathering, basic framework development.
- **Sprint 2 (Week 3-4):** Core feature development, initial UI/UX design.
- **Sprint 3 (Week 5-6):** Integration testing, user feedback collection, feature refinement.
- **Sprint 4 (Week 7-8):** Final testing, deployment preparation, documentation.
- **Post-Deployment:** Continuous support, updates, and feature enhancements based on user feedback.



## Algorithm

xxxxxxxxxxxxxxxxxxx




## Current Status
- **Core Features Implemented:** [List key features currently available]
- **Performance Metrics:** [Provide current performance metrics, such as speed, accuracy, etc.]
- **Known Issues:** [List any known bugs or limitations]



## Future Plan

### **--next 3-6 months**
### Core Feature Enhancements

- **Custom File Organization Rules**
  - Build on existing `organize_files()` with user-defined extension/date-based sorting

- **Multi-Level Undo/Redo**
  - Extend current `operation_stack` to track individual file movements

### Performance Essentials

- **SQLite History System**
  - Replace JSON logs with relational database

- **Preview Caching**
  - Reuse generated thumbnails/text previews

### UI Improvements

- **Keyboard Navigation**
  - Add hotkeys for common actions

- **Theme Engine Foundation**
  - Extend `ttkbootstrap` integration for dark/light modes
---
### **--next 6-12 months**
### Advanced Functionality

- **Lazy-Loading Directories**
  - Implement incremental loading for large folders



- **Cloud Storage Integration**
  - Start with Google Drive API integration

### Architecture Upgrades

- **Core/UI Separation**
  - Prepare for potential cross-platform development

- **Plugin System Prototype**
  - Modular architecture for future extensions

### AI Foundations

- **Basic ML Classification**
  - File type recognition using existing metadata

- **Auto-Tagging System**
  - Leverage file content analysis


# **Additional Components**

## Domo (YouTube URL)
- [Software Demo Video](https://www.youtube.com/watch?v=example)



## Environments of the Software Development and Running
- **Programming Language:** Python

- **Minimum H/W Requirements:**
  - CPU: 1.5 GHz Dual-core processor
  - RAM: 4 GB
  - Storage: 500 MB free space

- **Minimum S/W Requirements:**
  - Operating System: Windows 7+, macOS 10.12+, Linux (Ubuntu 18.04+)
  - Python Version: 3.7+
  
- **Required Packages:**  
  - tkinter  
  - ttk
  - filedialog
  - messagebox
  - ttkbootstrap
  - os  
  - shutil  
  - hashlib  
  - datetime  
  - json
  - PIL



## Declaration
- **Open Source Components and Packages:**  
  - tkinter: [PSF License](https://docs.python.org/3/license.html)  
  - ttk: [PSF License](https://docs.python.org/3/license.html)  
  - filedialog: [PSF License](https://docs.python.org/3/license.html)  
  - messagebox: [PSF License](https://docs.python.org/3/license.html)  
  - ttkbootstrap: [MIT License](https://github.com/israel-dryer/ttkbootstrap/blob/main/LICENSE)  
  - os: [PSF License](https://docs.python.org/3/license.html)  
  - shutil: [PSF License](https://docs.python.org/3/license.html)  
  - hashlib: [PSF License](https://docs.python.org/3/license.html)  
  - datetime: [PSF License](https://docs.python.org/3/license.html)  
  - json: [PSF License](https://docs.python.org/3/license.html)  
  - PIL (Pillow): [BSD License](https://github.com/python-pillow/Pillow/blob/main/LICENSE)  

*Note: The Python Standard Library components (e.g., tkinter, os, shutil, etc.) are distributed under the Python Software Foundation License (PSF License).*

*This document is subject to change as the project progresses.*