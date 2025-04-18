# File_Organizer
**Organize Files the Stress-Free Way**

File_Organizer works like a digital assistant for your files. It can combine automatic organization with human-friendly controls. It also can track every action, letting you experiment freely knowing you can always rewind mistakes.

### 📂 Smart Auto-Sorting and tools

- Automatically moves files to folders by type (documents, images, etc.).
- Finds duplicate files by content (not just names).
- Shows file previews for quick checking (text/images).
- Tracks every change in an activity log.

### ⏮️ Safety First

- Undo accidental file moves.
- Never lose files by mistake.



# **Graphical Abstract**

![Image](https://github.com/user-attachments/assets/24d32416-d1a0-4904-9258-ec238c6bc271)  
*This screenshot provides a visual representation of File_Organizer after opening a folder*

*(include files in the test_folder and fuctionalities)*



# **Purpose of the Software**

- **Type of Development Process:** 
  - Agile

- **Why Agile?** 
   1. **Flexibility and Adaptability**  
   Agile allows teams to respond quickly to changes in customer feedback. For our project, an ocean of new requiremnets will occur in our developing process as requirements are always cahnging.

  2. **Incremental Delivery**  
   Agile promotes delivering work in small. This  allows us to develop new functionalities setp by step and make adjustments regularly.

  3. **Faster Delivery**  
   By focusing on essential features first and iterating quickly, Agile helps our team deliver products to market faster than waterfall.

  
  
- **Possible Usage** 
  - Our software is **designed for** *file management and organization*, **targeting** *students, photographers, and everyday users*. It aims to simplify the process of organizing digital files, providing efficient auto-sorting, powerful duplicate detection, and instant previews.


# **Software Development Plan**

## Development Process
![Image](https://github.com/user-attachments/assets/0c7cb39b-4b25-46d9-8708-f91f04700b82)

We adopted **Scrum**—an Agile project management and product development framework—to break down the project into smaller, manageable tasks. Scrum helps people and teams deliver value incrementally in a collaborative way. As an agile framework, Scrum provides just enough structure for people and teams to integrate into how they work, while adding the right practices to optimize for their specific needs.

1. Requirement analysis: Product Owner gathers and understands the key requirements from students and  lecturers. Create a list of features required and put them to the product backlog.

2. Sprint Planning: Select items from the product backlog (work for 1-2 weeks) for the upcoming sprint.

3. Daily standups: Daily standups meetings to update each other on progress and identify any issues.

4. Sprint Execution: Develop the items from the sprint planning.

5. Sprint Review & Retrospective: Demonstrate the completed work to students, lecturers, administrators. Gather feedback and discuss with the team for the improvements needed.

6. Repeat Move on the next sprint with improved processes.

## Members
- **Frank**  
  - *Role:* Project Manager,Scrum Master,Product owner  
  - *Responsibilities:* Write the README file, plan the whole software development process, develop the software and test the software. 
  - *Portion:* 34%
- **David**  
  - *Role:* Developer  
  - *Responsibilities:* Help develop and test the software.
  - *Portion:* 33%
- **Max**  
  - *Role:* Developer  
  - *Responsibilities:* Help develop and test the software.  
  - *Portion:* 33%


## Schedule
- **Sprint 1 (Week 1-2):** Requirements gathering, basic framework development.
- **Sprint 2 (Week 3-4):** Files organization functionality development, initial UI/UX design.
- **Sprint 3 (Week 5):** Undo Moves functionality development.
- **Sprint 4 (Week 6):** Preview functionality development.
- **Sprint 5 (Week 7-8):** Find duplicates and View history functionality development.
- **Sprint 6 (Week 9):** Integration testing, user feedback collection, feature refinement.
- **Sprint 7 (Week 10):** Final testing, documentation.
![Image](https://github.com/user-attachments/assets/1f5685e3-dbb2-4b79-a45f-fe05707b2194)

## Algorithm

### Requirement Gathering

- Gathering, analyzing, and documenting the requirements of students and lecturers.
- Forming interviews and surveys to collect information.

### Design

- Functionalities and design elements are created based on the product backlog(or the requirements).
- Includes database(view history) design.
- Covers basic futionalities:
  - Organize files 
  - Undo moves
  - View history
  
### Implementation

- Actual coding and development of the application (Sprint Execution).

### Test / Validation
- Fix issues and bugs.
- Mainly test the new functionalities added in each specific sprint.

### Maintenance
- Bugs and errors will be fixed based on the users' feedback.

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
- [Software Demo Video](https://www.youtube.com/watch?v=iN4A1Ta1p-I&t=12s)



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
  - os: [PSF License](https://docs.python.org/3/license.html)  
  - shutil: [PSF License](https://docs.python.org/3/license.html)  
  - hashlib: [PSF License](https://docs.python.org/3/license.html)  
  - datetime: [PSF License](https://docs.python.org/3/license.html)  
  - json: [PSF License](https://docs.python.org/3/license.html)  
  - PIL (Pillow): [BSD License](https://github.com/python-pillow/Pillow/blob/main/LICENSE)  

*Note: The Python Standard Library components (e.g., tkinter, os, shutil, etc.) are distributed under the Python Software Foundation License (PSF License).*

*This document is subject to change as the project progresses.*