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
# Possible Usage

Our software is designed for **file management and organization**, targeting **students, photographers, and everyday users**. It aims to simplify the process of organizing digital files, providing efficient auto-sorting, powerful duplicate detection, and instant previews.




# **Software Development Plan**

## Development Process

We adopted Scrum—an Agile project management and product development framework—to break down the project into smaller, manageable tasks and facilitate iterative progress. This approach enabled the team to deliver a high-quality application more efficiently by focusing on a limited set of features at any given time. Moreover, Agile (Scrum) allows us to prioritize the needs of our stakeholders (students, lecturers, and administrators) from the very beginning of the software development life cycle.

### Requirement Analysis

- **Product Owner** gathers and understands the key requirements from students, lecturers, and administrators.
- Create a list of features required and add them to the **product backlog**.

### Sprint Planning

- Select items from the **product backlog** (work for 3 - 4 weeks) for the upcoming sprint.

### Daily Standups

- Daily standup meetings to update each other on progress and identify any issues.

### Sprint Execution

- Develop the items selected during sprint planning.

### Sprint Review and Retrospective

- Demonstrate the completed work to students, lecturers, and administrators.
- Gather feedback and discuss with the team for improvements needed.

### Repeat

- Move on to the next sprint with improved processes.


## Members
- **Frank**  
  - *Role:* Project Manager  
  - *Responsibilities:* Write the README file, plan the whole software development process, develop the software and test the software. 
  - *Portion:* 34%
- **David**  
  - *Role:* Developer  
  - *Responsibilities:* Help develop the software and test the software.
  - *Portion:* 33%
- **Max**  
  - *Role:* Developer  
  - *Responsibilities:* Help develop the software and test the software.  
  - *Portion:* 33%


## Schedule
- **Sprint 1 (Week 1-2):** Initial setup, requirements gathering, basic framework development.
- **Sprint 2 (Week 3-4):** Core feature development, initial UI/UX design.
- **Sprint 3 (Week 5-6):** Integration testing, user feedback collection, feature refinement.
- **Sprint 4 (Week 7-8):** Final testing, deployment preparation, documentation.
- **Post-Deployment:** Continuous support, updates, and feature enhancements based on user feedback.



## Algorithm

### Requirement Gathering

- Gathering, analyzing, and documenting the requirements of students, lecturers, and administrators.
- Forming interviews and surveys to collect information.

### Design

- System and design elements are created based on the requirements.
- Includes database schema designs and data flow diagrams.
- Covers basic structure and modules such as:
  - User authentication and authorization
  - Course and assignment management
- Plan out the product backlog for the upcoming Sprint (Sprint Planning).

### Implementation

- Actual coding and development of the application (Sprint Execution).
- Using version control systems like Git to collaborate and track changes to the codebase.

### Test / Validation

- Fix issues and bugs.
- Mainly test the newly added functionality for this Sprint.

### Deployment

- Deploy the code and update the application to the production environment.
- Review the improvements needed for the Sprint process and apply them (Sprint Review and Retrospective).
- Start another round of Sprint.

### Maintenance

- After each deployment, closely monitor bugs and errors.
- Address user feedback.



## Current Status

### Core Features Implemented

- Basic file organization (by file type)
- Duplicate file detection (content-based comparison)
- Full operation history tracking (undo all actions)
- File previews (images and text files)

### Current Performance

- Folder loading speed: ~500 files/second
- File moving speed: ~200 operations/second (SSD test)
- Memory usage: 150MB base + 50MB per 10,000 files
- Image preview generation: 0-5 seconds

### Known Issues

- Limited preview formats (no PDF/Office docs)
- UI freezes during large file processing
- Manual refresh required after external changes when checking history
- Special character path handling issues



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