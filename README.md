## 📁 CAT-14 Image Bulk Rename Utility

A Tkinter-based GUI tool for batch-renaming JPEG files in a directory using their EXIF metadata (capture date), along with user-specified project metadata such as author, state, and location. Originally designed for Caltrans District 4 project documentation compliance.

---

### ⚙️ Features

* Select a target directory of `.jpg` images
* Extracts the `DateTimeOriginal` EXIF tag (tag `36867`)
* Applies a two-pass renaming strategy:

  1. **Date-stamped base name** (for initial sort)
  2. **Final Caltrans-compliant format**:

     ```
     YYYY-MM-DD - [state] - ROUTE 24, R5.97, R6.26 AND R6.51 - [author] - ####.jpg
     ```
* GUI options for:

  * Author name
  * Project state (`pre-con`, `mid-con`, `post-con`)
  * Location index (`1`–`12`)

---

### 🧱 Dependencies

All installable via `pip`:

* `Pillow` – for reading EXIF data from images
* `sv-ttk` – for modern themed UI components
* `tkinter` – built-in to Python, but requires system `tk` libraries

On Ubuntu/Debian systems:

```bash
sudo apt install python3-tk fonts-dejavu fonts-ubuntu
```

Python packages:

```bash
pip install pillow sv-ttk
```

---

### 🖥️ Running the App

#### Using a virtual environment (recommended):

```bash
python3 -m venv ~/venvs/img_sorter_env
source ~/venvs/img_sorter_env/bin/activate
pip install pillow sv-ttk
python img_sort.py
```

If on Wayland, force X11 for proper font rendering:

```bash
GDK_BACKEND=x11 python img_sort.py
```

---

### 📌 Notes

* Requires images to contain EXIF tag `36867` (`DateTimeOriginal`)
* Skips files missing this tag or named `Thumbs.db`
* Renames are **destructive** — no undo
* Designed/tested for Ubuntu systems with X11 (Wayland has known font issues)

---

Let me know if you want:

* Undo functionality
* Dry-run mode
* Exportable CSV log of before/after filenames
